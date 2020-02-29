"""
Test of the controller of challenges module
"""
import pytest
from challenges.controller import (
    get_all_challenges,
    update_challenge,
    remove_challenge,
    insert_challenge,
)
from challenges.manager import ChallengesManager
from app import create_app

class TestUpdateChallenge:
    """
    Test of update_challenge
    """

    app = create_app(testing=True)

    @pytest.mark.parametrize(
        "database_input,test_input,expected",
        [
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
        ],
    )
    def test_update_challenge(self, monkeypatch, database_input, test_input, expected):
        def mock_get(*args, **kwargs):
            return database_input

        def mock_update(*args, **kwargs):
            return None

        monkeypatch.setattr(ChallengesManager, "get", mock_get)
        monkeypatch.setattr(ChallengesManager, "update_one", mock_update)

        with self.app.app_context():
            assert update_challenge("id", test_input) == expected


class TestRemoveChallenge:
    """
    Test of remove_challenge
    """

    app = create_app(testing=True)

    @pytest.mark.parametrize(
        "database_input,expected", [({"key": "value"}, {"n": 1, "ok": 1.0})]
    )
    def test_remove_challenge(self, monkeypatch, database_input, expected):
        def mock_get(*args, **kwargs):
            return database_input

        def mock_remove(*args, **kwargs):
            return {"n": 1, "ok": 1.0}

        monkeypatch.setattr(ChallengesManager, "get", mock_get)
        monkeypatch.setattr(ChallengesManager, "remove_one", mock_remove)

        with self.app.app_context():
            assert remove_challenge("id") == expected


class TestInsertChallenge:
    """
    Test of insert_challenge
    """

    app = create_app(testing=True)

    @pytest.mark.parametrize(
        "test_input,expected", [({"title": "value"}, {"title": "value"})]
    )
    def test_insert_challenge(self, monkeypatch, test_input, expected):
        def mock_insert(*args, **kwargs):
            return None

        monkeypatch.setattr(ChallengesManager, "insert_one", mock_insert)

        with self.app.app_context():
            assert insert_challenge(test_input).title == expected["title"]
