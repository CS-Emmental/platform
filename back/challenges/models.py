from core.models import Document, from_dict_class
import time
from challenges.exceptions import (
    EmptyFieldException,
    EmmentalTypeException,
    InconsistentHintsException,
    InconsistentFlagsException,
)


class ChallengeCategory(Document):
    fields = Document.fields + ["title", "icon", "description"]

    export_fields = Document.export_fields + [
        "category_id",
        "title",
        "icon",
        "description",
    ]

    editable_fields = Document.editable_fields + ["title", "icon", "description"]

    def __init__(
        self,
        _id: str = None,
        title: str = "",
        icon: str = "fas fa-shield-alt",
        description: str = "",
        created_at: int = None,
        updated_at: int = None,
    ):
        super().__init__(_id, created_at, updated_at)
        if (
            not isinstance(title, str)
            or not isinstance(icon, str)
            or not isinstance(description, str)
        ):
            raise EmmentalTypeException

        self.category_id = self._id
        self.title = title
        self.icon = icon
        self.description = description

        if self.title == "" or self.title == None:
            raise EmptyFieldException

    @staticmethod
    def from_dict(dict_object: dict):
        return from_dict_class(dict_object, ChallengeCategory)


class Challenge(Document):
    fields = Document.fields + [
        "title",
        "description",
        "category_id",
        "total_points",
        "summary",
        "flags",
        "hints",
        "ports",
        "image",
        "challenge_type",
    ]

    export_fields = Document.export_fields + [
        "challenge_id",
        "title",
        "description",
        "category_id",
        "total_points",
        "summary",
        "flags",
        "hints",
        "ports",
        "image",
        "challenge_type",
    ]

    editable_fields = Document.editable_fields + [
        "title",
        "description",
        "category_id",
        "total_points",
        "summary",
        "flags",
        "hints",
        "ports",
        "image",
        "challenge_type",
    ]

    def __init__(
        self,
        _id: str = None,
        title: str = "",
        description: str = "",
        summary: str = "",
        category_id: str = "",
        total_points: int = 0,
        flags: list = None,
        hints: list = None,
        created_at: int = None,
        updated_at: int = None,
        ports: list = None,
        image: str = "",
        challenge_type: str = "",
    ):

        super().__init__(_id, created_at, updated_at)

        self.challenge_id = self._id
        self.title = title
        self.description = description
        self.summary = summary
        self.total_points = total_points
        self.category_id = category_id
        self.flags = flags
        self.hints = hints
        self.ports = ports
        self.image = image
        self.challenge_type = challenge_type

        self.verify()

    def verify(self):
        if (
            not isinstance(self.title, str)
            or not isinstance(self.description, str)
            or not isinstance(self.summary, str)
            or not isinstance(self.total_points, int)
            or not isinstance(self.category_id, str)
            or not isinstance(self.flags, list)
            or (self.hints and not isinstance(self.hints, list))
        ):
            raise EmmentalTypeException

        if self.hints and (
            sum([hint["cost"] for hint in self.hints]) > 1
            or min([hint["cost"] for hint in self.hints]) < 0
        ):
            raise InconsistentHintsException

        if self.flags and (
            sum([flag["reward"] for flag in self.flags]) != 1
            or min([flag["reward"] for flag in self.flags]) < 0
        ):
            raise InconsistentFlagsException

        if self.title == "" or self.title is None:
            raise EmptyFieldException
        
    @staticmethod
    def from_dict(dict_object: dict):
        dict_object["total_points"] = int(dict_object["total_points"])
        return from_dict_class(dict_object, Challenge)


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

    editable_fields = Document.editable_fields + ["rating"]

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
