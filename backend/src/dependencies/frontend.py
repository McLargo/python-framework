from httpx import Client, Response, codes

from . import HttpClient


class Frontend(HttpClient):
    def __init__(self) -> None:
        super().__init__()
        self._client = Client()
        self._base_url = "http://frontend:8999"

    def liveness(self) -> bool:
        response: Response = self._client.get(url=self._base_url)
        return response.status_code == codes.OK
