from pytest import fixture
import pytest
from dotenv import load_dotenv


@fixture(scope="module", autouse=True)
def setup_env():
    load_dotenv("env/.test.env")
