from httpx import Response, codes


def test_liveness(client) -> None:
    expected_result: dict = {"backend_liveness": True}

    response: Response = client.get("/liveness")

    assert response.status_code == codes.OK
    assert isinstance(response.json(), dict)
    assert response.json() == expected_result
