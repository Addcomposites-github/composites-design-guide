"""Report generation service.

Generates a well-formatted Markdown report from an analysis response,
and optionally converts it to PDF via WeasyPrint.
"""

from __future__ import annotations

import io
import logging
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Markdown report generation
# ---------------------------------------------------------------------------

def generate_markdown_report(analysis: Dict[str, Any]) -> str:
    """Create a human-readable Markdown report from a full analysis result.

    Parameters
    ----------
    analysis : dict
        Dict with keys ``part_analysis``, ``material_recommendation``,
        ``laminate_design``, ``manufacturing_plan``, ``cost_estimate``,
        ``risk_assessment``.

    Returns
    -------
    str
        Markdown-formatted report string.
    """
    sections: List[str] = []

    # Header
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    sections.append(
        f"# Composites Manufacturing Plan\n\n"
        f"*Generated on {timestamp} by the "
        f"[Composites Design Platform](https://github.com/addcomposites)*\n"
    )

    # ---- 1. Part Analysis ----
    pa = analysis.get("part_analysis", {})
    sections.append("## 1. Part Analysis\n")
    if pa:
        rows = [
            ("Geometry type", pa.get("geometry_type", "N/A")),
            ("Estimated dimensions", pa.get("estimated_dimensions", "N/A")),
            ("Curvature", pa.get("curvature", "N/A")),
            ("Complexity", pa.get("complexity", "N/A")),
        ]
        for label, value in rows:
            sections.append(f"- **{label}:** {value}")

        load_paths = pa.get("load_paths", [])
        if load_paths:
            sections.append("\n**Load paths:**")
            for lp in load_paths:
                sections.append(f"- {lp}")

        challenges = pa.get("manufacturing_challenges", [])
        if challenges:
            sections.append("\n**Manufacturing challenges:**")
            for ch in challenges:
                sections.append(f"- {ch}")
    sections.append("")

    # ---- 2. Material Recommendation ----
    mr = analysis.get("material_recommendation", {})
    sections.append("## 2. Material Recommendation\n")
    if mr:
        sections.append(f"- **Fibre type:** {mr.get('fibre_type', 'N/A')}")
        sections.append(f"- **Fibre form:** {mr.get('fibre_form', 'N/A')}")
        sections.append(f"- **Resin system:** {mr.get('resin_system', 'N/A')}")
        reasoning = mr.get("reasoning", "")
        if reasoning:
            sections.append(f"\n{reasoning}")
    sections.append("")

    # ---- 3. Laminate Design ----
    ld = analysis.get("laminate_design", {})
    sections.append("## 3. Laminate Design\n")
    if ld:
        seq = ld.get("stacking_sequence", [])
        seq_str = ", ".join(str(a) for a in seq) if seq else "N/A"
        sections.append(f"- **Stacking sequence:** [{seq_str}]")
        sections.append(f"- **Number of plies:** {ld.get('num_plies', 'N/A')}")
        sections.append(
            f"- **Estimated thickness:** "
            f"{ld.get('estimated_thickness_mm', 'N/A')} mm"
        )
        reinforcements = ld.get("local_reinforcements", [])
        if reinforcements:
            sections.append("\n**Local reinforcements:**")
            for r in reinforcements:
                sections.append(f"- {r}")
    sections.append(
        "\n> Use [AddStack](https://addstack.addcomposites.com) to calculate "
        "the full ABD matrix and run failure analysis for this laminate."
    )
    sections.append("")

    # ---- 4. Manufacturing Plan ----
    mp = analysis.get("manufacturing_plan", {})
    sections.append("## 4. Manufacturing Plan\n")
    if mp:
        sections.append(
            f"**Recommended process:** {mp.get('recommended_process', 'N/A')}\n"
        )
        steps = mp.get("steps", [])
        if steps:
            sections.append("**Steps:**")
            for i, step in enumerate(steps, 1):
                sections.append(f"{i}. {step}")

        materials = mp.get("required_materials", [])
        if materials:
            sections.append("\n**Required materials:**")
            for m in materials:
                sections.append(f"- {m}")

        consumables = mp.get("required_consumables", [])
        if consumables:
            sections.append("\n**Required consumables:**")
            for c in consumables:
                sections.append(f"- {c}")

        tooling = mp.get("tooling_notes", "")
        if tooling:
            sections.append(f"\n**Tooling notes:** {tooling}")
    sections.append("")

    # ---- 5. Cost Estimate ----
    ce = analysis.get("cost_estimate", {})
    sections.append("## 5. Cost Estimate\n")
    if ce:
        sections.append("| Component | Cost (USD) |")
        sections.append("|-----------|-----------|")
        sections.append(
            f"| Material | ${ce.get('material_cost', 0):.2f} |"
        )
        sections.append(
            f"| Labour | ${ce.get('labour_cost', 0):.2f} |"
        )
        sections.append(
            f"| Tooling (amortised) | ${ce.get('tooling_cost', 0):.2f} |"
        )
        sections.append(
            f"| Consumables | ${ce.get('consumables_cost', 0):.2f} |"
        )
        sections.append(
            f"| **Total** | **${ce.get('total_cost', 0):.2f}** |"
        )
        notes = ce.get("breakdown_notes", [])
        if notes:
            sections.append("\n**Notes:**")
            for n in notes:
                sections.append(f"- {n}")
        disclaimer = ce.get("disclaimer", "")
        if disclaimer:
            sections.append(f"\n> {disclaimer}")
    else:
        sections.append(
            "*Cost estimation was not performed. Use the "
            "`/api/estimate-cost` endpoint for a detailed breakdown.*"
        )
    sections.append("")

    # ---- 6. Risk Assessment ----
    ra = analysis.get("risk_assessment", {})
    sections.append("## 6. Risk Assessment\n")
    if ra:
        failure_modes = ra.get("failure_modes", [])
        if failure_modes:
            sections.append("**Potential failure modes:**")
            for fm in failure_modes:
                sections.append(f"- {fm}")

        inspection = ra.get("inspection_points", [])
        if inspection:
            sections.append("\n**Inspection points:**")
            for ip in inspection:
                sections.append(f"- {ip}")

        safety = ra.get("safety_factors", "")
        if safety:
            sections.append(f"\n**Safety factors:** {safety}")

        defects = ra.get("common_defects", [])
        if defects:
            sections.append("\n**Common defects to watch for:**")
            for d in defects:
                sections.append(f"- {d}")
    sections.append("")

    # ---- Footer ----
    sections.append("---\n")
    sections.append("## Recommended Free Tools\n")
    sections.append(
        "- [AddStack](https://addstack.addcomposites.com) -- Laminate design, "
        "CLT calculations, failure criteria\n"
        "- [eLamX2](https://elamx2.de) -- Open-source CLT tool from "
        "TU Dresden\n"
        "- [Resin Flow Simulator]"
        "(https://www.addcomposites.com/addcomposites-apps/resin-flow) "
        "-- VARTM infusion simulation\n"
    )
    sections.append(
        "> **Disclaimer:** This report is for educational and guidance "
        "purposes only. It is not a substitute for professional engineering "
        "judgement, company-specific design manuals, or regulatory "
        "certification requirements. Always verify design decisions with a "
        "qualified composites engineer.\n"
    )

    return "\n".join(sections)


# ---------------------------------------------------------------------------
# PDF generation (optional)
# ---------------------------------------------------------------------------

def generate_pdf_report(markdown_content: str) -> bytes:
    """Convert a Markdown report to PDF bytes.

    Uses ``markdown`` to convert to HTML, then ``weasyprint`` to render
    the HTML as a PDF.  If WeasyPrint is not installed, raises a
    RuntimeError with installation instructions.

    Parameters
    ----------
    markdown_content : str
        The markdown report text.

    Returns
    -------
    bytes
        The PDF file content.
    """
    try:
        import markdown as md_lib
    except ImportError as exc:
        raise RuntimeError(
            "The 'markdown' package is required for PDF generation. "
            "Install it with: pip install markdown"
        ) from exc

    try:
        from weasyprint import HTML
    except ImportError as exc:
        raise RuntimeError(
            "WeasyPrint is required for PDF generation. "
            "Install it with: pip install weasyprint  "
            "(may require system-level dependencies -- see "
            "https://doc.courtbouillon.org/weasyprint/stable/first_steps.html)"
        ) from exc

    # Convert markdown to HTML
    html_body = md_lib.markdown(
        markdown_content,
        extensions=["tables", "fenced_code"],
    )

    # Wrap in a minimal HTML page with basic styling
    full_html = f"""\
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Composites Manufacturing Plan</title>
<style>
  body {{
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    max-width: 800px;
    margin: 40px auto;
    padding: 0 20px;
    color: #333;
    line-height: 1.6;
  }}
  h1 {{ color: #1a5276; border-bottom: 2px solid #1a5276; padding-bottom: 8px; }}
  h2 {{ color: #2e86c1; margin-top: 30px; }}
  table {{ border-collapse: collapse; width: 100%; margin: 16px 0; }}
  th, td {{ border: 1px solid #ccc; padding: 8px 12px; text-align: left; }}
  th {{ background: #f0f4f8; }}
  blockquote {{
    border-left: 4px solid #2e86c1;
    margin: 16px 0;
    padding: 8px 16px;
    background: #f8f9fa;
    color: #555;
  }}
  code {{ background: #f0f0f0; padding: 2px 6px; border-radius: 3px; }}
  a {{ color: #2e86c1; }}
</style>
</head>
<body>
{html_body}
</body>
</html>
"""

    # Render to PDF
    pdf_bytes = HTML(string=full_html).write_pdf()
    return pdf_bytes
