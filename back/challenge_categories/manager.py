from core.manager import MongoManager
from challenge_categories.model import ChallengeCategory

class ChallengeCategoriesManager(MongoManager):
    def __init__(self):
        super().__init__("challenge_categories")

    def get_all(self):
        return [ChallengeCategory.from_dict(x) for x in super().get_all()]

    def get(self, category_id):
        return ChallengeCategory.from_dict(super().get(category_id))

    def update_one(self, category):
        return super().update_one(category.category_id, category.to_insert_dict())

    def insert_one(self, category):
        return super().insert_one(category.to_insert_dict())

    def remove_one(self, category):
        return super().remove_one(category.category_id)
