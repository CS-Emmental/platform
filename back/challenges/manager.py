from core.manager import MongoManager
from challenges.models import ChallengeCategory, Challenge, ChallengeParticipation


class ChallengesManager(MongoManager):
    def __init__(self):
        super().__init__("challenges")

    def get_all(self):
        return [Challenge.from_dict(x) for x in super().get_all()]

    def get(self, challenge_id):
        return Challenge.from_dict(super().get(challenge_id))

    def update_one(self, challenge):
        return super().update_one(challenge.challenge_id, challenge.to_insert_dict())

    def insert_one(self, challenge):
        return super().insert_one(challenge.to_insert_dict())

    def remove_one(self, challenge):
        return super().remove_one(challenge.challenge_id)


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


class ChallengeParticipationsManager(MongoManager):
    def __init__(self):
        super().__init__("challenge_participations")

    def get(self, participation_id):
        return ChallengeParticipation.from_dict(super().get(participation_id))

    def get_query(self, query):
        return [ChallengeParticipation.from_dict(x) for x in super().get_query(query)]

    def update_one(self, participation):
        return super().update_one(
            participation.participation_id, participation.to_insert_dict()
        )

    def insert_one(self, participation):
        return super().insert_one(participation.to_insert_dict())

    def remove_one(self, participation):
        return super().remove_one(participation.participation_id)
