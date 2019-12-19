import time
from uuid import uuid4

from core.models import Document, from_dict_class

class ChallengeCategory(Document):
    fields = [
        '_id',
        'title',
        'icon',
        'description',
        'created_at',
    ]

    export_fields = [
        'category_id',
        'title',
        'icon',
        'description',
        'created_at'
    ]

    def __init__(self,
                 _id: str = uuid4(),
                 title: str = "",
                 icon: str = "fas fa-shield-alt",
                 description: str = "",
                 created_at: float = time.time()):
        self._id = _id
        self.title = title
        self.icon = icon
        self.description = description
        self.created_at = created_at

    @staticmethod
    def from_dict(dict_object: dict):
        return from_dict_class(dict_object, ChallengeCategory)


class Challenge(Document):
    def __init__(self,
                 _id: str = uuid4(),
                 title: str = "",
                 description: str = "",
                 created_at: float = time.time()):
        self._id = _id
        self.title = title
        self.description = description
        self.created_at = created_at

    @staticmethod
    def from_dict(source):
        return Challenge(**source)
