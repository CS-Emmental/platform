import time
from uuid import uuid4


class ChallengeCategory():
    def __init__(self,
                 title: str,
                 _id: str = uuid4(),
                 icon: str = "fas fa-shield-alt",
                 description: str = "",
                 created_at: float = time.time()):
        self._id = _id
        self.title = title
        self.icon = icon
        self.description = description
        self.created_at = created_at

    @staticmethod
    def from_dict(source):
        return ChallengeCategory(**source)

    def to_dict(self):
        return vars(self)
