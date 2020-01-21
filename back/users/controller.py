from flask_login import login_user, logout_user

from users.manager import UserManager
from users.models import User

def login(inputs):
    user = UserManager().get_one_by_query(inputs)
    login_user(user)
    return user

def signup(inputs):
    user = User(**inputs)
    if UserManager().insert_one(user):
        login_user(user)
        return user

def logout():
    logout_user()