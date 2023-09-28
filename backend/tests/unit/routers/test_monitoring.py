from httpx import Response
from src.models import LivenessModel


def test_liveness(client) -> None:
    expected_result: dict = {"backend_liveness": True}

    response: Response = client.get("/liveness")

    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert response.json() == expected_result
