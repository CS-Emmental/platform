from challenges.manager import ChallengeCategoriesManager, ChallengesManager
from challenges.models import ChallengeCategory, Challenge

def get_challenge_categories():
    categories = ChallengeCategoriesManager().get_all()
    return categories

def update_challenge_category(inputs):
    current_id = inputs['category_id']
    existingCategory = ChallengeCategoriesManager().get_one(current_id)
    categorieToUpdate = ChallengeCategory(current_id,existingCategory)
    categorieToUpdate.update(inputs)
    if ChallengeCategoriesManager().update_one(categorieToUpdate.to_update_dict(),current_id):
        return str(categorieToUpdate.title) +" successfully updated"
    else:
        return "error"

def delete_challenge_category(inputs):
    if ChallengeCategoriesManager().remove_one(inputs["category_id"]):
        return str(inputs['title']) +" successfully deleted"
    else:
        return "error"

def create_challenge_category(inputs):
    challengeCategory = ChallengeCategory(**inputs)
    if ChallengeCategoriesManager().insert_one(challengeCategory.to_insert_dict()):
        return str(challengeCategory.title) +" successfully created"
    else:
        return "error"

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