import pytest
from _pytest import monkeypatch
from fastapi.testclient import TestClient

from itenergy.app import app


@pytest.fixture(scope='session')
def test_client() -> TestClient:
    # mp = monkeypatch.MonkeyPatch()
    # mp.setenv('PGHOST', 'localhost')
    # mp.setenv('PGPORT', '5433')
    return TestClient(app)
