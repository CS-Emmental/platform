from flask import Blueprint, jsonify, current_app, request
from flask_login import current_user, login_required

from challenges.controller import get_challenge_categories,update_challenge_categories,delete_challenge_categories,create_challenge_categories,get_all_challenges

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
        return jsonify('error') 

@challenges.route('/challenge-categories/delete', methods=['POST'])
def delete_categories():
    if current_user.has_permissions(['admin']):
        inputs = request.json
        current_app.logger.debug(inputs)
        return delete_challenge_category(inputs)
    else :
        return jsonify('error') 

@challenges.route('/challenge-categories/create', methods=['POST'])
def create_categories():
    if current_user.has_permissions(['admin']):
        inputs = request.json
        current_app.logger.debug(inputs)
        return create_challenge_category(inputs)
    else :
        return jsonify('error')  
    
@challenges.route('/challenges')
def get_challenges():
    challenges = get_all_challenges()
    return jsonify([c.to_dict() for c in challenges])


@challenges.route('/challenges/<challenge_id>', methods=['POST'])
@login_required
def post_challenge(challenge_id: str):
    if current_user.has_permissions(['admin']):
        return jsonify(challenge_id)
    else:
        return jsonify('error')
