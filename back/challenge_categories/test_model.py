import time

import pytest

from challenge_categories.model import ChallengeCategory
from challenge_categories.test_model_data import (
    data_challenge_category_custom_init,
    data_challenge_category_error,
)
from core.exceptions import (
    EmmentalDateException,
    EmmentalEmptyFieldException,
    EmmentalTypeException,
)


def get_challenge_category(test_input):
    return ChallengeCategory(
        _id=test_input["_id"],
        created_at=test_input["created_at"],
        updated_at=test_input["updated_at"],
        description=test_input["description"],
        title=test_input["title"],
        icon=test_input["icon"],
    )


class TestInit:
    """
    Test of the magic function __init__
    """

    def test_default_init(self):
        t_before = int(time.time())
        # Title field is mandatory in ChallengeCategory object
        challengeCategory = ChallengeCategory(title="title")
        t_after = int(time.time())

        # assert _id is not undefined
        assert challengeCategory._id

        assert challengeCategory.title == "title"

        assert challengeCategory.created_at
        assert challengeCategory.created_at >= t_before
        assert challengeCategory.created_at <= t_after

        assert challengeCategory.updated_at
        assert challengeCategory.updated_at >= t_before
        assert challengeCategory.updated_at <= t_after

    @pytest.mark.parametrize("test_input,expected", data_challenge_category_custom_init)
    def test_custom_init(self, test_input, expected):
        challengeCategory = get_challenge_category(test_input)

        assert challengeCategory._id == expected["_id"]
        assert challengeCategory.created_at == expected["created_at"]
        assert challengeCategory.updated_at == expected["updated_at"]
        assert challengeCategory.title == expected["title"]
        assert challengeCategory.description == expected["description"]
        assert challengeCategory.icon == expected["icon"]

    @pytest.mark.parametrize("test_input,error_raised", data_challenge_category_error)
    def test_error(self, test_input, error_raised):
        with pytest.raises(error_raised):
            challengeCategory = get_challenge_category(test_input)
