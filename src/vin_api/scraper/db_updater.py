import httpx
import asyncio
import datetime
import zipfile
import os
import subprocess
import logging

logger = logging.getLogger(__name__)

async def check_and_update_db(
    container_name: str = os.environ.get("POSTGRES_CONTAINER", "vin-api-db-1"),
    db_user: str = os.environ.get("POSTGRES_USER", "vpic"),
    db_name: str = os.environ.get("POSTGRES_DB", "vpic_db")
):
    """
    Checks if a new DB dump is available for the current year/month or recent months.
    If available and not already applied, it downloads and restores it.
    """
    # Look back up to 3 months
    today = datetime.date.today()
    found_url = None
    target_zip = None

    async with httpx.AsyncClient() as client:
        for i in range(3):
            d = today - datetime.timedelta(days=i*30)
            url = f"https://vpic.nhtsa.dot.gov/downloads/vPICList_lite_{d.year}_{d.month:02d}.custom.zip"
            try:
                response = await client.head(url)
                if response.status_code == 200:
                    found_url = url
                    target_zip = f"vPICList_lite_{d.year}_{d.month:02d}.custom.zip"
                    break
            except Exception as e:
                logger.error(f"Error checking {url}: {e}")

    if not found_url:
        logger.info("No recent database dumps found.")
        return

    # We use a simple local file to track the last restored version.
    version_file = ".latest_db_version"
    if os.path.exists(version_file):
        with open(version_file, "r") as f:
            if f.read().strip() == target_zip:
                logger.info(f"Database dump {target_zip} already downloaded and restored. Skipping update.")
                return

    logger.info(f"Downloading new database dump: {found_url}")
    
    # Download
    async with httpx.AsyncClient() as client:
        async with client.stream('GET', found_url) as r:
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
        return

    logger.info(f"Restoring {custom_file} to Postgres...")
    cmd = f"docker exec -i {container_name} pg_restore -U {db_user} -d {db_name} < {custom_file}"
    try:
        subprocess.run(cmd, shell=True, check=False) # pg_restore often returns 1 for non-fatal errors
        logger.info("Database restore complete.")
    except Exception as e:
        logger.error(f"Database restore failed: {e}")

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
