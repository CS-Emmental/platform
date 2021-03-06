from core.exceptions import (
    EmmentalTypeException,
    EmmentalEmptyFieldException,
    EmmentalDateException,
)

data_user_legit_args = [
    (
        {
            "username": "username",
            "password": "password",
            "email": "email",
            "firstname": "firstname",
            "lastname": "lastname",
        },
        {
            "username": "username",
            "password": "password",
            "email": "email",
            "firstname": "firstname",
            "lastname": "lastname",
        },
    )
]

data_user_error = [
    (
        # updated_at_at explicitly before created_at
        {
            "_id": "_id",
            "username": "username",
            "password": "password",
            "email": "email",
            "firstname": "firstname",
            "lastname": "lastname",
            "permissions": ["admin"],
            "created_at": 10,
            "updated_at": 5,
        },
        EmmentalDateException,
    ),
    (
        # updated_at_at implicitly before created_at
        {
            "_id": "_id",
            "username": "username",
            "password": "password",
            "email": "email",
            "firstname": "firstname",
            "lastname": "lastname",
            "permissions": ["admin"],
            "created_at": None,
            "updated_at": 5,
        },
        EmmentalDateException,
    ),
    (
        # username cannot be empty
        {
            "_id": "_id",
            "username": "",
            "password": "password",
            "email": "email",
            "firstname": "firstname",
            "lastname": "lastname",
            "permissions": ["admin"],
            "created_at": None,
            "updated_at": None,
        },
        EmmentalEmptyFieldException,
    ),
    (
        # username must be a string
        {
            "_id": "_id",
            "username": 101,
            "password": "password",
            "email": "email",
            "firstname": "firstname",
            "lastname": "lastname",
            "permissions": ["admin"],
            "created_at": None,
            "updated_at": None,
        },
        EmmentalTypeException,
    ),
    (
        # password cannot be empty
        {
            "_id": "_id",
            "username": "username",
            "password": "",
            "email": "email",
            "firstname": "firstname",
            "lastname": "lastname",
            "permissions": ["admin"],
            "created_at": None,
            "updated_at": None,
        },
        EmmentalEmptyFieldException,
    ),
    (
        # password must be a string
        {
            "_id": "_id",
            "username": "username",
            "password": [""],
            "email": "email",
            "firstname": "firstname",
            "lastname": "lastname",
            "permissions": ["admin"],
            "created_at": None,
            "updated_at": None,
        },
        EmmentalTypeException,
    ),
    (
        # email cannot be empty
        {
            "_id": "_id",
            "username": "username",
            "password": "password",
            "email": "",
            "firstname": "firstname",
            "lastname": "lastname",
            "permissions": ["admin"],
            "created_at": None,
            "updated_at": None,
        },
        EmmentalEmptyFieldException,
    ),
    (
        # firstname must be a string
        {
            "_id": "_id",
            "username": "username",
            "password": "password",
            "email": ["email@email.email"],
            "firstname": 1,
            "lastname": "lastname",
            "permissions": ["admin"],
            "created_at": None,
            "updated_at": None,
        },
        EmmentalTypeException,
    ),
    (
        # lastname must be a string
        {
            "_id": "_id",
            "username": "username",
            "password": "password",
            "email": "email",
            "firstname": "firstname",
            "lastname": None,
            "permissions": ["admin"],
            "created_at": None,
            "updated_at": None,
        },
        EmmentalTypeException,
    ),
    (
        # permissions must be a list
        {
            "_id": "_id",
            "username": "username",
            "password": "password",
            "email": "email",
            "firstname": "firstname",
            "lastname": "lastname",
            "permissions": "admin",
            "created_at": None,
            "updated_at": None,
        },
        EmmentalTypeException,
    ),
]
