import time
from uuid import uuid4
from flask_login import UserMixin

from core.models import Document, from_dict_class


class User(Document, UserMixin):
    fields = [
        "_id",
        "username",
        "password",
        "email",
        "firstname",
        "lastname",
        "is_active",
        "created_at",
        "permissions",
    ]

    export_fields = [
        "user_id",
        "username",
        "email",
        "firstname",
        "lastname",
        "is_active",
        "created_at",
        "permissions",
    ]

    editable_fields = [
        "email",
        "firstname",
        "lastname",
    ]

    def __init__(
        self,
        _id: str = None,
        username: str = "",
        password: str = "",
        email: str = "",
        firstname: str = "",
        lastname: str = "",
        is_active: bool = True,
        permissions: list = [],
        created_at: float = None,
    ):
        self._id = str(uuid4()) if not _id else _id
        self.user_id = self._id
        self.username = username
        self.password = password
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.permissions = permissions
        self.created_at = time.time() if not created_at else created_at

    def get_id(self):
        return self.user_id

    def has_permissions(self, permissions):
        return set(permissions) <= set(self.permissions)

    @staticmethod
    def from_dict(dict_object: dict):
        return from_dict_class(dict_object, User)
