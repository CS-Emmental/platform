from flask import Blueprint, jsonify, request, current_app

from challenges.controller import get_challenge_categories,update_challenge_categories

challenges = Blueprint('challenges', 'challenges')

@challenges.route('/challenge-categories')
def get_categories():
    categories = get_challenge_categories()
    return jsonify([c.to_dict() for c in categories])

@challenges.route('/challenge-categories/update', methods=['POST'])
def update_categories():
    inputs = request.json
    current_app.logger.debug(inputs)
    categories_updated = update_challenge_categories(inputs)
    return jsonify([c.to_dict() for c in categories_updated])
