from challenges.manager import ChallengeCategoriesManager, ChallengesManager
from challenges.models import ChallengeCategory
from flask import Blueprint, jsonify, request, current_app

def get_challenge_categories():
    categories = ChallengeCategoriesManager().get_all()
    return categories

def update_challenge_categories(inputs):
    current_id = inputs['category_id']
    existingCategory = ChallengeCategoriesManager().get_one(current_id)
    categorieToUpdate = ChallengeCategory(current_id,existingCategory)
    categorieToUpdate.update(inputs)
    if ChallengeCategoriesManager().update_one(categorieToUpdate.to_update_dict(),current_id):
        return str(categorieToUpdate.title) +" successfully updated"
    else:
        return "error"

def delete_challenge_categories(inputs):
    if ChallengeCategoriesManager().remove_one(inputs["category_id"]):
        return str(inputs['title']) +" successfully deleted"
    else:
        return "error"

def create_challenge_categories(inputs):
    challengeCategory = ChallengeCategory(**inputs)
    if ChallengeCategoriesManager().insert_one(challengeCategory.to_insert_dict()):
        return str(challengeCategory.title) +" successfully created"
    else:
        return "error"

def get_all_challenges():
    challenges = ChallengesManager().get_all()
    return challenges