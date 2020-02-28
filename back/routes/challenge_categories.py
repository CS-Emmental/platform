from flask import Blueprint, jsonify, request
from flask_login import current_user, login_required

from challenge_categories.controller import (
    get_challenge_categories,
    update_challenge_category,
    remove_challenge_category,
    insert_challenge_category,
)

challenge_categories = Blueprint("challenge_categories", "challenge_categories")


@challenge_categories.route("/challenge-categories")
def get_categories():
    categories = get_challenge_categories()
    return jsonify([c.to_dict() for c in categories])


@challenge_categories.route("/challenge-categories/<challenge_category_id>", methods=["POST"])
def update_category(challenge_category_id: str):
    update_dict = request.json
    if current_user.has_permissions(["admin"]):
        updated = update_challenge_category(challenge_category_id, update_dict)
        return jsonify(updated.to_dict())
    else:
        return jsonify("unauthorized")


@challenge_categories.route("/challenge-categories/<challenge_category_id>", methods=["DELETE"])
def delete_category(challenge_category_id: str):
    if current_user.has_permissions(["admin"]):
        deleted_response = remove_challenge_category(challenge_category_id)
        return jsonify(deleted_response)
    else:
        return jsonify("unauthorized")


@challenge_categories.route("/challenge-categories", methods=["POST"])
def create_category():
    insert_dict = request.json
    if current_user.has_permissions(["admin"]):
        inserted = insert_challenge_category(insert_dict)
        return jsonify(inserted.to_dict())
    else:
        return jsonify("unauthorized")
