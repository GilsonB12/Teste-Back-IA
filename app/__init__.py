from flask import Flask
from flask_pymongo import PyMongo
from flasgger import Swagger
from .config import Config

mongo = PyMongo()
swagger = Swagger()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    mongo.init_app(app)
    swagger.init_app(app)

    from .routes.process_routes import process_bp
    app.register_blueprint(process_bp)

    return app
