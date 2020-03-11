from core.exceptions import EmmentalNotUniqueException
from challenges.exceptions import EmmentalFlagsException, EmmentalHintsException
from challenges.model import Challenge


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
                {
                    "reward": 1,
                    "secret": "1234",
                    "text": "The secret to find is four digits",
                }
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
            flags=[
                {
                    "reward": 1,
                    "secret": "1234",
                    "text": "The secret to find is four digits",
                }
            ],
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
                {
                    "reward": 100,
                    "secret": "1234",
                    "text": "The secret to find is four digits",
                }
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
                {
                    "reward": 0.8,
                    "secret": "1234",
                    "text": "The secret to find is four digits",
                },
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
                {
                    "reward": -5,
                    "secret": "1234",
                    "text": "The secret to find is four digits",
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
                {
                    "reward": -5,
                    "secret": "1234",
                    "text": "The secret to find is four digits",
                },
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
    # Very simple test. To improve when the function tested becomes more complex
    (Challenge(_id="id", title="title"), {"n": 1, "ok": 1.0}, {"n": 1, "ok": 1.0})
]

data_controller_insert = [
    # Simplest insertion
    ({"title": "title"}, {"nInserted": 1}, 0, Challenge(title="title")),
    # Complete realistic insertion
    (
        {
            "title": "Very Simple Challenge",
            "description": "Lorem ipsum dolor sit amet.",
            "summary": "Lorem ipsum dolor sit amet.",
            "category_id": "d626d9aa-f8a9-45b6-8f49-74893ee27e41",  # uuid4
            "total_points": 100,
            "flags": [
                {
                    "reward": 1,
                    "secret": "1234",
                    "text": "The secret to find is four digits",
                }
            ],
            "hints": [{"cost": 0.5, "text": "Try some common passwords ;)",}],
            "ports": [8888],
            "image": "my-docker-image",
            "challenge_type": "web",
        },
        {"nInserted": 1},
        0,
        Challenge(
            title="Very Simple Challenge",
            description="Lorem ipsum dolor sit amet.",
            summary="Lorem ipsum dolor sit amet.",
            category_id="d626d9aa-f8a9-45b6-8f49-74893ee27e41",
            total_points=100,
            flags=[
                {
                    "reward": 1,
                    "secret": "1234",
                    "text": "The secret to find is four digits",
                }
            ],
            hints=[{"cost": 0.5, "text": "Try some common passwords ;)",}],
            ports=[8888],
            image="my-docker-image",
            challenge_type="web",
        ),
    ),
]

data_controller_insert_errors = [
    # Test if it raises an error if Mongo tells there is already a category with the same title slug
    (1, {"title": "a title whose slug already exists"}, EmmentalNotUniqueException),
    (10, {"title": "a title whose slug already exists"}, EmmentalNotUniqueException),
    (
        # The sum of reward of flag must be between 0 and 1
        0,
        {
            "flags": [
                {
                    "reward": 100,
                    "secret": "1234",
                    "text": "The secret to find is four digits",
                }
            ]
        },
        EmmentalFlagsException,
    ),
    (
        # The sum of reward of flag must be between 0 and 1
        0,
        {
            "flags": [
                {
                    "reward": 0.8,
                    "secret": "1234",
                    "text": "The secret to find is four digits",
                },
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
        0,
        {
            "flags": [
                {
                    "reward": -5,
                    "secret": "1234",
                    "text": "The secret to find is four digits",
                },
            ]
        },
        EmmentalFlagsException,
    ),
    (
        # Any reward of flags is positive
        0,
        {
            "flags": [
                {
                    "reward": -5,
                    "secret": "1234",
                    "text": "The secret to find is four digits",
                },
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
        0,
        {"hints": [{"cost": 10, "text": "What are the first four digits ?",},]},
        EmmentalHintsException,
    ),
    (
        # Sum oh cost of hint cannot exceed 1
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
        0,
        {"hints": [{"cost": -9, "text": "What are the first four digits ?",},]},
        EmmentalHintsException,
    ),
    (
        # Sum oh cost of hint cannot exceed 1
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
