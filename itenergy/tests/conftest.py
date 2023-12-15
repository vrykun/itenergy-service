import pytest
from alembic import command
from alembic.config import Config
from fastapi.testclient import TestClient

from itenergy.app import app
from itenergy.db.engine import get_db_url

config = Config('alembic.ini')
connect_str = get_db_url()


@pytest.fixture(scope='session')
def test_client() -> TestClient:
    return TestClient(app)


@pytest.fixture(scope='session', autouse=True)
def database() -> None:
    config.set_main_option('sqlalchemy.url', connect_str)
    command.upgrade(config, 'head')
