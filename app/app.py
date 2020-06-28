from flask import Flask
from app.controller import api
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app, resources='/*')
    api.init_app(app)
    return app
