import time

import pytest

from challenge_categories.model import ChallengeCategory
from challenge_categories.test_data import (
    data_challenge_category_error_title,
    data_challenge_category_error_time,
    data_challenge_category_legit_args,
    data_challenge_category_error_type,
)
from core.exceptions import (
    InconsistentDateException,
    EmptyFieldException,
    EmmentalTypeException,
)


class TestInit:
    """
    Test of the magic function __init__
    """

    def test_only_category_title(self):
        t_before = int(time.time())
        challengeCategory = ChallengeCategory(title="a")
        t_after = int(time.time())
        # assert _id is not undefined
        assert challengeCategory._id

        assert challengeCategory.title == "a"

        assert challengeCategory.created_at
        assert challengeCategory.created_at >= t_before
        assert challengeCategory.created_at <= t_after

        assert challengeCategory.updated_at
        assert challengeCategory.updated_at >= t_before
        assert challengeCategory.updated_at <= t_after

    @pytest.mark.parametrize("test_input,expected", data_challenge_category_legit_args)
    def test_category_legit_args(self, test_input, expected):
        challengeCategory = ChallengeCategory(
            _id=test_input["_id"],
            created_at=test_input["created_at"],
            updated_at=test_input["updated_at"],
            description=test_input["description"],
            title=test_input["title"],
            icon=test_input["icon"],
        )

        assert challengeCategory._id == expected["_id"]
        assert challengeCategory.created_at == expected["created_at"]
        assert challengeCategory.updated_at == expected["updated_at"]
        assert challengeCategory.title == expected["title"]
        assert challengeCategory.description == expected["description"]
        assert challengeCategory.icon == expected["icon"]

    @pytest.mark.parametrize("test_input", data_challenge_category_error_time)
    def test_error_time(self, test_input):
        with pytest.raises(InconsistentDateException):
            challengeCategory = ChallengeCategory(
                _id=test_input["_id"],
                created_at=test_input["created_at"],
                updated_at=test_input["updated_at"],
                title=test_input["title"],
                description=test_input["description"],
                icon=test_input["icon"],
            )

    @pytest.mark.parametrize("test_input", data_challenge_category_error_title)
    def test_error_title(self, test_input):
        with pytest.raises(EmptyFieldException):
            challengeCategory = ChallengeCategory(
                _id=test_input["_id"],
                created_at=test_input["created_at"],
                updated_at=test_input["updated_at"],
                title=test_input["title"],
                description=test_input["description"],
                icon=test_input["icon"],
            )

    @pytest.mark.parametrize("test_input", data_challenge_category_error_type)
    def test_error_type(self, test_input):
        with pytest.raises(EmmentalTypeException):
            challengeCategory = ChallengeCategory(
                _id=test_input["_id"],
                created_at=test_input["created_at"],
                updated_at=test_input["updated_at"],
                title=test_input["title"],
                description=test_input["description"],
                icon=test_input["icon"],
            )
