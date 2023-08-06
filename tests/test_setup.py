import os


def test_check_test_env():
    assert os.getenv("RUNTIME_ENV") == "test"


def test_database_connection():
    ...
