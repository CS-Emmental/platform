import datetime
from uuid import uuid4

from mongoengine import Document, UUIDField, StringField, DateTimeField


class ChallengeCategory(Document):
    _id = UUIDField(primary_key=True, default=uuid4(), binary=False)
    title = StringField(required=True, max_length=200)
    icon = StringField(default="fas fa-shield-alt")
    description = StringField(max_length=2000)
    created_at = DateTimeField(default=datetime.datetime.now)

    meta = {'collection': 'challenge_categories'}
