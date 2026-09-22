from unittest.mock import patch

import pytest
from httpx import Client, codes

from src.dependencies.frontend import Frontend


@pytest.mark.unit
def test_frontend() -> None:
    frontend_client: Frontend = Frontend()
    assert isinstance(frontend_client._client, Client)
    assert isinstance(frontend_client._base_url, str)
    assert frontend_client._base_url == "http://frontend:8999"


@pytest.mark.unit
@pytest.mark.parametrize(
    ("status_code", "expected_liveness"),
    [(codes.OK, True), (codes.NOT_FOUND, False)],
)
@patch("httpx.Client.get")
def test_frontend_liveness(
    mock_get,
    status_code: int,
    expected_liveness: bool,
) -> None:
    mock_get.return_value.status_code = status_code
    frontend_client: Frontend = Frontend()
    assert frontend_client.liveness() is expected_liveness
