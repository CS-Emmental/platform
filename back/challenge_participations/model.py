from core.model import Document

from core.exceptions import EmmentalUnionException


class ChallengeParticipation(Document):
    fields = Document.fields + [
        "challenge_id",
        "user_id",
        "status",
        "rating",
        "found_flags",
        "used_hints",
        "port",
        "started_at",
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
        "started_at",
    ]

    editable_fields = Document.editable_fields + [
        "rating",
    ]

    def __init__(
        self,
        challenge_id: str = "",
        user_id: str = "",
        status: str = "",  # ""|"ongoing"|"stopped"
        rating: int = None,
        found_flags: list = None,
        used_hints: list = None,
        port: int = None,
        started_at: int = None,
        **kwargs,
    ):

        super().__init__(**kwargs)
        self.participation_id = self._id
        self.challenge_id = challenge_id
        self.user_id = user_id
        self.status = status
        self.rating = rating
        self.found_flags = found_flags if found_flags else []
        self.used_hints = used_hints if used_hints else []
        self.port = port
        self.started_at = started_at

        self.verify()

    def verify(self):
        super().verify()
        if self.status not in ("", "ongoing", "stopped"):
            raise EmmentalUnionException(
                error_code=25, field="status", incorrect_input=self.status
            )

    @staticmethod
    def from_dict(dict_object: dict):
        return Document.from_dict_class(dict_object, ChallengeParticipation)
