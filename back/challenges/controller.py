from flask_login import current_user

from core.exceptions import EmmentalException

from challenges.manager import (
    ChallengeCategoriesManager,
    ChallengeParticipationsManager,
    ChallengesManager,
)
from challenges.models import Challenge, ChallengeCategory, ChallengeParticipation


def get_challenge_category():
    categories = ChallengeCategoriesManager().get_all()
    return categories


def update_challenge_category(category_id: str, inputs: dict):
    category_updated = ChallengeCategoriesManager().get(category_id)
    category_updated.update(inputs)
    try:
        ChallengeCategoriesManager().update_one(category_updated)
        return category_updated
    except Exception:
        return "error"


def remove_challenge_category(category_id: str):
    category_deleted = ChallengeCategoriesManager().get(category_id)
    try:
        return ChallengeCategoriesManager().remove_one(category_deleted)
    except Exception:
        return "error"


def insert_challenge_category(inputs: dict):
    category_inserted = ChallengeCategory(**inputs)
    try:
        ChallengeCategoriesManager().insert_one(category_inserted)
        return category_inserted
    except Exception:
        return "error"


def get_all_challenges():
    challenges = ChallengesManager().get_all()
    if current_user.is_anonymous or not current_user.has_permissions(["admin"]):
        for challenge in challenges:
            for flag in challenge.flags:
                flag["value"] = ""
            if challenge.hints is not None:
                for hint in challenge.hints:
                    hint["text"] = ""
    return challenges


def update_challenge(challenge_id: str, inputs: dict):
    challenge_updated = ChallengesManager().get(challenge_id)
    challenge_updated.update(inputs)
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


def start_participation(options: dict):
    options["user_id"] = current_user.user_id
    new_participation = ChallengeParticipation(**options)
    ChallengeParticipationsManager().insert_one(new_participation)
    return new_participation


def get_currentuser_participations():
    currentuser_id = current_user.user_id
    participations = ChallengeParticipationsManager().get_query({"user_id": currentuser_id})
    return participations


def update_participation(participation_id: str, inputs: dict):
    participation_updated = ChallengeParticipationsManager().get(participation_id)
    participation_updated.update(inputs)
    try:
        ChallengeParticipationsManager().update_one(participation_updated)
        return participation_updated
    except Exception:
        return "error"


def get_hints(participation_id: str, hint_indexes: list):
    participation = ChallengeParticipationsManager().get(participation_id)
    challenge = ChallengesManager().get(participation.challenge_id)
    if challenge.hints:
        if max(hint_indexes) < len(challenge.hints) and min(hint_indexes) >= 0:
            # You can't request less hints than you had before
            if set(participation.used_hints) <= set(hint_indexes):
                participation.used_hints = hint_indexes
                ChallengeParticipationsManager().update_one(participation)
                return [{"index": i, "text": challenge.hints[i]["text"]} for i in hint_indexes]

def validate_flag(participation_id: str, flag_index: int, flag_value: str):
    participation = ChallengeParticipationsManager().get(participation_id)
    challenge = ChallengesManager().get(participation.challenge_id)
    if flag_index < len(challenge.flags):
        if flag_index not in participation.found_flags:
            if flag_value == challenge.flags[flag_index]["value"]:
                participation.found_flags.append(flag_index)
                ChallengeParticipationsManager().update_one(participation)
                return participation
            else:
                raise EmmentalException # todo
