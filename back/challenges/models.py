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
                 _id: str = str(uuid4()),
                 title: str = "",
                 icon: str = "fas fa-shield-alt",
                 description: str = "",
                 created_at: float = time.time()):
        self._id = _id
        self.category_id = _id
        self.title = title
        self.icon = icon
        self.description = description
        self.created_at = created_at

    @staticmethod
    def from_dict(dict_object: dict):
        return from_dict_class(dict_object, ChallengeCategory)


class Challenge(Document):
    fields = [
        '_id',
        'title',
        'description',
        'category_id',
        'created_at',
        'total_points',
        'summary',
    ]

    export_fields = [
        'challenge_id',
        'title',
        'description',
        'category_id',
        'created_at',
        'total_points',
        'summary',
    ]

    editable_fields = [
        'title',
        'description',
        'category_id',
        'total_points',
        'summary',
    ]
    
    def __init__(self,
                 _id: str = str(uuid4()),
                 title: str = "",
                 description: str = "",
                 summary: str = "",
                 category_id: str = "",
                 total_points: int = 0,
                 created_at: float = time.time()):
        self._id = _id
        self.challenge_id = _id
        self.title = title
        self.description = description
        self.summary = summary
        self.total_points = total_points
        self.category_id = category_id
        self.created_at = created_at

    @staticmethod
    def from_dict(dict_object: dict):
        return from_dict_class(dict_object, Challenge)
