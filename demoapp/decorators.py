from flask import request

from functools import wraps


def is_json(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not request.is_json:
            return {'success': False}, 400
        return f(*args, **kwargs)
    return wrapper


def validate_json(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        # TODO: bigger validation
        # TODO: custom validation per body not in here, but in POST
        if not all([key in request.json.keys() for key in ['first_name', 'last_name', 'dob']]):
            return {'success': False, 'message': 'Missing key'}, 400
        return f(*args, **kwargs)
    return wrapper
