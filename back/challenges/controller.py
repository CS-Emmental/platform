from challenges.manager import ChallengeCategoriesManager, ChallengesManager
from challenges.models import ChallengeCategory, Challenge

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
        return 'error'

def remove_challenge_category(category_id: str):
    category_deleted = ChallengeCategoriesManager().get(category_id)
    try:
        return ChallengeCategoriesManager().remove_one(category_deleted)
    except Exception:
        return 'error' 

def insert_challenge_category(inputs: dict):
    category_inserted = ChallengeCategory(**inputs)
    try:
        ChallengeCategoriesManager().insert_one(category_inserted)
        return category_inserted
    except Exception:
        return 'error'

def get_all_challenges():
    challenges = ChallengesManager().get_all()
    return challenges

def update_challenge(challenge_id: str, inputs: dict):
    challenge_updated = ChallengesManager().get(challenge_id)
    challenge_updated.update(inputs)
    try:
        ChallengesManager().update_one(challenge_updated)
        return challenge_updated
    except Exception:
        return 'error'

def insert_challenge(inputs: dict):
    challenge_inserted = Challenge(**inputs)
    try:
        ChallengesManager().insert_one(challenge_inserted)
        return challenge_inserted
    except Exception:
        return 'error'

def remove_challenge(challenge_id: str):
    challenge_deleted = ChallengesManager().get(challenge_id)
    try:
        return ChallengesManager().remove_one(challenge_deleted)
    except Exception:
        return 'error' 