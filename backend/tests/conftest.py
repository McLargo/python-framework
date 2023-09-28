import pytest

from faker import Faker

from fastapi.testclient import TestClient

from main import app


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


@pytest.fixture
def faker() -> Faker:
    return Faker()
