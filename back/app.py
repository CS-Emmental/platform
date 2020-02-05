import os
import traceback

from flask import Flask, jsonify
from flask.logging import create_logger
from flask_cors import CORS
from flask_pymongo import PyMongo
from flask_login import LoginManager, current_user

from routes.challenges import challenges
from routes.users import users

from users.manager import UserManager

from core.exceptions import EmmentalException


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY="dev", MONGO_URI="mongodb://mongo:27017/cs-emmental")

    app.mongo = PyMongo(app)
    login_manager = LoginManager()
    login_manager.init_app(app)
    CORS(app, supports_credentials=True)
    app.logger = create_logger(app)

    @login_manager.user_loader
    def load_user(user_id):
        return UserManager().get(user_id)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.errorhandler(EmmentalException)
    def handle_emmental_exception(e):
        app.logger.error(traceback.format_exc())
        response = jsonify({"error_code": e.error_code, "error_message": e.error_message,})
        return response, e.status_code

    @app.errorhandler(Exception)
    def handle_exception(e):
        app.logger.error(traceback.format_exc())
        response = jsonify({"error_code": -1, "error_message": "Unknown Error",})
        return response, 500

    app.register_blueprint(users)
    app.register_blueprint(challenges)

    @app.route("/config")
    def config():
        res = {"version": "0.0.1", "isAuthenticated": current_user.is_authenticated}
        if current_user.is_authenticated:
            res.update({"currentUser": current_user.to_dict()})
        return jsonify(res)

    return app
