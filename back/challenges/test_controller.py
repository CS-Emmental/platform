"""
Test of the controller of challenges module
"""
import pytest
from challenges.controller import get_challenge_category
from challenges.manager import ChallengeCategoriesManager
from app import create_app


class TestGetChallengeCategory:
    """
    Test of get_challenge_category
    """

    # Most managers inherit from MongoManager which uses the app_context.
    app = create_app()

    @pytest.mark.parametrize(
        "test_input,expected", [([], []), ([1], [1]), (["", "string_test"], ["", "string_test"])]
    )
    def test_get_challenge_category(self, monkeypatch, test_input, expected):
        """
        Test if the function well returns what the ChallengeCategoriesManager returns
        """

        def mock_get_all(*args, **kwargs):
            return test_input

        monkeypatch.setattr(ChallengeCategoriesManager, "get_all", mock_get_all)

        with self.app.app_context():
            assert get_challenge_category() == expected
