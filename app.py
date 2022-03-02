from flask import Flask

from demoapp.blueprint import register_blueprint
from demoapp.error_handler import register_error_handlers

app = Flask(__name__)

register_error_handlers(app)
register_blueprint(app)
