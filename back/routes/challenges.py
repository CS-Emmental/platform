from flask import Blueprint, jsonify
from challenges.models import ChallengeCategory

challenges = Blueprint('challenges', 'challenges')

@challenges.route('/challenge-categories')
def get_challenge_categories():
    groups = ChallengeCategory.objects.all()
    return jsonify(groups)
