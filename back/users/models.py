import time
from uuid import uuid4
from flask_login import UserMixin

from core.models import Document, from_dict_class

class User(Document, UserMixin):
    fields = [
        '_id',
        'username',
        'password',
        'email',
        'firstname',
        'lastname',
        'is_active',
        'created_at',
        'permissions',
    ]

    export_fields = [
        'user_id',
        'username',
        'email',
        'firstname',
        'lastname',
        'is_active',
        'created_at',
        'permissions',
    ]
    
    def __init__(self,
                 _id: str = str(uuid4()),
                 username: str = "",
                 password: str = "",
                 email: str = "",
                 firstname: str = "",
                 lastname: str = "",
                 is_active: bool = True,
                 permissions: list = [],
                 created_at: float = time.time()):
        self._id = _id
        self.user_id = _id
        self.username = username
        self.password = password
        self.email = email
        self.firstname = firstname
        self.lastname = lastname  
        self.permissions = permissions
        self.created_at = created_at

    def get_id(self):
        return self.user_id

    @staticmethod
    def from_dict(dict_object: dict):
        return from_dict_class(dict_object, User)