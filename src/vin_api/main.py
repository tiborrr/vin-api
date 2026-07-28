import logging
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .api.routes import router
from .config import get_settings
from .database.database import get_engine
from .ui.routes import router as ui_router

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Setup: Verify database is populated
    logger.info("Verifying database integrity...")
    engine = get_engine(get_settings())
    async with engine.connect() as conn:
        has_schema = await conn.run_sync(lambda sync_conn: sync_conn.dialect.has_schema(sync_conn, "vpic"))
        if not has_schema:
            logger.error("CRITICAL: The 'vpic' schema does not exist in the database! The database must be populated using the NHTSA dump before the API can start.")
            raise RuntimeError("Database not populated. Missing 'vpic' schema.")
    logger.info("Database verification successful.")
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
