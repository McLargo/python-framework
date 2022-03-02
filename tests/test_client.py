import pytest

from src.error_handler import (
    ERROR_CODE_1000,
    ERROR_CODE_1001,
    ERROR_CODE_1002,
    ERROR_CODE_1003,
    ERROR_CODE_1004,
)


def test_500_error(client):
    response = client.get("/api/v1/demo", headers={"raise_error": True})
    assert response.status_code == 500
    assert response.json["code"] == ERROR_CODE_1000
    assert response.json["message"] == "Uncontrolled exception"


def test_403_error(client):
    response = client.get("/api/v1/demo", headers={"block_request": True})
    assert response.status_code == 403
    assert response.json["code"] == ERROR_CODE_1002
    assert response.json["message"] == "Forbidden error"


def test_403_error_post(client):
    response = client.post("/api/v1/demo", headers={"block_request": True})
    assert response.status_code == 403
    assert response.json["code"] == ERROR_CODE_1002
    assert response.json["message"] == "Forbidden error"


def test_404_error(client):
    response = client.get("/api/v1/missing")
    assert response.status_code == 404
    assert response.json["code"] == ERROR_CODE_1003
    assert response.json["message"] == "Not found error"


def test_405_error(client):
    response = client.delete("/api/v1/demo")
    assert response.status_code == 405
    assert response.json["code"] == ERROR_CODE_1004
    assert response.json["message"] == "Method not allowed"


def test_post_demo_not_json(client):
    response = client.post("/api/v1/demo")
    assert response.status_code == 400
    assert isinstance(response.json, dict)
    expected_result = {
        "error_code": ERROR_CODE_1001,
        "error_message": "Request is not JSON",
    }
    assert response.json == expected_result


def test_get_demo(client, demo_fixture_expected):
    response = client.get("/api/v1/demo")
    assert response.status_code == 200
    assert isinstance(response.json, dict)
    assert response.json["data"] == demo_fixture_expected


def test_post_demo(client, demo_fixture, demo_fixture_expected):
    response = client.post("/api/v1/demo", json=demo_fixture)
    assert response.status_code == 200
    assert isinstance(response.json, dict)
    assert response.json["data"] == demo_fixture_expected


@pytest.mark.freeze_time("2022-03-02")
def test_post_demo_died_missing(client, demo_fixture, demo_fixture_expected):
    demo_fixture.pop("died")
    response = client.post("/api/v1/demo", json=demo_fixture)
    assert response.status_code == 200
    assert isinstance(response.json, dict)
    demo_fixture_expected["died"] = None
    demo_fixture_expected["age"] = 87
    demo_fixture_expected["alive"] = True
    assert response.json["data"] == demo_fixture_expected


@pytest.mark.freeze_time("2022-03-02")
def test_post_demo_died_is_none(client, demo_fixture, demo_fixture_expected):
    demo_fixture["died"] = None
    response = client.post("/api/v1/demo", json=demo_fixture)
    assert response.status_code == 200
    assert isinstance(response.json, dict)
    demo_fixture_expected["died"] = None
    demo_fixture_expected["age"] = 87
    demo_fixture_expected["alive"] = True
    assert response.json["data"] == demo_fixture_expected


def test_post_demo_missing_required_first_name(client, demo_fixture):
    demo_fixture.pop("first_name")
    response = client.post("/api/v1/demo", json=demo_fixture)
    assert response.status_code == 400
    assert isinstance(response.json, dict)
    expected_result = {
        "error_code": ERROR_CODE_1001,
        "error_message": {"first_name": ["Missing data for required field."]},
    }
    assert response.json == expected_result


def test_post_demo_missing_required_last_name(client, demo_fixture):
    demo_fixture.pop("last_name")
    response = client.post("/api/v1/demo", json=demo_fixture)
    assert response.status_code == 400
    assert isinstance(response.json, dict)
    expected_result = {
        "error_code": ERROR_CODE_1001,
        "error_message": {"last_name": ["Missing data for required field."]},
    }
    assert response.json == expected_result


def test_post_demo_missing_required_born(client, demo_fixture):
    demo_fixture.pop("born")
    response = client.post("/api/v1/demo", json=demo_fixture)
    assert response.status_code == 400
    assert isinstance(response.json, dict)
    expected_result = {
        "error_code": ERROR_CODE_1001,
        "error_message": {"born": ["Missing data for required field."]},
    }
    assert response.json == expected_result
