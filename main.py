from flask import Flask, jsonify, request

from demoapp.decorators import is_json
from demoapp.deserializers import DemoDeserializer
from demoapp.exceptions import ERROR_CODE_1000, ValidationException
from demoapp.schemas import schema_request
from demoapp.serializers import DemoSerializer
from demoapp.validators import validate_schema

app = Flask(__name__)


class DemoApiV1:
    @app.route("/api/v1/demo", methods=["GET"])
    def demo(error=None):
        return jsonify(data=DemoSerializer().response())

    @app.route("/api/v1/demo", methods=["POST"])
    @is_json
    def demopost(error=None):
        try:
            validate_schema(schema=schema_request, data=request.json)
            data = DemoDeserializer.deserializer(request.json)
            return jsonify(data=DemoSerializer().response(instance=data))
        except ValidationException as e:
            return (
                jsonify(error_message=e.message, error_code=e.error_code),
                400,
            )
        except Exception as e:
            return (
                jsonify(error_message=str(e), error_code=ERROR_CODE_1000),
                400,
            )
