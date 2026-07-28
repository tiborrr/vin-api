# VIN API

A fast and highly reliable API to validate and decode Vehicle Identification Numbers (VINs) using the official NHTSA vPIC PostgreSQL database.

This project uses FastAPI for the endpoints and automatically downloads, extracts, and restores the latest vPIC database dump into a Dockerized PostgreSQL instance. 

## Features

- **True DB Validation**: Connects to an actual PostgreSQL instance running the NHTSA database structure for 100% accuracy.
- **Auto-Updater**: Runs a continuous background task during the API's lifetime to scrape NHTSA for new monthly database dumps, downloading and restoring them automatically.
- **Fast Endpoints**: Provides a simple/fast endpoint using native Postgres scalar functions.
- **Rich Endpoints**: Provides a complex decode endpoint using the `vpic.spvindecode` function.
- **Fully Automated Setup**: `docker-compose` and a setup script handle the heavy lifting.

## Requirements

- Python 3.14+
- [uv](https://github.com/astral-sh/uv) (for blazing fast dependency management)
- Docker & Docker Compose (for the PostgreSQL database)

## Quick Start

### 1. Environment Configuration
Copy the example environment file and customize it if needed (defaults are fine for local testing).
```bash
cp .env.example .env
```

### 2. Start the Database
The API requires the PostgreSQL database. Start the Docker container:
```bash
docker compose up -d
```
*(Note: The database is mapped to port 5433 to avoid conflicts with any local Postgres instances you might have running).*

### 2. Initial Setup
Run the database updater script. This script automatically checks the NHTSA website for the latest monthly database dump, downloads it, and restores it into your running Docker instance. This will take a few minutes as the database is quite large.
```bash
uv run python src/vin_api/scraper/db_updater.py
```

### 3. Start the API
Start the FastAPI server. 
```bash
uv run uvicorn vin_api.main:app --app-dir src --port 8000
```
Upon startup, the API will also launch a background scheduler that automatically checks for database updates once every 24 hours.

## API Documentation

Once the server is running, interactive API documentation is available at:
- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

### Endpoints

- **Simple Validation**: `GET /api/v1/vin/{vin}/simple`
  Fast endpoint for basic validation and year/WMI extraction.
- **Complex Decode**: `GET /api/v1/vin/{vin}/decode`
  Returns all the rich detailed attributes for the provided VIN.

## Testing

This project includes automated tests that run against the real PostgreSQL container. 

To run the tests:
```bash
uv run pytest
```
