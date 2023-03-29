from conftest import config_test_db, config_db
from tasks_manager.db.config import get_config, get_connection_dsn


def test_get_config(config_db):
    assert get_config() == config_db


def test_get_connection_dsn(config_test_db):
    assert get_connection_dsn(config_test_db) == (
        f"postgresql://{config_test_db['POSTGRES_USER']}:{config_test_db['POSTGRES_PASSWORD']}@"
        f"{config_test_db['POSTGRES_HOST']}:{config_test_db['POSTGRES_PORT']}/{config_test_db['POSTGRES_DBNAME']}"
    )
