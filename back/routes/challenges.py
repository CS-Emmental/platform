from flask import Blueprint, jsonify, current_app
# from challenges.models import ChallengeCategory

challenges = Blueprint('challenges', 'challenges')

@challenges.route('/challenge-categories')
def get_challenge_categories():
    groups = list(current_app.mongo.db.challenge_categories.find())
    return jsonify(groups)
