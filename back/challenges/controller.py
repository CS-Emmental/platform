from challenges.manager import ChallengeCategoriesManager, ChallengesManager
from challenges.models import ChallengeCategory
from flask import Blueprint, jsonify, request, current_app

def get_challenge_categories():
    categories = ChallengeCategoriesManager().get_all()
    return categories

def update_challenge_categories(inputs):
    existingCategory = ChallengeCategoriesManager().get_one(inputs['category_id'])
    categorieToUpdate = ChallengeCategory(inputs['category_id'],existingCategory)
    categorieToUpdate.update(inputs)
    current_app.logger.debug(categorieToUpdate.to_update_dict())
    if ChallengeCategoriesManager().update_one(categorieToUpdate.to_update_dict(),['category_id']):
        return str(categorieToUpdate.title) +" successfully updated"
    else:
        return "error"

def delete_challenge_categories(inputs):
    ChallengeCategoriesManager().delete_one(inputs["category_id"])
    return get_challenge_categories()

def create_challenge_categories(inputs):
    challengeCategory = ChallengeCategory(**inputs)
    if ChallengeCategoriesManager().insert_one(challengeCategory.to_insert_dict()):
        return str(challengeCategory.title) +" successfully created"
    else:
        return "error"

def get_all_challenges():
    challenges = ChallengesManager().get_all()
    return challenges