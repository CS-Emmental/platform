from flask import Blueprint, jsonify

from challenges.controller import get_challenge_categories

challenges = Blueprint('challenges', 'challenges')

@challenges.route('/challenge-categories')
def get_categories():
    categories = get_challenge_categories()
    return jsonify([c.to_dict() for c in categories])
