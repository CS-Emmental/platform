from challenges.manager import ChallengeCategoriesManager, ChallengesManager
from challenges.models import ChallengeCategory
from flask import Blueprint, jsonify, request, current_app


def get_challenge_categories():
    categories = ChallengeCategoriesManager().get_all()
    return categories

def update_challenge_categories(inputs):
    if ChallengeCategoriesManager().update_one(inputs):
        return str(challengeCategory.title) +" successfully updated"
    else:
        return "error"

def delete_challenge_categories(inputs):
    ChallengeCategoriesManager().delete_one(inputs)
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