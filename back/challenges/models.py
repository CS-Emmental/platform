import time
from uuid import uuid4
from flask import current_app
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

    editable_fields = [
        'title',
        'icon',
        'description',
    ]

    def __init__(self,
                 _id: str = None,
                 title: str = "",
                 icon: str = "fas fa-shield-alt",
                 description: str = "",
                 created_at: float = None):
        self._id = str(uuid4()) if not _id else _id
        self.category_id = self._id
        self.title = title
        self.icon = icon
        self.description = description
        self.created_at = time.time() if not created_at else created_at


    def update(self,inputs: dict = {}):
        inputs = {k: inputs[k] for k in self.editable_fields}
        for key in inputs:
            setattr(self, key, inputs[key])

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
