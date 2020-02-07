data_legit_args = [
    (
        {"_id": "a", "created_at": 0, "updated_at": 0},
        {"_id": "a", "created_at": 0, "updated_at": 0},
    ),
    (
        {
            "_id": "c853fd69-e222-4e07-a261-efe1791aa542",
            "created_at": 1581002681,
            "updated_at": 1581002681,
        },
        {
            "_id": "c853fd69-e222-4e07-a261-efe1791aa542",
            "created_at": 1581002681,
            "updated_at": 1581002681,
        },
    ),
    (
        {
            "_id": "c853fd69-e222-4e07-a261-efe1791aa542",
            "created_at": 1581002681,
            "updated_at": 1681002681,
        },
        {
            "_id": "c853fd69-e222-4e07-a261-efe1791aa542",
            "created_at": 1581002681,
            "updated_at": 1681002681,
        },
    ),
]

data_error_args = [
    ({"_id": None, "created_at": 10, "updated_at": 5}),
    ({"_id": None, "created_at": None, "updated_at": 5}),
]
