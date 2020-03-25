import time
from flask import current_app
from flask_login import current_user
from challenge_participations.exceptions import EmmentalFlagSecretException
from challenge_participations.manager import ChallengeParticipationManager
from challenge_participations.model import ChallengeParticipation
from challenges.manager import ChallengeManager
from core.exceptions import EmmentalException
from kubernetes_controller.controller import (
    deploy_challenge_instance,
    stop_challenge_instance,
)


def start_participation(options: dict):
    options["user_id"] = current_user.user_id

    new_participation = ChallengeParticipation(status="ongoing", **options)
    challenge = ChallengeManager().get(new_participation.challenge_id)

    new_participation.port = deploy_challenge_instance(
        challenge_id=challenge.challenge_id,
        challenge_title=challenge.title,
        participation_id=new_participation.participation_id,
        containers=challenge.containers,
    )
    new_participation.started_at = int(time.time())

    ChallengeParticipationManager().insert_one(new_participation)
    return new_participation


def restart_participation(participation_id: str):
    participation = ChallengeParticipationManager().get(participation_id)
    challenge = ChallengeManager().get(participation.challenge_id)

    participation.port = deploy_challenge_instance(
        challenge_id=challenge.challenge_id,
        challenge_title=challenge.title,
        participation_id=participation.participation_id,
        containers=challenge.containers,
    )
    participation.status = "ongoing"
    participation.started_at = int(time.time())

    ChallengeParticipationManager().update_one(participation)
    return participation


def stop_participation(participation_id: str):
    participation = ChallengeParticipationManager().get(participation_id)
    challenge = ChallengeManager().get(participation.challenge_id)

    stop_challenge_instance(
        challenge_title=challenge.title,
        participation_id=participation.participation_id
        )
    participation.status = "stopped"
    participation.port = None

    ChallengeParticipationManager().update_one(participation)
    return participation


def stop_old_participations():
    old_timediff = current_app.config["INSTANCE_TIME_TO_LIVE_HOURS"] * 3600
    old_threshold = int(time.time()) - old_timediff
    old_participations = ChallengeParticipationManager().get_query(
        {"status": "ongoing", "started_at": {"$lte": old_threshold, }, }
    )
    for participation in old_participations:
        stop_participation(participation.participation_id)
    current_app.logger.info(
        "Stopped following old instances : {}".format(
            [participation.participation_id for participation in old_participations]
        )
    )


def get_currentuser_participations():
    currentuser_id = current_user.user_id
    participations = ChallengeParticipationManager().get_query(
        {"user_id": currentuser_id}
    )
    return participations


def update_participation(participation_id: str, inputs: dict):
    participation_updated = ChallengeParticipationManager().get(participation_id)
    participation_updated.update(inputs)
    ChallengeParticipationManager().update_one(participation_updated)
    return participation_updated


def get_hints(participation_id: str, hint_indexes: list):
    participation = ChallengeParticipationManager().get(participation_id)
    challenge = ChallengeManager().get(participation.challenge_id)
    if participation.status in ["ongoing", "stopped"]:
        if challenge.hints:
            if max(hint_indexes) < len(challenge.hints) and min(hint_indexes) >= 0:
                # You can't request less hints than you had before
                if set(participation.used_hints) <= set(hint_indexes):
                    participation.used_hints = hint_indexes
                    ChallengeParticipationManager().update_one(participation)
                    return [
                        {"index": i, "text": challenge.hints[i]["text"]}
                        for i in hint_indexes
                    ]
    raise EmmentalException  # TODO


def validate_flag(participation_id: str, flag_index: int, flag_value: str):
    participation = ChallengeParticipationManager().get(participation_id)
    challenge = ChallengeManager().get(participation.challenge_id)
    if flag_index < len(challenge.flags):
        if flag_index not in participation.found_flags:
            if flag_value == challenge.flags[flag_index]["secret"]:
                participation.found_flags.append(flag_index)
            else:
                raise EmmentalException  # TODO

    # Finish challenge if all flags are validated
    if len(participation.found_flags) == len(challenge.flags):
        if participation.status == "ongoing":
            stop_challenge_instance(
                challenge_title=challenge.title,
                participation_id=participation.participation_id
                )
        participation.port = None
        participation.status = "finished"

    ChallengeParticipationManager().update_one(participation)
    return participation
