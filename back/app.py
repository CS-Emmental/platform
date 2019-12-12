import os

from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo

from routes.challenges import challenges

def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        MONGO_URI='mongodb://mongo:27017/cs-emmental'
    )

    app.mongo = PyMongo(app)
    CORS(app)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(challenges)

    return app
