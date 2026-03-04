"""Material database service.

Loads materials.json and provides search/lookup methods.
Port of the material search logic from mcp-server/src/index.ts.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

from app.config import settings


# ---------------------------------------------------------------------------
# Module-level state
# ---------------------------------------------------------------------------

_materials: List[Dict[str, Any]] = []
_metadata: Dict[str, Any] = {}
_loaded: bool = False


# ---------------------------------------------------------------------------
# Loading
# ---------------------------------------------------------------------------

def load(materials_path: Optional[Path] = None) -> None:
    """Load (or reload) the materials database from disk.

    Parameters
    ----------
    materials_path : Path, optional
        Override path for materials.json.  Defaults to
        ``settings.MATERIALS_PATH``.
    """
    global _materials, _metadata, _loaded
    path = materials_path or settings.MATERIALS_PATH
    try:
        with open(path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
        _materials = data.get("materials", [])
        _metadata = data.get("_metadata", {})
        _loaded = True
    except Exception as exc:
        print(f"Warning: Could not load materials.json at {path}: {exc}")
        _materials = []
        _metadata = {}
        _loaded = True


def _ensure_loaded() -> None:
    if not _loaded:
        load()


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def search(query: str) -> List[Dict[str, Any]]:
    """Search materials by matching all query tokens against searchable fields.

    Mirrors the TypeScript ``searchMaterials`` function: every whitespace-
    separated token must appear somewhere in the concatenation of id, name,
    category, fibre_type, fibre_grade, resin_family, form, applications,
    and notes.

    If no results are found with an AND-match, falls back to an OR-match
    (any token present) to be more forgiving.

    Parameters
    ----------
    query : str
        Free-text search string.

    Returns
    -------
    list of dict
        Matching material records.
    """
    _ensure_loaded()

    q = query.lower()
    tokens = [t for t in q.split() if t]
    if not tokens:
        return list(_materials)

    def _searchable(m: Dict[str, Any]) -> str:
        parts = [
            m.get("id", ""),
            m.get("name", ""),
            m.get("category", ""),
            m.get("fibre_type", ""),
            m.get("fibre_grade", ""),
            m.get("resin_family", ""),
            m.get("form", ""),
        ]
        parts.extend(m.get("applications", []))
        parts.append(m.get("notes", "") or "")
        return " ".join(parts).lower()

    # AND-match: all tokens present
    results = [m for m in _materials if all(t in _searchable(m) for t in tokens)]
    if results:
        return results

    # Fallback: OR-match (at least one token present)
    results = [m for m in _materials if any(t in _searchable(m) for t in tokens)]
    return results


def get_all() -> List[Dict[str, Any]]:
    """Return every material in the database."""
    _ensure_loaded()
    return list(_materials)


def get_by_id(material_id: str) -> Optional[Dict[str, Any]]:
    """Look up a single material by its ``id`` field.

    Parameters
    ----------
    material_id : str
        The material identifier, e.g. ``"t700-epoxy-ud"``.

    Returns
    -------
    dict or None
        The material record, or ``None`` if not found.
    """
    _ensure_loaded()
    for m in _materials:
        if m.get("id") == material_id:
            return m
    return None


def get_metadata() -> Dict[str, Any]:
    """Return the ``_metadata`` block from materials.json."""
    _ensure_loaded()
    return dict(_metadata)


def get_count() -> int:
    """Return the number of materials loaded."""
    _ensure_loaded()
    return len(_materials)
