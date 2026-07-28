# Scraper Constants
NHTSA_VPIC_BASE_URL = "https://vpic.nhtsa.dot.gov/downloads"
NHTSA_DUMP_FILENAME_TEMPLATE = "vPICList_lite_{year}_{month:02d}.custom.zip"
VERSION_TRACKER_FILE = ".latest_db_version"
DB_UPDATE_INTERVAL_SECONDS = 86400

# Database defaults
DEFAULT_POSTGRES_CONTAINER = "vin-api-db-1"
DEFAULT_POSTGRES_USER = "vpic"
DEFAULT_POSTGRES_DB = "vpic_db"

# API & UI Constants
SP_VIN_DECODE_COLUMNS = ["variable", "value", "code", "datatype", "groupname"]
