from flask import Blueprint, jsonify, current_app, request
from flask_login import current_user, login_required

from challenges.controller import get_challenge_categories,update_challenge_categories,delete_challenge_categories,create_challenge_categories,get_all_challenges
from challenges.controller import get_challenge_categories, get_all_challenges, update_challenge, insert_challenge, remove_challenge

challenges = Blueprint('challenges', 'challenges')

@challenges.route('/challenge-categories')
def get_categories():
    categories = get_challenge_categories()
    return jsonify([c.to_dict() for c in categories])

@challenges.route('/challenge-categories/update', methods=['POST'])
def update_categories():
    if current_user.has_permissions(['admin']):
        inputs = request.json
        current_app.logger.debug(inputs)
        return update_challenge_category(inputs)
    else :
        return jsonify('unauthorized')

@challenges.route('/challenge-categories/delete', methods=['POST'])
def delete_categories():
    if current_user.has_permissions(['admin']):
        inputs = request.json
        current_app.logger.debug(inputs)
        return delete_challenge_category(inputs)
    else :
        return jsonify('unauthorized')

@challenges.route('/challenge-categories/create', methods=['POST'])
def create_categories():
    if current_user.has_permissions(['admin']):
        inputs = request.json
        current_app.logger.debug(inputs)
        return create_challenge_category(inputs)
    else :
        return jsonify('unauthorized')
    
@challenges.route('/challenges')
def get_challenges():
    challenges = get_all_challenges()
    return jsonify([c.to_dict() for c in challenges])


@challenges.route('/challenges/<challenge_id>', methods=['POST'])
@login_required
def post_challenge(challenge_id: str):
    update_dict = request.json
    if current_user.has_permissions(['admin']):
        updated = update_challenge(challenge_id, update_dict)
        return jsonify(updated.to_dict())
    else:
        return jsonify('unauthorized')

@challenges.route('/challenges', methods=['POST'])
@login_required
def put_challenge():
    insert_dict = request.json
    if current_user.has_permissions(['admin']):
        inserted = insert_challenge(insert_dict)
        return jsonify(inserted.to_dict())
    else:
        return jsonify('unauthorized')

@challenges.route('/challenges/<challenge_id>', methods=['DELETE'])
@login_required
def delete_challenge(challenge_id: str):
    if current_user.has_permissions(['admin']):
        deleted_response = remove_challenge(challenge_id)
        return jsonify(deleted_response)
    else:
        return jsonify('unauthorized')
