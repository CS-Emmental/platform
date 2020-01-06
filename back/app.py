import os

from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo
from flask_login import LoginManager

from routes.challenges import challenges
from routes.users import users

from users.manager import UserManager

def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        MONGO_URI='mongodb://mongo:27017/cs-emmental'
    )

    app.mongo = PyMongo(app)
    login_manager = LoginManager()
    login_manager.init_app(app)
    CORS(app, supports_credentials=True)

    @login_manager.user_loader
    def load_user(user_id):
        return UserManager().get(user_id)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(users)
    app.register_blueprint(challenges)

    return app
