from challenges.exceptions import EmmentalFlagsException, \
    EmmentalHintsException, EmmentalContainersException
from core.exceptions import EmmentalEmptyFieldException, EmmentalTypeException
from core.model import Document
from core.utils import slug


class Challenge(Document):
    fields = Document.fields + [
        "title",
        "title_slug",
        "description",
        "category_id",
        "total_points",
        "summary",
        "flags",
        "hints",
        "challenge_type",
        "containers"
    ]

    export_fields = Document.export_fields + [
        "challenge_id",
        "title",
        "title_slug",
        "description",
        "category_id",
        "total_points",
        "summary",
        "flags",
        "hints",
        "challenge_type",
        "containers"
    ]

    editable_fields = Document.editable_fields + [
        "title",
        "description",
        "category_id",
        "total_points",
        "summary",
        "flags",
        "hints",
        "challenge_type",
        "containers"
    ]

    def __init__(
        self,
        title: str = "",
        title_slug: str = "",
        description: str = "",
        summary: str = "",
        category_id: str = "",
        total_points: int = 0,
        flags: list = None,  # List[flag] where flag: {"reward": int, "secret": str, "text": str}
        hints: list = None,  # List[hint] where hint: {"cost": float, "text": str}
        containers: dict = None,  # See documentation
        challenge_type: str = "",
        **kwargs,
    ):

        super().__init__(**kwargs)

        self.challenge_id = self._id
        self.title = title
        # Can come from db. Always equal slug(self.title), c.f verify
        self.title_slug = title_slug
        self.description = description
        self.summary = summary
        self.total_points = total_points
        self.category_id = category_id
        self.flags = flags if flags else []
        self.hints = hints
        self.containers = containers
        self.challenge_type = challenge_type

        self.verify()

    def verify(self):
        super().verify()
        if not isinstance(self.title, str):
            raise EmmentalTypeException(error_code=6, incorrect_input="title")

        if not isinstance(self.description, str):
            raise EmmentalTypeException(error_code=7, incorrect_input="description")

        if not isinstance(self.summary, str):
            raise EmmentalTypeException(error_code=8, incorrect_input="summary")

        if not isinstance(self.total_points, int):
            raise EmmentalTypeException(error_code=9, incorrect_input="total_points")

        if not isinstance(self.category_id, str):
            raise EmmentalTypeException(error_code=10, incorrect_input="category_id")

        if not isinstance(self.flags, list):
            raise EmmentalTypeException(error_code=11, incorrect_input="flags")

        if self.hints and not isinstance(self.hints, list):
            raise EmmentalTypeException(error_code=12, incorrect_input="hints")

        if not isinstance(self.challenge_type, str):
            raise EmmentalTypeException(error_code=13, incorrect_input="challenge_type")

        if (  # This check could be made more complete
            not isinstance(self.containers, dict)
            or "containers" not in self.containers
            or len(self.containers["containers"]) == 0
            or "exposed" not in self.containers
            or "container" not in self.containers["exposed"]
            or not isinstance(self.containers["exposed"]["container"], str)
            or "port" not in self.containers["exposed"]
            or not isinstance(self.containers["exposed"]["port"], int)
        ):
            raise EmmentalContainersException(error_code=14)

        if self.hints and (
            sum([hint["cost"] for hint in self.hints]) > 1
            or min([hint["cost"] for hint in self.hints]) < 0
        ):
            raise EmmentalHintsException(error_code=16)

        if self.flags and (
            sum([flag["reward"] for flag in self.flags]) != 1
            or min([flag["reward"] for flag in self.flags]) < 0
        ):
            raise EmmentalFlagsException(error_code=17)

        if self.title == "" or self.title is None:
            raise EmmentalEmptyFieldException(error_code=18, blank_field="title")

        # Once "outer" inputs are fine, we can check and set following fields accordingly
        if self.title_slug != slug(self.title):
            self.title_slug = slug(self.title)

    @staticmethod
    def from_dict(dict_object: dict):
        dict_object["total_points"] = int(dict_object["total_points"])
        return Document.from_dict_class(dict_object, Challenge)
