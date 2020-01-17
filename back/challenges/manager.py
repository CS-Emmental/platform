from core.manager import MongoManager
from challenges.models import ChallengeCategory, Challenge

class ChallengesManager(MongoManager):
    def __init__(self):
        super().__init__('challenges')

    def get_all(self):
        return [Challenge.from_dict(x) for x in super().get_all()]

class ChallengeCategoriesManager(MongoManager):
    def __init__(self):
        super().__init__('challenge_categories')
    
    def get_all(self):
        return [ChallengeCategory.from_dict(x) for x in super().get_all()]