from core.exceptions import (
    EmmentalDateException,
    EmmentalEmptyFieldException,
    EmmentalTypeException,
)

data_challenge_category_custom_init = [
    (
        # Well typed, not realistic
        {
            "_id": "a",
            "title": "a",
            "icon": "a",
            "description": "a",
            "created_at": 0,
            "updated_at": 0,
        },
        {
            "_id": "a",
            "title": "a",
            "icon": "a",
            "description": "a",
            "created_at": 0,
            "updated_at": 0,
        },
    ),
    (
        # Realistic, created
        {
            "_id": "c853fd69-e222-4e07-a261-efe1791aa542",
            "title": "title",
            "icon": "icon",
            "description": "description",
            "created_at": 1581002681,
            "updated_at": 1581002681,
        },
        {
            "_id": "c853fd69-e222-4e07-a261-efe1791aa542",
            "title": "title",
            "icon": "icon",
            "description": "description",
            "created_at": 1581002681,
            "updated_at": 1581002681,
        },
    ),
    (
        # Realistic, updated
        {
            "_id": "c853fd69-e222-4e07-a261-efe1791aa542",
            "title": "title",
            "icon": "icon",
            "description": "description",
            "created_at": 1581002681,
            "updated_at": 2600000000,
        },
        {
            "_id": "c853fd69-e222-4e07-a261-efe1791aa542",
            "title": "title",
            "icon": "icon",
            "description": "description",
            "created_at": 1581002681,
            "updated_at": 2600000000,
        },
    ),
]


data_challenge_category_error = [
    (
        # updated_at explicitly before created_at
        {
            "_id": None,
            "title": "title",
            "icon": "icon",
            "description": "description",
            "created_at": 10,
            "updated_at": 5,
        },
        EmmentalDateException,
    ),
    (
        # updated_at implicitly before created_at
        {
            "_id": None,
            "title": "title",
            "icon": "icon",
            "description": "description",
            "created_at": None,
            "updated_at": 10,
        },
        EmmentalDateException,
    ),
    (
        # Title cannot be empty string
        {
            "_id": None,
            "title": "",
            "icon": "icon",
            "description": "description",
            "created_at": 0,
            "updated_at": 0,
        },
        EmmentalEmptyFieldException,
    ),
    (
        # title must be a string
        {
            "_id": None,
            "title": 123,
            "icon": "icon",
            "description": "description",
            "created_at": 0,
            "updated_at": 0,
        },
        EmmentalTypeException,
    ),
    (
        # icon must be a string
        {
            "_id": None,
            "title": "title",
            "icon": 156,
            "description": "description",
            "created_at": 0,
            "updated_at": 0,
        },
        EmmentalTypeException,
    ),
    (
        # description must be a string
        {
            "_id": None,
            "title": "title",
            "icon": "icon",
            "description": 798654,
            "created_at": 0,
            "updated_at": 0,
        },
        EmmentalTypeException,
    ),
]
