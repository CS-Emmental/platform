from core.manager import MongoManager
from challenges.models import ChallengeCategory

class ChallengesManager(MongoManager):
    def __init__(self):
        super().__init__('challenges')

class ChallengeCategoriesManager(MongoManager):
    def __init__(self):
        super().__init__('challenge_categories')
    
    def get_all(self):
        return [ChallengeCategory.from_dict(x) for x in super().get_all()]
    
    def update_one(self,data):
        return super().update_one(data)
    
    def delete_one(self,data):
        return super().delete_one(data)

    def create_one(self,data):
        return super().insert_one(data)
