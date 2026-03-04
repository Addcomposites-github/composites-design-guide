"""Application configuration using pydantic-settings.

Loads settings from environment variables and a .env file.
REPO_ROOT resolves to two levels above the backend/ directory,
which is the repository root containing knowledge/, data/, and index.json.
"""

from pathlib import Path
from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


# Resolve the repo root: backend/ -> web-app/ -> repo root
_BACKEND_DIR = Path(__file__).resolve().parent.parent  # web-app/backend/
_REPO_ROOT = _BACKEND_DIR.parent.parent  # composites-design-guide repo root


class Settings(BaseSettings):
    """Global application settings.

    Values are loaded from environment variables first, then from a .env
    file in the backend/ directory.
    """

    model_config = SettingsConfigDict(
        env_file=str(_BACKEND_DIR / ".env"),
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # ---- API Keys ----
    ANTHROPIC_API_KEY: Optional[str] = None

    # ---- Claude model ----
    CLAUDE_MODEL: str = "claude-sonnet-4-20250514"

    # ---- Repository paths ----
    REPO_ROOT: Path = _REPO_ROOT
    INDEX_PATH: Path = _REPO_ROOT / "index.json"
    MATERIALS_PATH: Path = _REPO_ROOT / "data" / "materials.json"
    PROCESSES_PATH: Path = _REPO_ROOT / "data" / "processes.json"
    DECISION_TREES_DIR: Path = _REPO_ROOT / "decision-trees"
    KNOWLEDGE_DIR: Path = _REPO_ROOT / "knowledge"

    # ---- Server ----
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DEBUG: bool = False


# Singleton instance for the app to import
settings = Settings()
