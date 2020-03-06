from challenge_categories.manager import ChallengeCategoriesManager
from challenge_categories.model import ChallengeCategory
from core.exceptions import EmmentalNotUniqueException


def get_challenge_categories():
    categories = ChallengeCategoriesManager().get_all()
    return categories


def update_challenge_category(category_id: str, inputs: dict):
    category_manager = ChallengeCategoriesManager()

    category_to_update = category_manager.get(category_id)
    category_to_update.update(inputs)

    same_title_slug_categories = category_manager.get_query(
        {"title_slug": category_to_update.title_slug}
    )
    for challenge_category in same_title_slug_categories:
        if challenge_category.category_id != category_to_update.category_id:
            raise EmmentalNotUniqueException(error_code=26)

    category_manager.update_one(category_to_update)
    return category_to_update


def remove_challenge_category(category_id: str):
    category_deleted = ChallengeCategoriesManager().get(category_id)
    return ChallengeCategoriesManager().remove_one(category_deleted)


def insert_challenge_category(inputs: dict):
    category_inserted = ChallengeCategory(**inputs)

    ChallengeCategoriesManager().insert_one(category_inserted)
    return category_inserted
