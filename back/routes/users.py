from flask import Blueprint, jsonify, current_app
from flask_login import login_user, logout_user, login_required

from users.manager import UserManager

users = Blueprint('users', 'users')

@users.route('/login')
def login():
    user = UserManager().get_all()[0]
    login_user(user)
    return jsonify(user.to_dict())

@users.route('/current-user')
@login_required
def current_user():
    user = UserManager().get_all()[0]
    return jsonify(user.to_dict())

@users.route('/logout')
@login_required
def logout():
    logout_user()
    return jsonify("logout")