from flask import request

from functools import wraps


def is_json(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not request.is_json:
            return {'success': False}, 400
        return f(*args, **kwargs)
    return wrapper
