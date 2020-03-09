from core.manager import MongoManager
from challenge_participations.model import ChallengeParticipation


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
