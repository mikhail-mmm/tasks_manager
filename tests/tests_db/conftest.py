import pytest


@pytest.fixture
def config_db():
    return {
        "POSTGRES_DBNAME": "tasks",
        "POSTGRES_HOST": "0.0.0.0",
        "POSTGRES_PORT": 5432,
        "POSTGRES_USER": "username",
        "POSTGRES_PASSWORD": "123123",
    }


@pytest.fixture
def config_test_db():
    return {
        "POSTGRES_DBNAME": "tasks_test",
        "POSTGRES_HOST": "0.0.0.0",
        "POSTGRES_PORT": 5432,
        "POSTGRES_USER": "username",
        "POSTGRES_PASSWORD": "123123",
    }
