from flask import Blueprint, jsonify
from challenge_groups.model import ChallengeGroup

challenge_groups = Blueprint('challenge_groups', 'challenge_groups')

@challenge_groups.route('/')
def get_challenge_groups():
    groups = ChallengeGroup.objects.all()
    return jsonify(groups)
