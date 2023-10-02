import logging


class Logger:
    def __init__(self, name: str = __name__):
        # set logging format and config
        self._log_format = "%(asctime)s: %(message)s"
        self._date_format = "%Y-%m-%d %H:%M:%S"
        logging.basicConfig(
            format=self._log_format,
            level=logging.INFO,
            datefmt=self._date_format,
        )
        self._logger = logging.getLogger(name)

    def log_info(self, message: str, *args) -> None:
        self._logger.info(message, *args)

    def log_warning(self, message: str, *args) -> None:
        self._logger.warning(message, *args)

    def log_error(self, message: str, *args) -> None:
        self._logger.error(message, *args)
