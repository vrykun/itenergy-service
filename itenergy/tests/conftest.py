import pytest
from fastapi.testclient import TestClient

from itenergy.app import app


@pytest.fixture(scope='session')
def test_client() -> TestClient:
    return TestClient(app)
