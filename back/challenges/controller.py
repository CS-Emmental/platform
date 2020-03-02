from flask_login import current_user

from challenges.manager import ChallengesManager
from challenges.model import Challenge


def get_all_challenges():
    challenges = ChallengesManager().get_all()
    if current_user.is_anonymous or not current_user.has_permissions(["admin"]):
        for challenge in challenges:
            for flag in challenge.flags:
                flag["secret"] = ""
            if challenge.hints is not None:
                for hint in challenge.hints:
                    hint["text"] = ""
    return challenges


def update_challenge(challenge_id: str, inputs: dict):
    challenge_updated = ChallengesManager().get(challenge_id)
    challenge_updated.update(inputs)

    # Do not forget to check if the object is correct after any update
    challenge_updated.verify()
    try:
        ChallengesManager().update_one(challenge_updated)
        return challenge_updated
    except Exception:
        return "error"


def insert_challenge(inputs: dict):
    challenge_inserted = Challenge(**inputs)
    try:
        ChallengesManager().insert_one(challenge_inserted)
        return challenge_inserted
    except Exception:
        return "error"


def remove_challenge(challenge_id: str):
    challenge_deleted = ChallengesManager().get(challenge_id)
    try:
        return ChallengesManager().remove_one(challenge_deleted)
    except Exception:
        return "error"
