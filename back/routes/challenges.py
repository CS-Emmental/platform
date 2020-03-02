from flask import Blueprint, jsonify, request
from flask_login import current_user, login_required

from challenges.controller import (
    get_all_challenges,
    insert_challenge,
    remove_challenge,
    update_challenge,
)
from users.exceptions import BadPermissionException

challenges = Blueprint("challenges", "challenges")


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
        raise BadPermissionException(error_code=22)


@challenges.route("/challenges", methods=["POST"])
@login_required
def put_challenge():
    insert_dict = request.json
    if current_user.has_permissions(["admin"]):
        inserted = insert_challenge(insert_dict)
        return jsonify(inserted.to_dict())
    else:
        raise BadPermissionException(error_code=23)


@challenges.route("/challenges/<challenge_id>", methods=["DELETE"])
@login_required
def delete_challenge(challenge_id: str):
    if current_user.has_permissions(["admin"]):
        deleted_response = remove_challenge(challenge_id)
        return jsonify(deleted_response)
    else:
        raise BadPermissionException(error_code=24)
