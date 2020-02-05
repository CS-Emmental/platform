import time
from uuid import uuid4


class Document:
    fields = [
        "_id",
        "created_at",
        "updated_at",
    ]

    export_fields = [
        "created_at",
        "updated_at",
    ]

    editable_fields = []

    def __init__(
        self, _id: str = None, created_at: int = None, updated_at: int = None,
    ):
        self._id = str(uuid4()) if not _id else _id
        self.created_at = int(time.time()) if not created_at else created_at
        self.updated_at = int(time.time()) if not updated_at else updated_at

    def to_dict(self):
        return {key: getattr(self, key) for key in self.export_fields}

    def to_insert_dict(self):
        return {key: getattr(self, key) for key in self.fields}

    def to_update_dict(self):
        return {key: getattr(self, key) for key in self.editable_fields}

    def update(self, inputs: dict = None):
        inputs_filtered = {k: inputs[k] for k in self.editable_fields}
        for key in inputs_filtered:
            setattr(self, key, inputs_filtered[key])
        setattr(self, "updated_at", int(time.time()))

    @staticmethod
    def from_dict(dict_object: dict):
        raise NotImplementedError


def from_dict_class(dict_object: dict, Class):
    kwargs = {key: value for (key, value) in dict_object.items() if key in Class.fields}
    return Class(**kwargs)
