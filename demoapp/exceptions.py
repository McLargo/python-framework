ERROR_CODE_1000 = 1000  # uncontrolled error
ERROR_CODE_1001 = 1001  # validation error


class ValidationException(Exception):
    def __init__(self, message):
        self.message = message
        self.error_code = ERROR_CODE_1001
