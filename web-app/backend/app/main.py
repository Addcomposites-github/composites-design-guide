"""OpenComposites API -- FastAPI application entry point.

Creates the FastAPI app with CORS middleware, includes all route modules
under the ``/api`` prefix, loads data stores on startup, and optionally
serves the built frontend as a single-page application in production.

Run locally with::

    uvicorn app.main:app --reload --port 8000

from the ``web-app/backend/`` directory.
"""

from __future__ import annotations

import logging
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Any, AsyncGenerator, Dict

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.config import settings
from app.routes import analysis, bolted_joint, clt, cost, knowledge, materials, processes, sandwich
from app.services import knowledge_service, material_service, process_service

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Lifespan -- load data stores at startup
# ---------------------------------------------------------------------------


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Application lifespan handler.

    Loads the knowledge index, materials database, and processes database
    into memory when the server starts up, and performs cleanup on shutdown.
    """
    logger.info("Loading data stores...")

    knowledge_service.load()
    material_service.load()
    process_service.load()

    logger.info(
        "Data loaded: %d knowledge entries, %d materials, %d processes",
        knowledge_service.get_entry_count(),
        material_service.get_count(),
        process_service.get_count(),
    )

    yield  # Server is running

    logger.info("Shutting down OpenComposites API.")


# ---------------------------------------------------------------------------
# Create FastAPI application
# ---------------------------------------------------------------------------

app = FastAPI(
    title="OpenComposites API",
    description=(
        "Backend API for OpenComposites by Addcomposites.  "
        "Powers the Photo-to-Plan composites AI agent, knowledge-base "
        "search, material lookup, process recommendation, stacking rule "
        "checks, CLT analysis, sandwich panel design, and bolted joint analysis."
    ),
    version="1.0.0",
    lifespan=lifespan,
)

# ---------------------------------------------------------------------------
# CORS -- allow the frontend dev servers
# ---------------------------------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:5173",
        "http://localhost:5174",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:5174",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------------------------------
# Include routers
# ---------------------------------------------------------------------------

app.include_router(analysis.router, prefix="/api")
app.include_router(materials.router, prefix="/api")
app.include_router(processes.router, prefix="/api")
app.include_router(cost.router, prefix="/api")
app.include_router(knowledge.router, prefix="/api")
app.include_router(sandwich.router, prefix="/api")
app.include_router(clt.router, prefix="/api")
app.include_router(bolted_joint.router, prefix="/api")

# ---------------------------------------------------------------------------
# Health check
# ---------------------------------------------------------------------------


@app.get(
    "/api/health",
    summary="Health check",
    description="Returns server status and version information.",
)
async def healthcheck() -> Dict[str, Any]:
    """Health endpoint -- confirms the server is running."""
    return {
        "status": "ok",
        "service": "OpenComposites API",
        "version": "1.0.0",
        "data": {
            "knowledge_entries": knowledge_service.get_entry_count(),
            "materials": material_service.get_count(),
            "processes": process_service.get_count(),
        },
    }


# ---------------------------------------------------------------------------
# Serve the built frontend (production SPA)
# ---------------------------------------------------------------------------

_FRONTEND_DIST = Path(__file__).resolve().parent.parent.parent / "frontend" / "dist"

if _FRONTEND_DIST.is_dir():
    # Serve Vite-built assets (JS, CSS, images)
    _ASSETS_DIR = _FRONTEND_DIST / "assets"
    if _ASSETS_DIR.is_dir():
        app.mount(
            "/assets",
            StaticFiles(directory=str(_ASSETS_DIR)),
            name="static-assets",
        )

    @app.get("/{full_path:path}")
    async def serve_spa(full_path: str) -> FileResponse:
        """Catch-all: serve static files or fall back to index.html for SPA routing."""
        file_path = _FRONTEND_DIST / full_path
        if full_path and file_path.is_file():
            return FileResponse(str(file_path))
        return FileResponse(str(_FRONTEND_DIST / "index.html"))
