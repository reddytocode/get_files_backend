from flask import Flask
from flask_restful import Api


def create_app():
    """crear instancia de Flask app"""
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    return app


def init_api(app):
    from .resource.ResgisterFaceImage import RegisterFaceImage
    from .resource.ResgisterCI_Image import RegisterCiImage

    api = Api(app)
    api.add_resource(RegisterCiImage, '/ci_file')
    api.add_resource(RegisterFaceImage, '/face_file')

