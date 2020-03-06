from flask_login import current_user

from challenges.manager import ChallengesManager
from challenges.model import Challenge
from core.exceptions import EmmentalNotUniqueException


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
    challenge_manager = ChallengesManager()

    challenge_to_update = challenge_manager.get(challenge_id)
    challenge_to_update.update(inputs)

    same_title_slug_challenges = challenge_manager.get_query(  # list
        {
            "title_slug": challenge_to_update.title_slug,
            "category_id": challenge_to_update.category_id,
        }
    )
    for challenge in same_title_slug_challenges:
        if challenge.challenge_id != challenge_to_update.challenge_id:
            raise EmmentalNotUniqueException(error_code=28)

    challenge_manager.update_one(challenge_to_update)
    return challenge_to_update


def insert_challenge(inputs: dict):
    challenge_manager = ChallengesManager()

    challenge_to_insert = Challenge(**inputs)

    same_title_slug_challenges = challenge_manager.count(  # count
        {
            "title_slug": challenge_to_insert.title_slug,
            "category_id": challenge_to_insert.category_id,
        }
    )
    if same_title_slug_challenges != 0:
        raise EmmentalNotUniqueException(error_code=29)

    challenge_manager.insert_one(challenge_to_insert)
    return challenge_to_insert


def remove_challenge(challenge_id: str):
    challenge_deleted = ChallengesManager().get(challenge_id)
    return ChallengesManager().remove_one(challenge_deleted)
