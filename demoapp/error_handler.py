from flask import jsonify
from marshmallow.exceptions import ValidationError

from demoapp.logging import Logging

ERROR_CODE_1000 = 1000  # uncontrolled error
ERROR_CODE_1001 = 1001  # validation error
ERROR_CODE_1002 = 1002  # permission error
ERROR_CODE_1003 = 1003  # not found error
ERROR_CODE_1004 = 1004  # not allowed error


class RequestJsonException(Exception):
    pass


def register_error_handlers(app):
    @app.errorhandler(Exception)
    def handle_exception(e):
        message = str(e)
        Logging().log_error(message)
        return jsonify(code=ERROR_CODE_1000, message=message), 500

    @app.errorhandler(403)
    def handle_403_error(e):
        message = "Forbidden error"
        Logging().log_warning(message)
        return jsonify(code=ERROR_CODE_1002, message=message), 403

    @app.errorhandler(404)
    def handle_404_error(e):
        message = "Not found error"
        Logging().log_warning(message)
        return jsonify(code=ERROR_CODE_1003, message=message), 404

    @app.errorhandler(405)
    def handle_405_error(e):
        message = "Method not allowed"
        Logging().log_info(message)
        return jsonify(code=ERROR_CODE_1004, message=message), 405

    @app.errorhandler(ValidationError)
    def handle_validation_error(e):
        message = e.messages
        Logging().log_error(message)
        return (
            jsonify(error_code=ERROR_CODE_1001, error_message=message),
            400,
        )

    @app.errorhandler(RequestJsonException)
    def handle_request_json_error(e):
        message = "Request is not JSON"
        Logging().log_error(message)
        return (
            jsonify(error_code=ERROR_CODE_1001, error_message=message),
            400,
        )
