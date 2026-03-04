"""Knowledge base search service.

Loads the pre-built index.json and provides a lightweight TF-IDF-like
search over knowledge article titles, tags, categories, and full content.
This is a direct Python port of the search logic in mcp-server/src/index.ts.
"""

from __future__ import annotations

import json
import math
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from app.config import settings


# ---------------------------------------------------------------------------
# Types
# ---------------------------------------------------------------------------

IndexEntry = Dict[str, Any]
"""A single entry from index.json with keys: file, dir, url, title,
category, tags, difficulty, related, tools, last_updated, content."""


# ---------------------------------------------------------------------------
# Module-level state
# ---------------------------------------------------------------------------

_index: List[IndexEntry] = []
_loaded: bool = False


# ---------------------------------------------------------------------------
# Loading
# ---------------------------------------------------------------------------

def load(index_path: Optional[Path] = None) -> None:
    """Load (or reload) the knowledge index from disk.

    Parameters
    ----------
    index_path : Path, optional
        Override for the index.json location.  Defaults to
        ``settings.INDEX_PATH``.
    """
    global _index, _loaded
    path = index_path or settings.INDEX_PATH
    try:
        with open(path, "r", encoding="utf-8") as fh:
            _index = json.load(fh)
        _loaded = True
    except Exception as exc:
        print(f"Warning: Could not load index.json at {path}: {exc}")
        _index = []
        _loaded = True  # Mark loaded so we don't retry on every request


def _ensure_loaded() -> None:
    if not _loaded:
        load()


# ---------------------------------------------------------------------------
# Tokenisation helpers
# ---------------------------------------------------------------------------

_TOKEN_RE = re.compile(r"[^a-z0-9+\-/]+")


def tokenize(text: str) -> List[str]:
    """Tokenize a string into lowercase alphanumeric tokens.

    Matches the behaviour of the TypeScript ``tokenize()`` function:
    replace non-alphanumeric characters (keeping ``+``, ``-``, ``/``)
    with spaces, split, and keep tokens longer than 1 character.
    """
    lowered = text.lower()
    parts = _TOKEN_RE.sub(" ", lowered).split()
    return [t for t in parts if len(t) > 1]


# ---------------------------------------------------------------------------
# TF-IDF scoring
# ---------------------------------------------------------------------------

def _idf(term: str, all_doc_tokens: List[List[str]]) -> float:
    """Compute inverse document frequency for *term* across the corpus."""
    count = sum(1 for doc in all_doc_tokens if term in doc)
    if count == 0:
        return 0.0
    return math.log(len(all_doc_tokens) / count)


def _score_document(
    entry: IndexEntry,
    query_tokens: List[str],
    all_doc_tokens: List[List[str]],
) -> float:
    """Score a single document against the query tokens.

    Weighting mirrors the TypeScript implementation:
    - Title exact match: 10 * IDF
    - Title partial match: 5 * IDF
    - Tag exact match: 8 * IDF
    - Tag partial match: 4 * IDF
    - Category exact match: 6 * IDF
    - Content TF: tf * IDF * 0.1
    - Content partial TF: partial_tf * IDF * 0.03
    """
    title_tokens = tokenize(entry.get("title", ""))
    tag_tokens: List[str] = []
    for tag in entry.get("tags", []):
        tag_tokens.extend(tokenize(tag))
    category_tokens = tokenize(entry.get("category", ""))
    content_tokens = tokenize(entry.get("content", ""))

    score = 0.0
    for qt in query_tokens:
        term_idf = _idf(qt, all_doc_tokens)

        # Title exact match
        if qt in title_tokens:
            score += 10.0 * term_idf
        # Title partial match (substring either way)
        if any(qt in t or t in qt for t in title_tokens):
            score += 5.0 * term_idf

        # Tag exact match
        if qt in tag_tokens:
            score += 8.0 * term_idf
        # Tag partial match
        if any(qt in t or t in qt for t in tag_tokens):
            score += 4.0 * term_idf

        # Category exact match
        if qt in category_tokens:
            score += 6.0 * term_idf

        # Content TF (exact)
        tf = content_tokens.count(qt)
        score += tf * term_idf * 0.1

        # Content partial TF (substring)
        partial_tf = sum(1 for t in content_tokens if qt in t or t in qt)
        score += partial_tf * term_idf * 0.03

    return score


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def search(query: str, top_n: int = 5) -> List[Dict[str, Any]]:
    """Search the knowledge index and return the top-N results.

    Parameters
    ----------
    query : str
        Natural-language search query.
    top_n : int
        Maximum number of results to return.

    Returns
    -------
    list of dict
        Each dict contains ``title``, ``file``, ``dir``, ``url``,
        ``category``, ``difficulty``, ``tags``, ``score``, and a
        content ``snippet``.
    """
    _ensure_loaded()

    query_tokens = tokenize(query)
    if not query_tokens:
        return []

    # Pre-compute all document token lists for IDF
    all_doc_tokens: List[List[str]] = []
    for entry in _index:
        tokens: List[str] = []
        tokens.extend(tokenize(entry.get("title", "")))
        for tag in entry.get("tags", []):
            tokens.extend(tokenize(tag))
        tokens.extend(tokenize(entry.get("category", "")))
        tokens.extend(tokenize(entry.get("content", "")))
        all_doc_tokens.append(tokens)

    scored: List[Tuple[IndexEntry, float]] = []
    for i, entry in enumerate(_index):
        s = _score_document(entry, query_tokens, all_doc_tokens)
        if s > 0:
            scored.append((entry, s))

    scored.sort(key=lambda x: x[1], reverse=True)

    results: List[Dict[str, Any]] = []
    for entry, score in scored[:top_n]:
        snippet = (entry.get("content", "") or "")[:500].strip()
        if len(entry.get("content", "")) > 500:
            snippet += "..."
        results.append(
            {
                "title": entry.get("title", ""),
                "file": entry.get("file", ""),
                "dir": entry.get("dir", ""),
                "url": entry.get("url", ""),
                "category": entry.get("category", ""),
                "difficulty": entry.get("difficulty", ""),
                "tags": entry.get("tags", []),
                "score": round(score, 2),
                "snippet": snippet,
            }
        )
    return results


def get_entry_count() -> int:
    """Return the number of loaded index entries."""
    _ensure_loaded()
    return len(_index)
