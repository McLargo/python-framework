from flask import Flask

from src.blueprint import register_blueprint
from src.error_handler import register_error_handlers

app = Flask(__name__)

register_error_handlers(app)
register_blueprint(app)
