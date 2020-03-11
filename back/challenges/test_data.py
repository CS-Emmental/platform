from core.exceptions import (
    EmmentalTypeException,
    EmmentalEmptyFieldException,
    EmmentalDateException,
    EmmentalNotUniqueException,
)
from challenges.exceptions import EmmentalFlagsException, EmmentalHintsException
from challenges.model import Challenge

data_challenge_legit_args = [
    (
        {
            "_id": "a",
            "title": "a",
            "description": "a",
            "summary": "a",
            "category_id": "a",
            "total_points": 0,
            "flags": [{"reward": 1, "secret": "", "text": ""}],
            "hints": [{"cost": 0.5, "text": ""}],
            "created_at": 0,
            "updated_at": 0,
        },
        {
            "_id": "a",
            "title": "a",
            "description": "a",
            "summary": "a",
            "category_id": "a",
            "total_points": 0,
            "flags": [{"reward": 1, "secret": "", "text": ""}],
            "hints": [{"cost": 0.5, "text": ""}],
            "created_at": 0,
            "updated_at": 0,
        },
    ),
    (
        {
            "_id": "c853fd69-e222-4e07-a261-efe1791aa542",
            "title": "title",
            "description": "description",
            "summary": "summary",
            "category_id": "category",
            "total_points": 0,
            "flags": [],
            "hints": [],
            "created_at": 1581002681,
            "updated_at": 1581002681,
        },
        {
            "_id": "c853fd69-e222-4e07-a261-efe1791aa542",
            "title": "title",
            "description": "description",
            "summary": "summary",
            "category_id": "category",
            "total_points": 0,
            "flags": [],
            "hints": [],
            "created_at": 1581002681,
            "updated_at": 1581002681,
        },
    ),
    (
        {
            "_id": "c853fd69-e222-4e07-a261-efe1791aa542",
            "title": "title",
            "description": "description",
            "summary": "summary",
            "category_id": "category",
            "total_points": 0,
            "flags": [],
            "hints": [],
            "created_at": 1581002681,
            "updated_at": 1681002681,
        },
        {
            "_id": "c853fd69-e222-4e07-a261-efe1791aa542",
            "title": "title",
            "description": "description",
            "summary": "summary",
            "category_id": "category",
            "total_points": 0,
            "flags": [],
            "hints": [],
            "created_at": 1581002681,
            "updated_at": 1681002681,
        },
    ),
]

data_challenge_error = [
    (
        # updated_at explicitly before created_at
        {
            "_id": None,
            "title": "a",
            "description": "a",
            "summary": "a",
            "category_id": "a",
            "total_points": 0,
            "flags": [],
            "hints": [],
            "created_at": 10,
            "updated_at": 5,
        },
        EmmentalDateException,
    ),
    (
        # updated_at implicitly before created_at
        {
            "_id": None,
            "title": "a",
            "description": "a",
            "summary": "a",
            "category_id": "a",
            "total_points": 0,
            "flags": [],
            "hints": [],
            "created_at": None,
            "updated_at": 5,
        },
        EmmentalDateException,
    ),
    (
        # title cannot be empty
        {
            "_id": None,
            "title": "",
            "description": "a",
            "summary": "a",
            "category_id": "a",
            "total_points": 0,
            "flags": [],
            "hints": [],
            "created_at": None,
            "updated_at": None,
        },
        EmmentalEmptyFieldException,
    ),
    (
        # title must be a string
        {
            "_id": None,
            "title": None,
            "description": "a",
            "summary": "a",
            "category_id": "a",
            "total_points": 0,
            "flags": [],
            "hints": [],
            "created_at": None,
            "updated_at": None,
        },
        EmmentalTypeException,
    ),
    (
        # description must be a string
        {
            "_id": None,
            "title": "a",
            "description": None,
            "summary": "a",
            "category_id": "a",
            "total_points": 0,
            "flags": [],
            "hints": [],
            "created_at": None,
            "updated_at": None,
        },
        EmmentalTypeException,
    ),
    (
        # summary must be a string
        {
            "_id": None,
            "title": "a",
            "description": "a",
            "summary": 1,
            "category_id": "a",
            "total_points": 0,
            "flags": [],
            "hints": [],
            "created_at": None,
            "updated_at": None,
        },
        EmmentalTypeException,
    ),
    (
        # category_id must be a string
        {
            "_id": None,
            "title": "a",
            "description": "a",
            "summary": "a",
            "category_id": [],
            "total_points": 0,
            "flags": [],
            "hints": [],
            "created_at": None,
            "updated_at": None,
        },
        EmmentalTypeException,
    ),
    (
        # total_points must be an int
        {
            "_id": None,
            "title": "a",
            "description": "a",
            "summary": "a",
            "category_id": "",
            "total_points": "points",
            "flags": [],
            "hints": [],
            "created_at": None,
            "updated_at": None,
        },
        EmmentalTypeException,
    ),
    (
        # flags must be a list
        {
            "_id": None,
            "title": "a",
            "description": "a",
            "summary": "a",
            "category_id": "",
            "total_points": 0,
            "flags": "[]",
            "hints": [],
            "created_at": None,
            "updated_at": None,
        },
        EmmentalTypeException,
    ),
    (
        # hints must be a list
        {
            "_id": None,
            "title": "a",
            "description": "a",
            "summary": "a",
            "category_id": "",
            "total_points": 0,
            "flags": [],
            "hints": "[]",
            "created_at": None,
            "updated_at": None,
        },
        EmmentalTypeException,
    ),
    (
        # cost of hints can't exceed 1
        {
            "_id": None,
            "title": "None",
            "description": "a",
            "summary": "a",
            "category_id": "a",
            "total_points": 0,
            "flags": [],
            "hints": [{"cost": 0.2, "text": ""}, {"cost": 0.9, "text": ""}],
            "created_at": None,
            "updated_at": None,
        },
        EmmentalHintsException,
    ),
    (
        # hints cost cannot be negative
        {
            "_id": None,
            "title": "None",
            "description": "a",
            "summary": "a",
            "category_id": "a",
            "total_points": 0,
            "flags": [],
            "hints": [{"cost": -0.2, "text": ""}, {"cost": 0.2, "text": ""}],
            "created_at": None,
            "updated_at": None,
        },
        EmmentalHintsException,
    ),
    (
        # flags reward cannot be negative
        {
            "_id": None,
            "title": "None",
            "description": "a",
            "summary": "a",
            "category_id": "a",
            "total_points": 0,
            "flags": [
                {"reward": 0.2, "secret": "", "text": ""},
                {"reward": -0.2, "secret": "", "text": ""},
            ],
            "hints": [],
            "created_at": None,
            "updated_at": None,
        },
        EmmentalFlagsException,
    ),
    (
        # flags reward total sum must equal one
        {
            "_id": None,
            "title": "None",
            "description": "a",
            "summary": "a",
            "category_id": "a",
            "total_points": 0,
            "flags": [
                {"reward": 0.9, "secret": "", "text": ""},
                {"reward": 0.2, "secret": "", "text": ""},
            ],
            "hints": [],
            "created_at": None,
            "updated_at": None,
        },
        EmmentalFlagsException,
    ),
    (
        # flags reward total sum must equal one
        {
            "_id": None,
            "title": "None",
            "description": "a",
            "summary": "a",
            "category_id": "a",
            "total_points": 0,
            "flags": [{"reward": 0.9, "secret": "", "text": ""}],
            "hints": [],
            "created_at": None,
            "updated_at": None,
        },
        EmmentalFlagsException,
    ),
]

data_controller_update = [
    (
        # Simplest example
        Challenge(title="old_title"),
        {"title": "new_title"},
        Challenge(title="new_title"),
    ),
    (
        # Realistic example (from almost empty object to fully set object)
        Challenge(title="empty challenge"),
        {
            "title": "Very Simple Challenge",
            "description": "Lorem ipsum dolor sit amet.",
            "summary": "Lorem ipsum dolor sit amet.",
            "category_id": "d626d9aa-f8a9-45b6-8f49-74893ee27e41",  # uuid4
            "total_points": 100,
            "flags": [
                {"reward": 1, "secret": "1234", "text": "The secret to find is four digits",}
            ],
            "hints": [{"cost": 0.5, "text": "Try some common passwords ;)",}],
            "ports": [8888],
            "image": "my-docker-image",
            "challenge_type": "web",
        },
        Challenge(
            title="Very Simple Challenge",
            description="Lorem ipsum dolor sit amet.",
            summary="Lorem ipsum dolor sit amet.",
            category_id="d626d9aa-f8a9-45b6-8f49-74893ee27e41",
            total_points=100,
            flags=[{"reward": 1, "secret": "1234", "text": "The secret to find is four digits",}],
            hints=[{"cost": 0.5, "text": "Try some common passwords ;)",}],
            ports=[8888],
            image="my-docker-image",
            challenge_type="web",
        ),
    ),
]

data_controller_update_errors = [
    (
        # Count is not 0
        Challenge(title="old title"),
        1,
        {"title": "already existing slug title"},
        EmmentalNotUniqueException,
    ),
    (
        # The sum of reward of flag must be between 0 and 1
        Challenge(title="old title"),
        0,
        {
            "flags": [
                {"reward": 100, "secret": "1234", "text": "The secret to find is four digits",}
            ]
        },
        EmmentalFlagsException,
    ),
    (
        # The sum of reward of flag must be between 0 and 1
        Challenge(title="old title"),
        0,
        {
            "flags": [
                {"reward": 0.8, "secret": "1234", "text": "The secret to find is four digits",},
                {
                    "reward": 0.8,
                    "secret": "5678",
                    "text": "The secret to find is four digits different from previous ones",
                },
            ]
        },
        EmmentalFlagsException,
    ),
    (
        # Any reward of flags is positive
        Challenge(title="old title"),
        0,
        {
            "flags": [
                {"reward": -5, "secret": "1234", "text": "The secret to find is four digits",},
            ]
        },
        EmmentalFlagsException,
    ),
    (
        # Any reward of flags is positive
        Challenge(title="old title"),
        0,
        {
            "flags": [
                {"reward": -5, "secret": "1234", "text": "The secret to find is four digits",},
                {
                    "reward": 0.8,
                    "secret": "5678",
                    "text": "The secret to find is four digits different from previous ones",
                },
            ]
        },
        EmmentalFlagsException,
    ),
    (
        # Sum oh cost of hint cannot exceed 1
        Challenge(title="old title"),
        0,
        {"hints": [{"cost": 10, "text": "What are the first four digits ?",},]},
        EmmentalHintsException,
    ),
    (
        # Sum oh cost of hint cannot exceed 1
        Challenge(title="old title"),
        0,
        {
            "hints": [
                {"cost": 0.8, "text": "What are the first four digits ?",},
                {"cost": 0.8, "text": "What are the next four digits ?",},
            ]
        },
        EmmentalHintsException,
    ),
    (
        # Any cost of hint must be positive
        Challenge(title="old title"),
        0,
        {"hints": [{"cost": -9, "text": "What are the first four digits ?",},]},
        EmmentalHintsException,
    ),
    (
        # Sum oh cost of hint cannot exceed 1
        Challenge(title="old title"),
        0,
        {
            "hints": [
                {"cost": -6, "text": "What are the first four digits ?",},
                {"cost": 6.5, "text": "What are the next four digits ?",},
            ]
        },
        EmmentalHintsException,
    ),
]

data_controller_remove = [
    # Very simple test with dummy test data. To improve when the function tested becomes more complex
    (Challenge(_id="id", title="title"), {"n": 1, "ok": 1.0}, {"n": 1, "ok": 1.0})
]

data_controller_insert = [({"title": "value"}, {"title": "value"})]
