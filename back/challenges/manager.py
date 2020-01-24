from core.manager import MongoManager
from challenges.models import ChallengeCategory, Challenge

class ChallengesManager(MongoManager):
    def __init__(self):
        super().__init__('challenges')

    def get_all(self):
        return [Challenge.from_dict(x) for x in super().get_all()]
    
    def get(self, challenge_id):
        return Challenge.from_dict(super().get(challenge_id))

    def update_one(self, challenge):
        return super().update_one(challenge.challenge_id, challenge.to_insert_dict())
    
    def insert_one(self, challenge):
        return super().insert_one(challenge.to_insert_dict())

class ChallengeCategoriesManager(MongoManager):
    def __init__(self):
        super().__init__('challenge_categories')
    
    def get_all(self):
        return [ChallengeCategory.from_dict(x) for x in super().get_all()]
