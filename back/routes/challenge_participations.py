from flask import Blueprint, jsonify, request
from flask_login import current_user, login_required

from challenge_participations.controller import (
    start_participation,
    get_currentuser_participations,
    update_participation,
    get_hints,
    validate_flag,
    stop_participation,
)

challenge_participations = Blueprint("challenge_participations", "challenge_participations")


@challenge_participations.route("/challenge-participations", methods=["POST"])
@login_required
def start_challenge_participation():
    options = request.json
    participation = start_participation(options)
    return jsonify(participation.to_dict())


@challenge_participations.route("/challenge-participations/current-user", methods=["GET"])
@login_required
def get_current_user_participations():
    participations = get_currentuser_participations()
    return jsonify([p.to_dict() for p in participations])


@challenge_participations.route("/challenge-participations/<participation_id>", methods=["POST"])
@login_required
def post_participation(participation_id: str):
    update_dict = request.json
    updated = update_participation(participation_id, update_dict)
    return jsonify(updated.to_dict())

@challenge_participations.route("/challenge-participations/<participation_id>/stop-instance", methods=["POST"])
@login_required
def stop_challenge_participation(participation_id: str):
    res = stop_participation(participation_id)
    return jsonify(res.to_dict())

@challenge_participations.route("/challenge-participations/<participation_id>/hints", methods=["POST"])
@login_required
def use_hints(participation_id: str):
    hints_indexes = request.json
    hints = get_hints(participation_id, hints_indexes)
    return jsonify(hints)

@challenge_participations.route("/challenge-participations/<participation_id>/flags", methods=["POST"])
@login_required
def post_flag(participation_id: str):
    flag = request.json
    participation = validate_flag(participation_id, flag["index"], flag["secret"])
    return jsonify(participation.to_dict())