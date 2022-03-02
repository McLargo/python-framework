from flask import request

from functools import wraps
from demoapp.exceptions import ERROR_CODE_1001


def is_json(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not request.is_json:
            return {
                "error_code": ERROR_CODE_1001,
                "error_message": "Request is not JSON"}, 400
        return f(*args, **kwargs)
    return wrapper
