from flask import Flask, request

from demoapp.decorators import is_json, validate_json
from demoapp.deserializers import DemoDeserializer
from demoapp.serializers import DemoSerializer


app = Flask(__name__)


class DemoApiV1:
    @app.route("/api/v1/demo", methods=['GET'])
    def demo():
        return DemoSerializer().response()

    @app.route("/api/v1/demo", methods=['POST'])
    @is_json
    @validate_json
    def demopost():
        instance = DemoDeserializer.deserializer(data=request.json)
        return DemoSerializer().response(instance=instance)
