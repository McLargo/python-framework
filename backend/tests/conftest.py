import pytest

from app import app


@pytest.fixture
def client():
    return app.test_client()


@pytest.fixture
def demo_fixture():
    return {
        "first_name": "Yuri",
        "last_name": "Gagarin",
        "born": "1934-03-09",
        "died": "1968-03-27",
    }


@pytest.fixture
def demo_fixture_expected():
    return {
        "first_name": "Yuri",
        "last_name": "Gagarin",
        "born": "1934-03-09",
        "died": "1968-03-27",
        "age": 34,
        "alive": False,
    }
