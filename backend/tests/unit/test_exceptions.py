from faker import Faker

from src.exceptions import SAMPLE_ERROR, APIError, SampleError


def test_api_error(faker: Faker) -> None:
    status: int = faker.random_int()
    message: str = faker.sentence()

    error: APIError = APIError(status=status, message=message)

    assert error.error_code == status
    assert error.error_message == message


def test_sample_error() -> None:
    error: SampleError = SampleError()

    assert error.error_code == SAMPLE_ERROR
    assert error.error_message == "Message for this sample exception."
