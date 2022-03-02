from flask import jsonify
from marshmallow.exceptions import ValidationError

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
        return jsonify(code=ERROR_CODE_1000, message=str(e)), 500

    @app.errorhandler(403)
    def handle_403_error(e):
        return jsonify(code=ERROR_CODE_1002, message="Forbidden error"), 403

    @app.errorhandler(404)
    def handle_404_error(e):
        return jsonify(code=ERROR_CODE_1003, message="Not found error"), 404

    @app.errorhandler(405)
    def handle_405_error(e):
        return jsonify(code=ERROR_CODE_1004, message="Method not allowed"), 405

    @app.errorhandler(ValidationError)
    def handle_validation_error(e):
        return (
            jsonify(error_code=ERROR_CODE_1001, error_message=e.messages),
            400,
        )

    @app.errorhandler(RequestJsonException)
    def handle_request_json_error(e):
        return (
            jsonify(
                error_code=ERROR_CODE_1001, error_message="Request is not JSON"
            ),
            400,
        )
