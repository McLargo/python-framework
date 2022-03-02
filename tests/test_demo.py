from demoapp.exceptions import ERROR_CODE_1000, ERROR_CODE_1001
from demoapp.serializers import DemoSerializer


def test_demo(client):
    response = client.get("/api/v1/demo")
    assert response.status_code == 200
    assert isinstance(response.json, dict)
    assert response.json["data"] == DemoSerializer().response()


def test_missing_route(client):
    response = client.get("/api/v1/missing")
    assert response.status_code == 404
    assert response.json is None


def test_demopost(client):
    json_data = {
        "first_name": "Miroslav",
        "middle_name": "Josef",
        "last_name": "Klose",
        "dob": "09-06-1978",
    }
    response = client.post("/api/v1/demo", json=json_data)
    assert response.status_code == 200
    assert isinstance(response.json, dict)
    expected_result = {
        "full_name": "Miroslav Josef Klose",
        "age": 43,
        "is_alive": True,
    }
    assert response.json["data"] == expected_result


def test_demopost_invalid_keys(client):
    json_data = {
        "first_name": "Miroslav",
        "middle_name": "Josef",
        "last_name": "Klose",
    }
    response = client.post("/api/v1/demo", json=json_data)
    assert response.status_code == 400
    assert isinstance(response.json, dict)
    expected_result = {
        "error_code": ERROR_CODE_1001,
        "error_message": "Validation: 'dob' is a required property",
    }
    assert response.json == expected_result


def test_demopost_without_middle_name(client):
    json_data = {
        "first_name": "Miroslav",
        "last_name": "Klose",
        "dob": "09-06-1978",
    }
    response = client.post("/api/v1/demo", json=json_data)
    assert response.status_code == 200
    assert isinstance(response.json, dict)
    expected_result = {
        "full_name": "Miroslav Klose",
        "age": 43,
        "is_alive": True,
    }
    assert response.json["data"] == expected_result


def test_demopost_ugly_exception(client):
    json_data = {
        "first_name": "Miroslav",
        "last_name": "Klose",
        "dob": "67-06-1978",
    }
    response = client.post("/api/v1/demo", json=json_data)
    assert response.status_code == 400
    assert isinstance(response.json, dict)
    expected_result = {
        "error_code": ERROR_CODE_1000,
        "error_message": "time data '67-06-1978' does not match format '%d-%m-%Y'",
    }
    assert response.json == expected_result


def test_demopost_not_json(client):
    response = client.post("/api/v1/demo")
    assert response.status_code == 400
    assert isinstance(response.json, dict)
    expected_result = {
        "error_code": ERROR_CODE_1001,
        "error_message": "Request is not JSON",
    }
    assert response.json == expected_result
