from unittest.mock import ANY, Mock

from faker import Faker

from src.logger import Logger


def test_logging_init() -> None:
    logger_empty_name: Logger = Logger()
    assert logger_empty_name._date_format == "%Y-%m-%d %H:%M:%S"
    assert logger_empty_name._log_format == "%(asctime)s: %(message)s"
    assert logger_empty_name._logger.name == "src.logger"

    logger: Logger = Logger("test.test_logging")
    assert logger._date_format == "%Y-%m-%d %H:%M:%S"
    assert logger._log_format == "%(asctime)s: %(message)s"
    assert logger._logger.name == "test.test_logging"


def test_logging_methods(faker: Faker) -> None:
    logger: Logger = Logger()
    logger._logger = Mock()

    words: list[str] = faker.words(nb=2)

    logger.log_info("Info message")
    logger.log_warning("Warning message", words[0])
    logger.log_error("Error message", words[0], words[1])

    assert logger._logger.debug.call_count == 0

    assert logger._logger.info.call_count == 1
    logger._logger.info.assert_called_once_with("Info message")

    assert logger._logger.warning.call_count == 1
    logger._logger.warning.assert_called_once_with("Warning message", ANY)

    assert logger._logger.error.call_count == 1
    logger._logger.error.assert_called_once_with("Error message", ANY, ANY)
