from core.manager import MongoManager
from users.models import User

class UserManager(MongoManager):
    def __init__(self):
        super().__init__('users')

    def get(self, user_id):
        return User.from_dict(self.collection.find({"_id": user_id})[0])

    def get_one_by_query(self, query):
        return User.from_dict(self.collection.find_one(query))

    def get_all(self):
        return [User.from_dict(x) for x in super().get_all()]