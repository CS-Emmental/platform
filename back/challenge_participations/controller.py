from flask_login import current_user

from challenge_participations.exceptions import EmmentalFlagSecretException
from challenge_participations.manager import ChallengeParticipationsManager
from challenge_participations.model import ChallengeParticipation
from challenges.manager import ChallengesManager
from core.exceptions import EmmentalException
from kubernetes_controller.controller import (
    deploy_challenge_instance,
    stop_challenge_instance,
)


def start_participation(options: dict):
    options["user_id"] = current_user.user_id

    new_participation = ChallengeParticipation(status="ongoing", **options)
    challenge = ChallengesManager().get(new_participation.challenge_id)

    new_participation = deploy_challenge_instance(challenge, new_participation)

    ChallengeParticipationsManager().insert_one(new_participation)
    return new_participation


def restart_participation(participation_id: str):
    participation = ChallengeParticipationsManager().get(participation_id)
    challenge = ChallengesManager().get(participation.challenge_id)

    participation = deploy_challenge_instance(challenge, participation)
    participation.status = "ongoing"

    ChallengeParticipationsManager().update_one(participation)
    return participation


def stop_participation(participation_id: str):
    participation = ChallengeParticipationsManager().get(participation_id)
    challenge = ChallengesManager().get(participation.challenge_id)

    stop_challenge_instance(challenge, participation)
    participation.status = "stopped"
    participation.port = None

    ChallengeParticipationsManager().update_one(participation)
    return participation


def get_currentuser_participations():
    currentuser_id = current_user.user_id
    participations = ChallengeParticipationsManager().get_query({"user_id": currentuser_id})
    return participations


def update_participation(participation_id: str, inputs: dict):
    participation_updated = ChallengeParticipationsManager().get(participation_id)
    participation_updated.update(inputs)
    ChallengeParticipationsManager().update_one(participation_updated)
    return participation_updated


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
            if flag_value == challenge.flags[flag_index]["secret"]:
                participation.found_flags.append(flag_index)
                ChallengeParticipationsManager().update_one(participation)
                return participation
            else:
                raise EmmentalException  # TODO
