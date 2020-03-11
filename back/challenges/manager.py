from core.manager import MongoManager
from challenges.model import Challenge


class ChallengeManager(MongoManager):
    def __init__(self):
        super().__init__("challenges")

    def get_all(self):
        return [Challenge.from_dict(x) for x in super().get_all()]

    def get(self, challenge_id):
        return Challenge.from_dict(super().get(challenge_id))

    def get_query(self, query):
        return [Challenge.from_dict(x) for x in super().get_query(query)]

    def update_one(self, challenge):
        return super().update_one(challenge.challenge_id, challenge.to_insert_dict())

    def insert_one(self, challenge):
        return super().insert_one(challenge.to_insert_dict())

    def remove_one(self, challenge):
        return super().remove_one(challenge.challenge_id)
