from functools import wraps

from flask import abort, request

from demoapp.error_handler import RequestJsonException


def is_json(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not request.is_json:
            raise RequestJsonException
        return f(*args, **kwargs)

    return wrapper


def permission(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if "block_request" in request.headers:
            abort(403)
        if "raise_error" in request.headers:
            raise Exception("Uncontrolled exception")
        return f(*args, **kwargs)

    return wrapper
