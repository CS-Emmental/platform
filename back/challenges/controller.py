from challenges.manager import ChallengeCategoriesManager, ChallengesManager
from challenges.models import Challenge

def get_challenge_categories():
    categories = ChallengeCategoriesManager().get_all()
    return categories

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