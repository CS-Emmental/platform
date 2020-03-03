import os
import traceback

import kubernetes
from flask import Flask, jsonify
from flask.logging import create_logger
from flask_login import LoginManager, current_user
from flask_pymongo import PyMongo

from core.exceptions import EmmentalException
from routes.challenges import challenges
from routes.challenge_categories import challenge_categories
from routes.challenge_participations import challenge_participations
from routes.users import users
from users.manager import UserManager


def create_app(testing=False):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # Load conf depending on the mode
    if testing:
        app.config.from_pyfile("test.conf.py", silent=False)
    elif app.env == "development":
        app.config.from_pyfile("back.conf.py", silent=False)
    elif app.env == "production":
        app.config.from_pyfile("/etc/config/back.conf.py", silent=False)
    else:
        raise ValueError("App mode unknow: not in dev|prod|test")

    # K8sManager configuration changes with app mode
    app.k8s = None
    if not testing:
        if app.env == "development":
            k8s_configuration = kubernetes.client.Configuration()
            k8s_configuration.verify_ssl = False
            k8s_configuration.debug = False
            k8s_configuration.host = app.config["K8S_HOST"]
            k8s_configuration.api_key["authorization"] = app.config["K8S_API_KEY"]
            k8s_configuration.api_key_prefix["authorization"] = "Bearer"

            app.k8s = kubernetes.client.ApiClient(k8s_configuration)
        else:
            kubernetes.config.load_incluster_config()
            app.k8s = kubernetes.client.ApiClient()

    app.mongo = PyMongo(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    app.logger = create_logger(app)

    @login_manager.user_loader
    def load_user(user_id):
        return UserManager().get(user_id)

    @app.errorhandler(EmmentalException)
    def handle_emmental_exception(e):
        app.logger.error(traceback.format_exc())
        app.logger.error(e.internal_message)
        response = jsonify({"error_code": e.error_code, "error_message": e.external_message,})
        return response, e.status_code

    @app.errorhandler(Exception)
    def handle_exception(e):
        app.logger.error(traceback.format_exc())
        response = jsonify({"error_code": -1, "error_message": "Unknown Error",})
        return response, 500

    app.register_blueprint(users)
    app.register_blueprint(challenges)
    app.register_blueprint(challenge_categories)
    app.register_blueprint(challenge_participations)

    @app.route("/config")
    def config():
        res = {
            "version": "0.0.1",
            "isAuthenticated": current_user.is_authenticated,
            "env": app.env,
        }
        if current_user.is_authenticated:
            res.update({"currentUser": current_user.to_dict()})
        return jsonify(res)

    return app
