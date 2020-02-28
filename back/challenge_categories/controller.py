from challenge_categories.manager import ChallengeCategoriesManager
from challenge_categories.model import ChallengeCategory

def get_challenge_categories():
    categories = ChallengeCategoriesManager().get_all()
    return categories


def update_challenge_category(category_id: str, inputs: dict):
    category_updated = ChallengeCategoriesManager().get(category_id)
    category_updated.update(inputs)
    try:
        ChallengeCategoriesManager().update_one(category_updated)
        return category_updated
    except Exception:
        return "error"


def remove_challenge_category(category_id: str):
    category_deleted = ChallengeCategoriesManager().get(category_id)
    try:
        return ChallengeCategoriesManager().remove_one(category_deleted)
    except Exception:
        return "error"


def insert_challenge_category(inputs: dict):
    category_inserted = ChallengeCategory(**inputs)
    try:
        ChallengeCategoriesManager().insert_one(category_inserted)
        return category_inserted
    except Exception:
        return "error"