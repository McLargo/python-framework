from flask import Flask, jsonify, request

from demoapp.decorators import is_json, permission
from demoapp.error_handler import register_error_handlers
from demoapp.schemas import DemoSchema

app = Flask(__name__)

register_error_handlers(app)


class DemoApiV1:
    @app.route("/api/v1/demo", methods=["GET"])
    @permission
    def demo(error=None):
        data = {
            "first_name": "Yuri",
            "last_name": "Gagarin",
            "born": "1934-03-09",
            "died": "1968-3-27",
        }
        validate_data = DemoSchema().load(data)
        return jsonify(data=DemoSchema().dump(validate_data))

    @app.route("/api/v1/demo", methods=["POST"])
    @permission
    @is_json
    def demo_post(error=None):
        validate_data = DemoSchema().load(request.json)
        return jsonify(data=DemoSchema().dump(validate_data))
