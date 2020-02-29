"""
Test of the controller of challenge Category module
"""
import pytest
from challenge_categories.controller import (
    get_challenge_categories,
    update_challenge_category,
    remove_challenge_category,
    insert_challenge_category,
)
from challenge_categories.manager import ChallengeCategoriesManager
from app import create_app
from challenge_categories.test_data import (
    data_controller_get,
    data_controller_update,
    data_controller_remove,
    data_controller_insert,
)


class TestGetChallengeCategories:
    """
    Test of get_challenge_categories
    """

    # Most managers inherit from MongoManager which uses the app_context.
    app = create_app(testing=True)

    @pytest.mark.parametrize("test_input,expected", data_controller_get)
    def test_get_challenge_categories(self, monkeypatch, test_input, expected):
        """
        Test if the function well returns what the ChallengeCategoriesManager returns
        """

        def mock_get_all(*args, **kwargs):
            return test_input

        monkeypatch.setattr(ChallengeCategoriesManager, "get_all", mock_get_all)

        with self.app.app_context():
            assert get_challenge_categories() == expected


class TestUpdateChallengeCategory:
    """
    Test of update_challenge_category
    """

    app = create_app(testing=True)

    @pytest.mark.parametrize(
        "database_input,test_input,expected", data_controller_update
    )
    def test_update_challenge_category(
        self, monkeypatch, database_input, test_input, expected
    ):
        def mock_get(*args, **kwargs):
            return database_input

        def mock_update(*args, **kwargs):
            return None

        monkeypatch.setattr(ChallengeCategoriesManager, "get", mock_get)
        monkeypatch.setattr(ChallengeCategoriesManager, "update_one", mock_update)

        with self.app.app_context():
            assert update_challenge_category("id", test_input) == expected


class TestRemoveChallengeCategory:
    """
    Test of remove_challenge_category
    """

    app = create_app(testing=True)

    @pytest.mark.parametrize("database_input,expected", data_controller_remove)
    def test_remove_challenge_category(self, monkeypatch, database_input, expected):
        def mock_get(*args, **kwargs):
            return database_input

        def mock_remove(*args, **kwargs):
            return {"n": 1, "ok": 1.0}

        monkeypatch.setattr(ChallengeCategoriesManager, "get", mock_get)
        monkeypatch.setattr(ChallengeCategoriesManager, "remove_one", mock_remove)

        with self.app.app_context():
            assert remove_challenge_category("id") == expected


class TestInsertChallengeCategory:
    """
    Test of insert_challenge_category
    """

    app = create_app(testing=True)

    @pytest.mark.parametrize("test_input,expected", data_controller_insert)
    def test_insert_challenge_category(self, monkeypatch, test_input, expected):
        def mock_insert(*args, **kwargs):
            return None

        monkeypatch.setattr(ChallengeCategoriesManager, "insert_one", mock_insert)

        with self.app.app_context():
            assert insert_challenge_category(test_input).title == expected["title"]
