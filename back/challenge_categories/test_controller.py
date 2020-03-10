"""
Test of the controller of challenge Category module
"""
import pytest

from app import create_app
from challenge_categories.controller import (
    get_challenge_categories,
    insert_challenge_category,
    remove_challenge_category,
    update_challenge_category,
)
from challenge_categories.manager import ChallengeCategoriesManager
from challenge_categories.test_controller_data import (
    data_controller_get,
    data_controller_insert,
    data_controller_insert_errors,
    data_controller_remove,
    data_controller_update,
    data_controller_update_errors,
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
            get_challenge = get_challenge_categories()

        assert get_challenge.title == expected.title
        assert get_challenge.title_slug == expected.title_slug
        assert get_challenge.icon == expected.icon
        assert get_challenge.description == expected.description


class TestUpdateChallengeCategory:
    """
    Test of update_challenge_category
    """

    app = create_app(testing=True)

    @pytest.mark.parametrize(
        "get_manager,count_manager,update_fields,expected", data_controller_update
    )
    def test_update_challenge_category(
        self, monkeypatch, get_manager, count_manager, update_fields, expected
    ):
        def mock_get(*args, **kwargs):
            return get_manager

        def mock_count(*args, **kwargs):
            return count_manager

        def mock_update_one(*args, **kwargs):
            # None is acceptable since the return value is not used
            return None

        monkeypatch.setattr(ChallengeCategoriesManager, "get", mock_get)
        monkeypatch.setattr(ChallengeCategoriesManager, "count", mock_count)
        monkeypatch.setattr(ChallengeCategoriesManager, "update_one", mock_update_one)

        with self.app.app_context():
            # category_id is not used because of mocks of MongoManager -> Can be any value
            updated_category = update_challenge_category(category_id="id", inputs=update_fields)

        assert updated_category.title == expected.title
        assert updated_category.title_slug == expected.title_slug
        assert updated_category.icon == expected.icon
        assert updated_category.description == expected.description

    @pytest.mark.parametrize(
        "get_manager,count_manager,update_fields,error", data_controller_update_errors
    )
    def test_update_challenge_category_errors(
        self, monkeypatch, get_manager, count_manager, update_fields, error
    ):
        def mock_get(*args, **kwargs):
            return get_manager

        def mock_count(*args, **kwargs):
            return count_manager

        def mock_update_one(*args, **kwargs):
            # None is acceptable since the return value is not used
            return None

        monkeypatch.setattr(ChallengeCategoriesManager, "get", mock_get)
        monkeypatch.setattr(ChallengeCategoriesManager, "count", mock_count)
        monkeypatch.setattr(ChallengeCategoriesManager, "update_one", mock_update_one)

        with self.app.app_context():
            with pytest.raises(error):
                update_challenge_category("id", update_fields)


class TestRemoveChallengeCategory:
    """
    Test of remove_challenge_category
    """

    app = create_app(testing=True)

    @pytest.mark.parametrize("get_manager,remove_manager,expected", data_controller_remove)
    def test_remove_challenge_category(self, monkeypatch, get_manager, remove_manager, expected):
        def mock_get(*args, **kwargs):
            return get_manager

        def mock_remove_one(*args, **kwargs):
            return remove_manager

        monkeypatch.setattr(ChallengeCategoriesManager, "get", mock_get)
        monkeypatch.setattr(ChallengeCategoriesManager, "remove_one", mock_remove_one)

        with self.app.app_context():
            assert remove_challenge_category("id") == expected


class TestInsertChallengeCategory:
    """
    Test of insert_challenge_category
    """

    app = create_app(testing=True)

    @pytest.mark.parametrize(
        "inputs_dict,insert_one_manager,count_manager,expected", data_controller_insert
    )
    def test_insert_challenge_category(
        self, monkeypatch, inputs_dict, insert_one_manager, count_manager, expected
    ):
        def mock_insert_one(*args, **kwargs):
            return insert_one_manager

        def mock_count(*args, **kwargs):
            return count_manager

        monkeypatch.setattr(ChallengeCategoriesManager, "insert_one", mock_insert_one)
        monkeypatch.setattr(ChallengeCategoriesManager, "count", mock_count)

        with self.app.app_context():
            inserted_category = insert_challenge_category(inputs=inputs_dict)

        assert inserted_category.title == expected.title
        assert inserted_category.title_slug == expected.title_slug
        assert inserted_category.icon == expected.icon
        assert inserted_category.description == expected.description

    @pytest.mark.parametrize("inputs_dict,count_manager,error", data_controller_insert_errors)
    def test_insert_challenge_category_error(self, monkeypatch, inputs_dict, count_manager, error):
        def mock_count(*args, **kwargs):
            return count_manager

        monkeypatch.setattr(ChallengeCategoriesManager, "count", mock_count)

        with self.app.app_context():
            with pytest.raises(error):
                insert_challenge_category(inputs=inputs_dict)
