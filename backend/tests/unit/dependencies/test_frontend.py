from unittest.mock import patch

from httpx import Client, codes

from src.dependencies.frontend import Frontend


def test_frontend() -> None:
    frontend_client: Frontend = Frontend()
    assert isinstance(frontend_client._client, Client)
    assert isinstance(frontend_client._base_url, str)
    assert frontend_client._base_url == "http://frontend:8999"


@patch("httpx.Client.get")
def test_frontend_liveness_ok(mock_get) -> None:
    mock_get.return_value.status_code = codes.OK
    frontend_client: Frontend = Frontend()
    assert frontend_client.liveness() is True


@patch("httpx.Client.get")
def test_frontend_liveness_ko(mock_get) -> None:
    mock_get.return_value.status_code = codes.NOT_FOUND
    frontend_client: Frontend = Frontend()
    assert frontend_client.liveness() is False
