from flask_login import login_user, logout_user, current_user

from users.manager import UserManager

def login(inputs):
    user = UserManager().get_one_by_query(inputs)
    login_user(user)
    return user

def logout():
    logout_user()

def get_current_user():
    return current_user