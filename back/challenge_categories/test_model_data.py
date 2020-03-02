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

data_challenge_category_error_time = [
    (
        {
            "_id": None,
            "title": "title",
            "icon": "icon",
            "description": "description",
            "created_at": 10,
            "updated_at": 5,
        }
    ),
    (
        {
            "_id": None,
            "title": "title",
            "icon": "icon",
            "description": "description",
            "created_at": None,
            "updated_at": 10,
        }
    ),
]

data_challenge_category_error_title = [
    (
        {
            "_id": None,
            "title": "",
            "icon": "icon",
            "description": "description",
            "created_at": 0,
            "updated_at": 0,
        }
    )
]
data_challenge_category_error_type = [
    (
        {
            "_id": None,
            "title": None,
            "icon": "icon",
            "description": "description",
            "created_at": 0,
            "updated_at": 0,
        }
    ),
    (
        {
            "_id": None,
            "title": "title",
            "icon": None,
            "description": "description",
            "created_at": 0,
            "updated_at": 0,
        }
    ),
    (
        {
            "_id": None,
            "title": "title",
            "icon": "icon",
            "description": None,
            "created_at": 0,
            "updated_at": 0,
        }
    ),
    ({"_id": None, "title": 1, "icon": 1, "description": 1, "created_at": 0, "updated_at": 0,}),
]

