from src.models import LivenessModel


def test_liveness(client):
    response = client.get("/liveness")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    expected_result = {"backend_liveness": True}
    assert response.json() == expected_result
