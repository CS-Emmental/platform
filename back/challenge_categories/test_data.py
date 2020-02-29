data_challenge_category_legit_args = [
    (
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
        {
            "_id": "c853fd69-e222-4e07-a261-efe1791aa542",
            "title": "title",
            "icon": "icon",
            "description": "description",
            "created_at": 1581002681,
            "updated_at": 1681002681,
        },
        {
            "_id": "c853fd69-e222-4e07-a261-efe1791aa542",
            "title": "title",
            "icon": "icon",
            "description": "description",
            "created_at": 1581002681,
            "updated_at": 1681002681,
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
    ),
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

data_controller_update=[
            ({"key": "value"}, {"key": "new_value"}, {"key": "new_value"}),
            ({"key": "value"}, {}, {"key": "value"}),
            (
                {"key1": "value1", "key2": "value2"},
                {"key1": "new_value1", "key2": "value2"},
                {"key1": "new_value1", "key2": "value2"},
            ),
            (
                {"key1": "value1", "key2": "value2"},
                {"key1": "new_value1"},
                {"key1": "new_value1", "key2": "value2"},
            ),
            (
                {"key1": "value1", "key2": "value2"},
                {"key1": "new_value1", "key2": "new_value2"},
                {"key1": "new_value1", "key2": "new_value2"},
            ),
        ]

data_controller_remove=[({"key": "value"}, {"n": 1, "ok": 1.0})]
data_controller_insert=[({"title": "value"}, {"title": "value"})]
data_controller_get=[([], []), ([1], [1]), (["", "string_test"], ["", "string_test"])]