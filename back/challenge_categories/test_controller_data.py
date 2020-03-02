data_controller_update = [
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

data_controller_remove = [({"key": "value"}, {"n": 1, "ok": 1.0})]
data_controller_insert = [({"title": "value"}, {"title": "value"})]
data_controller_get = [([], []), ([1], [1]), (["", "string_test"], ["", "string_test"])]
