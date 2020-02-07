from core.models import Document, from_dict_class


class ChallengeCategory(Document):
    fields = Document.fields + [
        "title",
        "icon",
        "description",
    ]

    export_fields = Document.export_fields + [
        "category_id",
        "title",
        "icon",
        "description",
    ]

    editable_fields = Document.editable_fields + [
        "title",
        "icon",
        "description",
    ]

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

        self.category_id = self._id
        self.title = title
        self.icon = icon
        self.description = description

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
    ]

    editable_fields = Document.editable_fields + [
        "title",
        "description",
        "category_id",
        "total_points",
        "summary",
        "flags",
        "hints",
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

    @staticmethod
    def from_dict(dict_object: dict):
        return from_dict_class(dict_object, Challenge)


class ChallengeParticipation(Document):
    fields = Document.fields + [
        "challenge_id",
        "user_id",
        "status",
        "rating",
        "found_flags",
        "used_hints",
    ]

    export_fields = Document.export_fields + [
        "participation_id",
        "challenge_id",
        "user_id",
        "status",
        "rating",
        "found_flags",
        "used_hints",
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
    ):
        super().__init__(_id, created_at, updated_at)

        self.participation_id = self._id
        self.challenge_id = challenge_id
        self.user_id = user_id
        self.status = status
        self.rating = rating
        self.found_flags = found_flags if found_flags else []
        self.used_hints = used_hints if used_hints else []

    @staticmethod
    def from_dict(dict_object: dict):
        return from_dict_class(dict_object, ChallengeParticipation)
