import asyncio
import datetime
import logging
import os
import subprocess
import sys
import zipfile

import httpx

from ..config import get_settings
from ..constants import (
    NHTSA_DUMP_FILENAME_TEMPLATE,
    NHTSA_VPIC_BASE_URL,
    VERSION_TRACKER_FILE,
)

logger = logging.getLogger(__name__)

async def check_and_update_db():
    """
    Checks if a new DB dump is available for the current year/month or recent months.
    If available and not already applied, it downloads and restores it.
    """
    settings = get_settings()
    # Look back up to 3 months
    today = datetime.date.today()
    found_url = None
    target_zip = None

    async with httpx.AsyncClient() as client:
        for i in range(3):
            d = today - datetime.timedelta(days=i*30)
            filename = NHTSA_DUMP_FILENAME_TEMPLATE.format(year=d.year, month=d.month)
            url = f"{NHTSA_VPIC_BASE_URL}/{filename}"
            try:
                response = await client.head(url)
                if response.status_code == 200:
                    found_url = url
                    target_zip = filename
                    break
            except Exception as e:
                logger.error(f"Error checking {url}: {e}")

    if not found_url or not target_zip:
        logger.info("No recent database dumps found.")
        # If no DB dumps found, we must verify the DB is already populated, otherwise we cannot proceed!
        verify_cmd = [
            "psql",
            "-h", settings.postgres_host,
            "-p", str(settings.postgres_port),
            "-U", settings.postgres_user,
            "-d", settings.postgres_db,
            "-tAc", "SELECT 1 FROM information_schema.schemata WHERE schema_name = 'vpic'"
        ]
        env = os.environ.copy()
        if hasattr(settings, 'postgres_password') and settings.postgres_password:
            env['PGPASSWORD'] = settings.postgres_password
        
        res = subprocess.run(verify_cmd, env=env, capture_output=True, text=True)
        if "1" not in res.stdout:
            logger.error("FATAL: No database dumps found online and the local database is completely empty. The API cannot function.")
            sys.exit(1)
        return

    # We use a simple local file to track the last restored version.
    version_file = VERSION_TRACKER_FILE
    if os.path.exists(version_file):
        with open(version_file) as f:
            if f.read().strip() == target_zip:
                logger.info(f"Database dump {target_zip} already downloaded and restored. Skipping update.")
                return

    logger.info(f"Downloading new database dump: {found_url}")
    
    # Download
    async with httpx.AsyncClient() as client, client.stream('GET', found_url) as r:
        with open(target_zip, 'wb') as f:
            async for chunk in r.aiter_bytes():
                f.write(chunk)

    logger.info("Extracting...")
    dump_dir = f"dump_{target_zip}"
    os.makedirs(dump_dir, exist_ok=True)
    with zipfile.ZipFile(target_zip, 'r') as zip_ref:
        zip_ref.extractall(dump_dir)

    # Find the .backup or .custom file
    custom_file = None
    for f in os.listdir(dump_dir):
        if f.endswith(".backup") or f.endswith(".custom"):
            custom_file = os.path.join(dump_dir, f)
            break

    if not custom_file:
        logger.error("Could not find restore file in zip.")
        sys.exit(1)

    logger.info(f"Restoring {custom_file} to Postgres...")
    
    env = os.environ.copy()
    if hasattr(settings, 'postgres_password') and settings.postgres_password:
        env['PGPASSWORD'] = settings.postgres_password

    cmd = [
        "pg_restore",
        "-h", settings.postgres_host,
        "-p", str(settings.postgres_port),
        "-U", settings.postgres_user,
        "-d", settings.postgres_db,
        "-1",
        "--no-owner",
        "--no-privileges",
        custom_file
    ]

    try:
        subprocess.run(cmd, env=env, check=False) # pg_restore often returns 1 for non-fatal errors
        logger.info("Database restore command finished executing.")
    except Exception as e:
        logger.error(f"Database restore failed to execute: {e}")
        sys.exit(1)

    # Verify restore was successful
    verify_cmd = [
        "psql",
        "-h", settings.postgres_host,
        "-p", str(settings.postgres_port),
        "-U", settings.postgres_user,
        "-d", settings.postgres_db,
        "-tAc", "SELECT 1 FROM information_schema.schemata WHERE schema_name = 'vpic'"
    ]
    result = subprocess.run(verify_cmd, env=env, capture_output=True, text=True)
    if "1" not in result.stdout:
        logger.error("FATAL: Restore verification failed! Schema 'vpic' was not created.")
        sys.exit(1)
    
    logger.info("Database restore verified successfully.")

    # Cleanup
    os.remove(target_zip)
    for f in os.listdir(dump_dir):
        os.remove(os.path.join(dump_dir, f))
    os.rmdir(dump_dir)

    # Save version
    with open(version_file, "w") as f:
        f.write(target_zip)

    logger.info("Cleanup complete.")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(check_and_update_db())
