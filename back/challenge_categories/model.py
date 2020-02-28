from core.model import Document, from_dict_class
from core.exceptions import (
    EmptyFieldException,
    EmmentalTypeException,
)


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
