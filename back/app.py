import os

from flask import Flask
from flask_cors import CORS
from flask_mongoengine import MongoEngine

from routes.challenge_groups import challenge_groups

def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        MONGODB_SETTINGS={
            'db': 'cs-emmental',
            'host': 'mongo',
            'port': 27017,
        },
    )

    CORS(app)
    MongoEngine(app)

    app.config.from_pyfile('config.py', silent=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(challenge_groups, url_prefix='/challenge-groups')

    return app
