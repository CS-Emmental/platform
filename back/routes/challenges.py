from flask import Blueprint, jsonify

from challenges.controller import get_challenge_categories, get_all_challenges

challenges = Blueprint('challenges', 'challenges')

@challenges.route('/challenge-categories')
def get_categories():
    categories = get_challenge_categories()
    return jsonify([c.to_dict() for c in categories])

@challenges.route('/challenges')
def get_challenges():
    challenges = get_all_challenges()
    return jsonify([c.to_dict() for c in challenges])