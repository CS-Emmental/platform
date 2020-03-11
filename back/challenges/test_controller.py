"""
Test of the controller of challenges module
"""
import pytest

from app import create_app
from challenges.controller import (
    insert_challenge,
    remove_challenge,
    update_challenge,
)
from challenges.manager import ChallengeManager
from challenges.test_controller_data import (
    data_controller_insert,
    data_controller_insert_errors,
    data_controller_remove,
    data_controller_update,
    data_controller_update_errors,
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

        monkeypatch.setattr(ChallengeManager, "get", mock_get)
        monkeypatch.setattr(ChallengeManager, "count", mock_count)
        monkeypatch.setattr(ChallengeManager, "update_one", mock_update_one)

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

        monkeypatch.setattr(ChallengeManager, "get", mock_get)
        monkeypatch.setattr(ChallengeManager, "count", mock_count)
        monkeypatch.setattr(ChallengeManager, "update_one", mock_update_one)

        with self.app.app_context():
            with pytest.raises(error):
                update_challenge("id", update_dict)


class TestRemoveChallenge:
    """
    Test of remove_challenge
    """

    app = create_app(testing=True)

    @pytest.mark.parametrize(
        "get_manager,remove_manager,expected", data_controller_remove
    )
    def test_remove_challenge(self, monkeypatch, get_manager, remove_manager, expected):
        def mock_get(*args, **kwargs):
            return get_manager

        def mock_remove_one(*args, **kwargs):
            return remove_manager

        monkeypatch.setattr(ChallengeManager, "get", mock_get)
        monkeypatch.setattr(ChallengeManager, "remove_one", mock_remove_one)

        with self.app.app_context():
            assert remove_challenge("id") == expected


class TestInsertChallenge:
    """
    Test of insert_challenge
    """

    app = create_app(testing=True)

    @pytest.mark.parametrize(
        "inputs_dict,insert_one_manager,count_manager,expected", data_controller_insert
    )
    def test_insert_challenge(
        self, monkeypatch, inputs_dict, insert_one_manager, count_manager, expected
    ):
        def mock_insert_one(*args, **kwargs):
            return insert_one_manager

        def mock_count(*args, **kwargs):
            return count_manager

        monkeypatch.setattr(ChallengeManager, "insert_one", mock_insert_one)
        monkeypatch.setattr(ChallengeManager, "count", mock_count)

        with self.app.app_context():
            inserted_challenge = insert_challenge(inputs=inputs_dict)

        assert inserted_challenge.title == expected.title
        assert inserted_challenge.title_slug == expected.title_slug
        assert inserted_challenge.description == expected.description
        assert inserted_challenge.summary == expected.summary
        assert inserted_challenge.category_id == expected.category_id
        assert inserted_challenge.total_points == expected.total_points
        assert inserted_challenge.flags == expected.flags
        assert inserted_challenge.hints == expected.hints
        assert inserted_challenge.ports == expected.ports
        assert inserted_challenge.image == expected.image
        assert inserted_challenge.challenge_type == expected.challenge_type

    @pytest.mark.parametrize(
        "count_manager,inputs_dict,error", data_controller_insert_errors
    )
    def test_insert_challenge_error(
        self, monkeypatch, count_manager, inputs_dict, error
    ):
        def mock_count(*args, **kwargs):
            return count_manager

        monkeypatch.setattr(ChallengeManager, "count", mock_count)

        with self.app.app_context():
            with pytest.raises(error):
                insert_challenge(inputs=inputs_dict)
