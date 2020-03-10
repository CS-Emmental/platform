from challenge_categories.model import ChallengeCategory
from core.exceptions import EmmentalNotUniqueException


data_controller_get = [
    (ChallengeCategory(_id="id", title="title"), ChallengeCategory(_id="id", title="title")),
    (
        ChallengeCategory(_id="id", title="title", description="Lorem ipsum dolor sit amet."),
        ChallengeCategory(_id="id", title="title", description="Lorem ipsum dolor sit amet."),
    ),
]

data_controller_update = [
    (
        # Simplest example
        ChallengeCategory(_id="const_id", title="old_title"),
        0,
        {"title": "new_title"},
        ChallengeCategory(_id="const_id", title="new_title"),
    ),
    (
        # More complete example
        ChallengeCategory(_id="const_id", title="old title"),
        0,
        {"title": "Brand new title 1", "icon": "another_icon", "description": "lalalalala"},
        ChallengeCategory(
            _id="const_id",
            title="Brand new title 1",
            icon="another_icon",
            title_slug="brand-new-title-1",
            description="lalalalala",
        ),
    ),
]

data_controller_update_errors = [
    (
        # Another category will have the same title after update
        ChallengeCategory(_id="const_id", title="old_title"),
        1,  # here
        {"title": "new_title"},
        EmmentalNotUniqueException,
    ),
    (
        # Another categories will have the same title after update
        ChallengeCategory(_id="const_id", title="old_title"),
        10,  # here
        {"title": "new_title"},
        EmmentalNotUniqueException,
    ),
]

data_controller_remove = [
    # Very simple test with dummy test data. To improve when the function tested becomes more complex
    (ChallengeCategory(_id="id", title="title"), {"n": 1, "ok": 1.0}, {"n": 1, "ok": 1.0})
]

data_controller_insert = [({"title": "value"}, {"title": "value"})]
