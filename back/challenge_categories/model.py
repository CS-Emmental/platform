from core.exceptions import EmmentalEmptyFieldException, EmmentalTypeException
from core.model import Document, from_dict_class
from core.utils import slug


class ChallengeCategory(Document):
    fields = Document.fields + [
        "title",
        "title_slug",
        "icon",
        "description",
    ]

    export_fields = Document.export_fields + [
        "category_id",
        "title",
        "title_slug",
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
        title_slug: str = "",
        icon: str = "fas fa-shield-alt",
        description: str = "",
        created_at: int = None,
        updated_at: int = None,
    ):
        super().__init__(_id, created_at, updated_at)
        self.category_id = self._id
        self.title = title
        self.title_slug = title_slug  # Can come from db. Always equal slug(self.title), c.f verify
        self.icon = icon
        self.description = description

        self.verify()

    def verify(self):
        super().verify()

        if not isinstance(self.title, str):
            raise EmmentalTypeException(error_code=2, incorrect_input="title")
        if not isinstance(self.icon, str):
            raise EmmentalTypeException(error_code=3, incorrect_input="icon")
        if not isinstance(self.description, str):
            raise EmmentalTypeException(error_code=4, incorrect_input="description")

        if self.title == "" or self.title == None:
            raise EmmentalEmptyFieldException(error_code=5, blank_field="title")

        # Once "outer" inputs are fine, we can check and set following fields accordingly
        if self.title_slug != slug(self.title):
            self.title_slug = slug(self.title)

    @staticmethod
    def from_dict(dict_object: dict):
        return from_dict_class(dict_object, ChallengeCategory)
