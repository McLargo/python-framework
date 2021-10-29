import pytest

from app import app

from demoapp.exceptions import ERROR_CODE_1001
from demoapp.serializers import DemoSerializer


@pytest.fixture
def client():
    return app.test_client()


def test_demo(client):
    resp = client.get("/api/v1/demo")
    assert resp.status_code == 200
    assert isinstance(resp.json, dict)
    assert resp.json == DemoSerializer().response()


def test_missing_route(client):
    resp = client.get("/api/v1/missing")
    assert resp.status_code == 404
    assert resp.json is None


def test_demopost(client):
    json_data = {
        "first_name": "Miroslav",
        "middle_name": "Josef",
        "last_name": "Klose",
        "dob": "09-06-1978",
    }
    resp = client.post("/api/v1/demo", json=json_data)
    assert resp.status_code == 200
    assert isinstance(resp.json, dict)
    expected_result = {
        "full_name": "Miroslav Josef Klose",
        "age": 43,
        "is_alive": True,

    }
    assert resp.json == expected_result


def test_demopost_invalid_keys(client):
    json_data = {
        "first_name": "Miroslav",
        "middle_name": "Josef",
        "last_name": "Klose",
    }
    resp = client.post("/api/v1/demo", json=json_data)
    assert resp.status_code == 400
    assert isinstance(resp.json, dict)
    expected_result = {
        "error_code": ERROR_CODE_1001,
        "error_message": "Validation: 'dob' is a required property",
    }
    assert resp.json == expected_result
