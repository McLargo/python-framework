SAMPLE_ERROR: int = 1000


class APIError(Exception):
    def __init__(self, status: int, message: str) -> None:
        self.error_code: int = status
        self.error_message: str = message


class SampleError(APIError):
    def __init__(self) -> None:
        super().__init__(
            status=SAMPLE_ERROR,
            message="Message for this sample exception.",
        )
