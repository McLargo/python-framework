from functools import wraps

from flask import jsonify, request

from demoapp.exceptions import ERROR_CODE_1001


def is_json(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not request.is_json:
            return (
                jsonify(
                    error_code=ERROR_CODE_1001,
                    error_message="Request is not JSON",
                ),
                400,
            )
        return f(*args, **kwargs)

    return wrapper
