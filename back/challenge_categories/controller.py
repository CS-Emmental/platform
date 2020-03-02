from challenge_categories.manager import ChallengeCategoriesManager
from challenge_categories.model import ChallengeCategory


def get_challenge_categories():
    categories = ChallengeCategoriesManager().get_all()
    return categories


def update_challenge_category(category_id: str, inputs: dict):
    category_updated = ChallengeCategoriesManager().get(category_id)
    category_updated.update(inputs)
    ChallengeCategoriesManager().update_one(category_updated)
    return category_updated


def remove_challenge_category(category_id: str):
    category_deleted = ChallengeCategoriesManager().get(category_id)
    return ChallengeCategoriesManager().remove_one(category_deleted)


def insert_challenge_category(inputs: dict):
    category_inserted = ChallengeCategory(**inputs)

    ChallengeCategoriesManager().insert_one(category_inserted)
    return category_inserted
