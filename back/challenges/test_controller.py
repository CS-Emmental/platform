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
from challenges.test_data import (
    data_controller_update,
    data_controller_update_errors,
    data_controller_remove,
    data_controller_insert,
)


class TestUpdateChallenge:
    """
    Test of update_challenge
    """

    app = create_app(testing=True)

    @pytest.mark.parametrize("get_manager,update_dict,expected", data_controller_update)
    def test_update_challenge(self, monkeypatch, get_manager, update_dict, expected):
        def mock_get(*args, **kwargs):
            return get_manager

        def mock_count(*args, **kwargs):
            return 0

        def mock_update_one(*args, **kwargs):
            return None

        monkeypatch.setattr(ChallengesManager, "get", mock_get)
        monkeypatch.setattr(ChallengesManager, "count", mock_count)
        monkeypatch.setattr(ChallengesManager, "update_one", mock_update_one)

        with self.app.app_context():
            updated_challenge = update_challenge("id", update_dict)

        assert updated_challenge.title == expected.title
        assert updated_challenge.title_slug == expected.title_slug
        assert updated_challenge.description == expected.description
        assert updated_challenge.summary == expected.summary
        assert updated_challenge.category_id == expected.category_id
        assert updated_challenge.total_points == expected.total_points
        assert updated_challenge.flags == expected.flags
        assert updated_challenge.hints == expected.hints
        assert updated_challenge.ports == expected.ports
        assert updated_challenge.image == expected.image
        assert updated_challenge.challenge_type == expected.challenge_type

    @pytest.mark.parametrize(
        "get_manager,count_manager,update_dict,error", data_controller_update_errors
    )
    def test_update_challenge_error(
        self, monkeypatch, get_manager, count_manager, update_dict, error
    ):
        def mock_get(*args, **kwargs):
            return get_manager

        def mock_count(*args, **kwargs):
            return count_manager

        def mock_update_one(*args, **kwargs):
            return None

        monkeypatch.setattr(ChallengesManager, "get", mock_get)
        monkeypatch.setattr(ChallengesManager, "count", mock_count)
        monkeypatch.setattr(ChallengesManager, "update_one", mock_update_one)

        with self.app.app_context():
            with pytest.raises(error):
                update_challenge("id", update_dict)


class TestRemoveChallenge:
    """
    Test of remove_challenge
    """

    app = create_app(testing=True)

    @pytest.mark.parametrize("database_input,expected", data_controller_remove)
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

    @pytest.mark.parametrize("test_input,expected", data_controller_insert)
    def test_insert_challenge(self, monkeypatch, test_input, expected):
        def mock_insert(*args, **kwargs):
            return None

        monkeypatch.setattr(ChallengesManager, "insert_one", mock_insert)

        with self.app.app_context():
            assert insert_challenge(test_input).title == expected["title"]
