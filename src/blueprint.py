from flask import Blueprint, jsonify, request

from src.decorators import is_json, permission
from src.schemas import DemoSchema

demo_blueprint = Blueprint("Demo", __name__, url_prefix="/api/v1")


@demo_blueprint.route("/demo", methods=["GET"])
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


@demo_blueprint.route("/demo", methods=["POST"])
@permission
@is_json
def demo_post(error=None):
    validate_data = DemoSchema().load(request.json)
    return jsonify(data=DemoSchema().dump(validate_data))


def register_blueprint(app):
    app.register_blueprint(demo_blueprint)
