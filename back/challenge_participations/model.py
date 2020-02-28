
from core.models import Document, from_dict_class


class ChallengeParticipation(Document):
    fields = Document.fields + [
        "challenge_id",
        "user_id",
        "status",
        "rating",
        "found_flags",
        "used_hints",
        "port",
    ]

    export_fields = Document.export_fields + [
        "participation_id",
        "challenge_id",
        "user_id",
        "status",
        "rating",
        "found_flags",
        "used_hints",
        "port",
    ]

    editable_fields = Document.editable_fields + [
        "rating",
    ]

    def __init__(
        self,
        _id: str = None,
        challenge_id: str = "",
        user_id: str = "",
        status: str = "ongoing",
        rating: int = None,
        found_flags: list = None,
        used_hints: list = None,
        created_at: int = None,
        updated_at: int = None,
        port: int = None,
    ):
        super().__init__(_id, created_at, updated_at)

        self.participation_id = self._id
        self.challenge_id = challenge_id
        self.user_id = user_id
        self.status = status
        self.rating = rating
        self.found_flags = found_flags if found_flags else []
        self.used_hints = used_hints if used_hints else []
        self.port = port

    @staticmethod
    def from_dict(dict_object: dict):
        return from_dict_class(dict_object, ChallengeParticipation)