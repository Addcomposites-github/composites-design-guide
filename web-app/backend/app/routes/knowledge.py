"""Knowledge base routes -- search, article retrieval, and stacking rule checks.

GET   /api/search?query=...&top_n=5   Search the knowledge base.
GET   /api/article/{dir}/{filename}   Retrieve a single article as markdown.
POST  /api/check-stacking             Verify a stacking sequence against
                                       standard design rules.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, Optional

from fastapi import APIRouter, HTTPException, Query

from app.config import settings
from app.models.schemas import (
    SearchResponse,
    StackingCheckRequest,
    StackingCheckResponse,
)
from app.services import knowledge_service, stacking_service

router = APIRouter(tags=["knowledge"])


@router.get(
    "/search",
    response_model=SearchResponse,
    summary="Search the composites knowledge base",
    description=(
        "Full-text search across all knowledge articles using a "
        "lightweight TF-IDF scoring model.  Searches titles, tags, "
        "categories, and article content."
    ),
)
async def search_knowledge(
    query: str = Query(
        ...,
        min_length=1,
        description="Natural-language search query.",
    ),
    top_n: Optional[int] = Query(
        default=5,
        ge=1,
        le=20,
        description="Number of results to return (default 5, max 20).",
    ),
) -> SearchResponse:
    """Search the knowledge index."""
    results = knowledge_service.search(query, top_n=top_n or 5)
    return SearchResponse(results=results, count=len(results))


@router.get(
    "/article/{directory}/{filename}",
    summary="Get a knowledge base article",
    description=(
        "Returns the raw markdown content and front-matter metadata "
        "for a single knowledge base article."
    ),
)
async def get_article(directory: str, filename: str) -> Dict[str, Any]:
    """Read and return a single knowledge article."""
    # Sanitise path components to prevent traversal
    safe_dir = Path(directory).name
    safe_file = Path(filename).name
    if not safe_file.endswith(".md"):
        safe_file += ".md"

    article_path = settings.KNOWLEDGE_DIR / safe_dir / safe_file
    if not article_path.is_file():
        raise HTTPException(
            status_code=404,
            detail=f"Article '{safe_dir}/{safe_file}' not found.",
        )

    content = article_path.read_text(encoding="utf-8")

    # Parse simple YAML front-matter if present
    title = safe_file.replace(".md", "").replace("-", " ").title()
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            for line in parts[1].strip().splitlines():
                if line.startswith("title:"):
                    title = line.split(":", 1)[1].strip().strip('"').strip("'")
                    break

    return {
        "title": title,
        "directory": safe_dir,
        "filename": safe_file,
        "content": content,
    }


@router.post(
    "/check-stacking",
    response_model=StackingCheckResponse,
    summary="Check laminate stacking rules",
    description=(
        "Verifies a stacking sequence against standard composite design "
        "rules: symmetry, balance, 10 %% rule, and consecutive ply limit."
    ),
)
async def check_stacking(
    request: StackingCheckRequest,
) -> StackingCheckResponse:
    """Run stacking rule checks on the given angle sequence."""
    results = stacking_service.check_all(
        angles=request.angles,
        max_consecutive=request.max_consecutive or 4,
    )
    all_passed = all(r["passed"] for r in results)
    return StackingCheckResponse(results=results, all_passed=all_passed)
