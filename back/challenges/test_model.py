import time

import pytest

from challenges.exceptions import EmmentalFlagsException, EmmentalHintsException
from challenges.model import Challenge
from challenges.test_data import data_challenge_error, data_challenge_legit_args
from core.exceptions import (
    EmmentalTypeException,
    EmmentalEmptyFieldException,
    EmmentalDateException,
)


def get_challenge(test_input):
    return Challenge(
        _id=test_input["_id"],
        created_at=test_input["created_at"],
        updated_at=test_input["updated_at"],
        description=test_input["description"],
        title=test_input["title"],
        summary=test_input["summary"],
        hints=test_input["hints"],
        flags=test_input["flags"],
        total_points=test_input["total_points"],
        category_id=test_input["category_id"],
    )


class TestInit:
    """
    Test of the magic function __init__
    """

    def test_only_challenge_title(self):
        t_before = int(time.time())
        challenge = Challenge(title="a")
        t_after = int(time.time())
        # assert _id is not undefined
        assert challenge._id

        assert challenge.title == "a"

        assert challenge.created_at
        assert challenge.created_at >= t_before
        assert challenge.created_at <= t_after

        assert challenge.updated_at
        assert challenge.updated_at >= t_before
        assert challenge.updated_at <= t_after

    @pytest.mark.parametrize("test_input,expected", data_challenge_legit_args)
    def test_challenge_legit_args(self, test_input, expected):
        challenge = get_challenge(test_input)

        assert challenge._id == expected["_id"]
        assert challenge.created_at == expected["created_at"]
        assert challenge.updated_at == expected["updated_at"]
        assert challenge.title == expected["title"]
        assert challenge.description == expected["description"]
        assert challenge.summary == expected["summary"]
        assert challenge.hints == expected["hints"]
        assert challenge.flags == expected["flags"]
        assert challenge.category_id == expected["category_id"]

    @pytest.mark.parametrize("test_input,error_raised", data_challenge_error)
    def test_error(self, test_input, error_raised):
        with pytest.raises(error_raised):
            challenge = get_challenge(test_input)
