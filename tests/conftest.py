import pytest
from fastapi.testclient import TestClient

from vin_api.config import get_settings
from vin_api.main import app

@pytest.fixture(scope="session")
def client():
    """Provides a TestClient for FastAPI"""
    with TestClient(app) as client:
        yield client

@pytest.fixture(scope="session")
def settings():
    """Provides application settings"""
    return get_settings()
