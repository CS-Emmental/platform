from flask import Blueprint, jsonify, request
from flask_login import current_user, login_required

from challenges.controller import (
    get_challenge_category,
    get_all_challenges,
    update_challenge,
    insert_challenge,
    remove_challenge,
    update_challenge_category,
    remove_challenge_category,
    insert_challenge_category,
    start_participation,
    get_currentuser_participations,
    update_participation,
    get_hints,
)

challenges = Blueprint("challenges", "challenges")


@challenges.route("/challenge-categories")
def get_categories():
    categories = get_challenge_category()
    return jsonify([c.to_dict() for c in categories])


@challenges.route("/challenge-category/<challenge_category_id>", methods=["POST"])
def update_categories(challenge_category_id: str):
    update_dict = request.json
    if current_user.has_permissions(["admin"]):
        updated = update_challenge_category(challenge_category_id, update_dict)
        return jsonify(updated.to_dict())
    else:
        return jsonify("unauthorized")


@challenges.route("/challenge-category/<challenge_category_id>", methods=["DELETE"])
def delete_categories(challenge_category_id: str):
    if current_user.has_permissions(["admin"]):
        deleted_response = remove_challenge_category(challenge_category_id)
        return jsonify(deleted_response)
    else:
        return jsonify("unauthorized")


@challenges.route("/challenge-category/", methods=["POST"])
def create_categories():
    insert_dict = request.json
    if current_user.has_permissions(["admin"]):
        inserted = insert_challenge_category(insert_dict)
        return jsonify(inserted.to_dict())
    else:
        return jsonify("unauthorized")


@challenges.route("/challenges")
def get_challenges():
    challenge_list = get_all_challenges()
    return jsonify([c.to_dict() for c in challenge_list])


@challenges.route("/challenges/<challenge_id>", methods=["POST"])
@login_required
def post_challenge(challenge_id: str):
    update_dict = request.json
    if current_user.has_permissions(["admin"]):
        updated = update_challenge(challenge_id, update_dict)
        return jsonify(updated.to_dict())
    else:
        return jsonify("unauthorized")


@challenges.route("/challenges", methods=["POST"])
@login_required
def put_challenge():
    insert_dict = request.json
    if current_user.has_permissions(["admin"]):
        inserted = insert_challenge(insert_dict)
        return jsonify(inserted.to_dict())
    else:
        return jsonify("unauthorized")


@challenges.route("/challenges/<challenge_id>", methods=["DELETE"])
@login_required
def delete_challenge(challenge_id: str):
    if current_user.has_permissions(["admin"]):
        deleted_response = remove_challenge(challenge_id)
        return jsonify(deleted_response)
    else:
        return jsonify("unauthorized")


@challenges.route("/challenge-participations", methods=["POST"])
@login_required
def start_challenge_participation():
    options = request.json
    participation = start_participation(options)
    return jsonify(participation.to_dict())


@challenges.route("/challenge-participations/current-user", methods=["GET"])
@login_required
def get_current_user_participations():
    participations = get_currentuser_participations()
    return jsonify([p.to_dict() for p in participations])


@challenges.route("/challenge-participations/<participation_id>", methods=["POST"])
@login_required
def post_participation(participation_id: str):
    update_dict = request.json
    updated = update_participation(participation_id, update_dict)
    return jsonify(updated.to_dict())


@challenges.route("/challenge-participations/<participation_id>/hints", methods=["POST"])
@login_required
def use_hints(participation_id: str):
    hints_indexes = request.json
    hints = get_hints(participation_id, hints_indexes)
    return jsonify(hints)
