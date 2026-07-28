import logging
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .api.routes import router
from .ui.routes import router as ui_router

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Setup can go here
    yield
    # Cleanup can go here

app = FastAPI(
    title="VIN Validation API",
    description="API for decoding VIN numbers using the NHTSA vPIC database.",
    version="1.0.0",
    lifespan=lifespan
)

# Mount Static Files
BASE_DIR = Path(__file__).resolve().parent
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")

# Include Routers
app.include_router(ui_router)
app.include_router(router)
