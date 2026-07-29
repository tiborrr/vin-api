# VIN API

A fast and highly reliable API to validate and decode Vehicle Identification Numbers (VINs) using the official NHTSA vPIC PostgreSQL database.

This project features a blazing-fast FastAPI backend, bulk validation endpoints, and a lightweight HTMX frontend. It automatically downloads, extracts, and restores the latest vPIC database dump into a Dockerized PostgreSQL instance.

[![Docker Image Version (latest by date)](https://img.shields.io/docker/v/tiborrr/vpic-api-service)](https://hub.docker.com/r/tiborrr/vpic-api-service)

## Features

- **True DB Validation**: Connects to an actual PostgreSQL instance running the native NHTSA database structure for 100% accuracy.
- **Auto-Initialization**: Docker compose handles scraping NHTSA for the latest database dumps and gracefully restores them on startup.
- **Fast Endpoints**: Provides a simple validation and a high-performance bulk endpoint leveraging PostgreSQL `UNNEST` and native scalar functions.
- **Rich Endpoints**: Provides a complex decode endpoint using the `vpic.spvindecode` stored procedure.
- **HTMX Frontend**: Includes a sleek, modern UI for decoding VINs right from your browser.
- **Docker Hub Images**: Ready-to-use Docker images published automatically on releases.

## Requirements

- Docker & Docker Compose

## Quick Start (Docker Compose)

The easiest way to run the service is using Docker Compose. This automatically spins up the database, initializes the NHTSA schema, and launches the API.

### 1. Environment Configuration
Copy the example environment file and customize it if needed (defaults are fine for local testing).
```bash
cp .env.example .env
```

### 2. Start the Stack
Bring up the entire stack in detached mode:
```bash
docker compose up -d
```

**What happens?**
1. The `db` container (PostgreSQL) starts.
2. The `db-init` container waits for the database, downloads the latest vPIC dump, and seeds the schema. *(Note: This can take a few minutes as the database is large).*
3. The `api` container waits for `db-init` to finish, then starts the FastAPI web server.

### 3. Access the Service
- **Web UI:** [http://localhost:8000/](http://localhost:8000/)
- **Swagger Documentation:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Using the Docker Hub Image

If you want to pull the pre-built image directly from Docker Hub rather than building it locally, you can use:
```bash
docker pull tiborrr/vpic-api-service:latest
```
*(This is ideal for production deployments or CI environments)*.

## API Endpoints

- **Simple Validation**: `GET /api/v1/vin/{vin}/simple`
  Fast endpoint for basic validation, year, and WMI extraction.
- **Bulk Validation**: `POST /api/v1/vin/bulk-simple`
  High-performance endpoint that validates up to 100 VINs concurrently.
- **Complex Decode**: `GET /api/v1/vin/{vin}/decode`
  Returns all the rich detailed attributes for the provided VIN.

## Testing

This project includes automated tests that run in an isolated Docker container against the real PostgreSQL schema to ensure flawless execution.

To run the test suite:
```bash
docker compose run --build --rm test
```
