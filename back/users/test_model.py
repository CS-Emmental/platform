import time

import pytest

from users.model import User
from users.test_data import (
    data_user_legit_args,
    data_user_error,
)
from core.exceptions import (
    EmmentalTypeException,
    EmmentalEmptyFieldException,
    EmmentalDateException,
)

def get_user(test_input):
    return User(
        _id=test_input["_id"],
        username=test_input["username"],
        firstname=test_input["firstname"],
        lastname=test_input["lastname"],
        email=test_input["email"],
        password=test_input["password"],
        created_at=test_input["created_at"],
        updated_at=test_input["updated_at"],
        permissions=test_input["permissions"],
    )


class TestInit:
    """
    Test of the magic function __init__
    """
    @pytest.mark.parametrize("test_input,expected", data_user_legit_args)
    def test_user_legit_args(self, test_input, expected):
        user= User(
            username=test_input["username"],
            firstname=test_input["firstname"],
            lastname=test_input["lastname"],
            email=test_input["email"],
            password=test_input["password"]
        )
        
        assert user.username == expected["username"]
        assert user.firstname == expected["firstname"]
        assert user.lastname == expected["lastname"]
        assert user.email == expected["email"]
        assert user.password == expected["password"]

    @pytest.mark.parametrize("test_input,error_raised", data_user_error)
    def test_user_legit_args(self, test_input, error_raised):
        with pytest.raises(error_raised):
            user = get_user(test_input)