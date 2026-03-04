"""Vision service -- Claude API integration for photo-to-plan analysis.

Uses the Anthropic Python SDK to call Claude with optional image input.
Builds a structured prompt requesting JSON output covering part analysis,
material recommendation, laminate design, manufacturing plan, cost
estimate context, and risk assessment.
"""

from __future__ import annotations

import json
import logging
from typing import Any, Dict, List, Optional

from app.config import settings
from app.services import knowledge_service

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Prompt construction
# ---------------------------------------------------------------------------

_SYSTEM_PROMPT = """\
You are a composites engineering expert AI assistant.  You help makers, \
students, and engineers design and manufacture composite (fibre-reinforced \
polymer) parts.

When given a part description (and optionally a photo), you must return a \
single JSON object with exactly these top-level keys:

{
  "part_analysis": {
    "geometry_type": "<flat | single_curvature | double_curvature | axisymmetric | constant_cross_section>",
    "estimated_dimensions": "<string, e.g. '400 x 200 x 3 mm'>",
    "curvature": "<none | gentle | moderate | tight>",
    "complexity": "<simple | moderate | complex>",
    "load_paths": ["<string describing each primary load path>"],
    "manufacturing_challenges": ["<string>"]
  },
  "material_recommendation": {
    "fibre_type": "<Carbon | Glass | Aramid | Basalt | Hybrid>",
    "fibre_form": "<UD | Woven | NCF | Chopped Strand Mat>",
    "resin_system": "<Epoxy | Polyester | Vinyl Ester | Phenolic>",
    "reasoning": "<string explaining why these materials suit the application>"
  },
  "laminate_design": {
    "stacking_sequence": [<list of angles as numbers, e.g. 0, 45, -45, 90, ...]>,
    "num_plies": <integer>,
    "estimated_thickness_mm": <float>,
    "local_reinforcements": ["<string describing where and why>"]
  },
  "manufacturing_plan": {
    "recommended_process": "<wet-layup | vacuum-bagging | resin-infusion-vartm | prepreg-autoclave | afp | rtm | filament-winding | pultrusion>",
    "steps": ["<ordered list of manufacturing steps>"],
    "required_materials": ["<string>"],
    "required_consumables": ["<string>"],
    "tooling_notes": "<string>"
  },
  "risk_assessment": {
    "failure_modes": ["<string>"],
    "inspection_points": ["<string>"],
    "safety_factors": "<string, e.g. 'Use a minimum safety factor of 2.0 for hobbyist parts'>",
    "common_defects": ["<string>"]
  }
}

Rules:
- Respond ONLY with the JSON object -- no markdown fences, no commentary.
- Tailor recommendations to the stated skill level.
- If the skill level is "beginner", prefer simpler processes (wet layup, \
  vacuum bagging) and forgiving materials (glass/epoxy, woven fabrics).
- Always design a symmetric, balanced laminate that satisfies the 10% rule.
- Include at least one 0, one 90, and one +/-45 pair in every laminate.
- Be conservative with safety factors for hobby/beginner use.
"""


def _build_knowledge_context(description: str, intended_use: str) -> str:
    """Search the knowledge base and format relevant excerpts for the prompt."""
    queries = [description, intended_use]
    seen_titles: set[str] = set()
    snippets: List[str] = []

    for q in queries:
        results = knowledge_service.search(q, top_n=3)
        for r in results:
            title = r.get("title", "")
            if title in seen_titles:
                continue
            seen_titles.add(title)
            snippet = r.get("snippet", "")[:300]
            snippets.append(f"### {title}\n{snippet}")

    if not snippets:
        return ""

    return (
        "\n\n--- RELEVANT KNOWLEDGE BASE CONTEXT ---\n"
        + "\n\n".join(snippets)
        + "\n--- END CONTEXT ---\n"
    )


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

async def analyze_part(
    description: str,
    intended_use: str,
    skill_level: str = "beginner",
    photo_base64: Optional[str] = None,
    api_key: Optional[str] = None,
) -> Dict[str, Any]:
    """Call Claude to analyze a composite part and return a structured plan.

    Parameters
    ----------
    description : str
        Plain-language description of the part.
    intended_use : str
        How the part will be used, key loads.
    skill_level : str
        ``"beginner"``, ``"intermediate"``, or ``"advanced"``.
    photo_base64 : str, optional
        Base64-encoded image (JPEG or PNG).

    Returns
    -------
    dict
        Parsed JSON with keys: ``part_analysis``,
        ``material_recommendation``, ``laminate_design``,
        ``manufacturing_plan``, ``risk_assessment``.

    Raises
    ------
    RuntimeError
        If the Anthropic API key is not configured or the API call fails.
    ValueError
        If Claude returns non-JSON output.
    """
    effective_key = api_key or settings.ANTHROPIC_API_KEY
    if not effective_key:
        raise RuntimeError(
            "ANTHROPIC_API_KEY is not set. "
            "Configure it in the environment or in web-app/backend/.env"
        )

    # Lazy import so the module can be imported even without the SDK installed
    try:
        import anthropic
    except ImportError as exc:
        raise RuntimeError(
            "The 'anthropic' package is required for vision analysis. "
            "Install it with: pip install anthropic"
        ) from exc

    knowledge_context = _build_knowledge_context(description, intended_use)

    # Build the user message content blocks
    user_content: List[Dict[str, Any]] = []

    # If a photo was provided, add it as an image block
    if photo_base64:
        # Detect media type from the base64 header or default to JPEG
        media_type = "image/jpeg"
        if photo_base64.startswith("/9j/"):
            media_type = "image/jpeg"
        elif photo_base64.startswith("iVBOR"):
            media_type = "image/png"

        user_content.append(
            {
                "type": "image",
                "source": {
                    "type": "base64",
                    "media_type": media_type,
                    "data": photo_base64,
                },
            }
        )

    # Text block with the request
    user_text = (
        f"Analyze this composite part and create a manufacturing plan.\n\n"
        f"**Part description:** {description}\n"
        f"**Intended use:** {intended_use}\n"
        f"**Builder skill level:** {skill_level}\n"
        f"{knowledge_context}\n\n"
        f"Return ONLY a JSON object following the schema described in the "
        f"system prompt."
    )
    user_content.append({"type": "text", "text": user_text})

    # Call Claude
    client = anthropic.Anthropic(api_key=effective_key)

    try:
        response = client.messages.create(
            model=settings.CLAUDE_MODEL,
            max_tokens=4096,
            system=_SYSTEM_PROMPT,
            messages=[
                {"role": "user", "content": user_content},
            ],
        )
    except anthropic.APIError as exc:
        logger.error("Anthropic API error: %s", exc)
        raise RuntimeError(f"Claude API call failed: {exc}") from exc

    # Extract text from response
    raw_text = ""
    for block in response.content:
        if hasattr(block, "text"):
            raw_text += block.text

    # Strip markdown fences if present
    raw_text = raw_text.strip()
    if raw_text.startswith("```"):
        # Remove opening fence
        first_newline = raw_text.index("\n") if "\n" in raw_text else 3
        raw_text = raw_text[first_newline + 1:]
    if raw_text.endswith("```"):
        raw_text = raw_text[:-3].rstrip()

    # Parse JSON
    try:
        result = json.loads(raw_text)
    except json.JSONDecodeError as exc:
        logger.error("Claude returned non-JSON: %s", raw_text[:500])
        raise ValueError(
            f"Claude returned non-JSON output. First 300 chars: "
            f"{raw_text[:300]}"
        ) from exc

    # Ensure all expected keys exist (fill missing with empty dicts)
    expected_keys = [
        "part_analysis",
        "material_recommendation",
        "laminate_design",
        "manufacturing_plan",
        "risk_assessment",
    ]
    for key in expected_keys:
        if key not in result:
            result[key] = {}

    return result
