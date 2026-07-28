import asyncio
import logging
from contextlib import asynccontextmanager, suppress
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .api.routes import router
from .config import get_settings
from .scraper.db_updater import check_and_update_db
from .ui.routes import router as ui_router

logger = logging.getLogger(__name__)

async def scheduled_db_update():
    settings = get_settings()
    while True:
        try:
            logger.info("Running scheduled database update check...")
            await check_and_update_db()
        except Exception as e:
            logger.error(f"Error during scheduled database update: {e}")
        
        logger.info(f"Sleeping for {settings.db_update_interval_seconds} seconds until next update check.")
        await asyncio.sleep(settings.db_update_interval_seconds)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Start the background task
    task = asyncio.create_task(scheduled_db_update())
    yield
    # Shutdown: Cancel the task
    task.cancel()
    with suppress(asyncio.CancelledError):
        await task

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
