from challenges.manager import ChallengeCategoriesManager, ChallengesManager, ChallengeParticipationsManager
from challenges.models import ChallengeCategory, Challenge, ChallengeParticipation
from flask_login import current_user
from flask import current_app

def get_challenge_categories():
    categories = ChallengeCategoriesManager().get_all()
    return categories

def update_challenge_category(category_id: str, inputs: dict):
    category_updated = ChallengeCategoriesManager().get(category_id)
    category_updated.update(inputs)
    try:
        ChallengeCategoriesManager().update_one(category_updated)
        return category_updated
    except Exception:
        return 'error'

def remove_challenge_category(category_id: str):
    category_deleted = ChallengeCategoriesManager().get(category_id)
    try:
        return ChallengeCategoriesManager().remove_one(category_deleted)
    except Exception:
        return 'error' 

def insert_challenge_category(inputs: dict):
    category_inserted = ChallengeCategory(**inputs)
    try:
        ChallengeCategoriesManager().insert_one(category_inserted)
        return category_inserted
    except Exception:
        return 'error'

def get_all_challenges():
    challenges = ChallengesManager().get_all()
    if current_user.is_anonymous or current_user.has_permissions(['admin']):
        for challenge in challenges:
            if challenge.hints is not None:
                for hint in challenge.hints:
                        hint['text'] = ''
    return challenges

def update_challenge(challenge_id: str, inputs: dict):
    challenge_updated = ChallengesManager().get(challenge_id)
    challenge_updated.update(inputs)
    try:
        ChallengesManager().update_one(challenge_updated)
        return challenge_updated
    except Exception:
        return 'error'

def insert_challenge(inputs: dict):
    challenge_inserted = Challenge(**inputs)
    try:
        ChallengesManager().insert_one(challenge_inserted)
        return challenge_inserted
    except Exception:
        return 'error'

def remove_challenge(challenge_id: str):
    challenge_deleted = ChallengesManager().get(challenge_id)
    try:
        return ChallengesManager().remove_one(challenge_deleted)
    except Exception:
        return 'error' 

def start_participation(options: dict):
    options['user_id'] = current_user.user_id
    new_participation = ChallengeParticipation(**options)
    ChallengeParticipationsManager().insert_one(new_participation)
    return new_participation

def get_currentuser_participations():
    currentuser_id = current_user.user_id
    participations = ChallengeParticipationsManager().get_query({'user_id': currentuser_id})
    return participations

def update_participation(participation_id: str, inputs: dict):
    participation_updated = ChallengeParticipationsManager().get(participation_id)
    participation_updated.update(inputs)
    try:
        ChallengeParticipationsManager().update_one(participation_updated)
        return participation_updated
    except Exception:
        return 'error'

def get_hints(participation_id: str, hint_indexes: list):
    participation = ChallengeParticipationsManager().get(participation_id)
    challenge = ChallengesManager().get(participation.challenge_id)
    if challenge.hints:
        if max(hint_indexes) < len(challenge.hints) and min(hint_indexes) >= 0:
            # You can't request less hints than you had before
            if set(participation.used_hints) <= set(hint_indexes):
                current_app.logger.debug('bonjour')
                participation.used_hints = hint_indexes
                ChallengeParticipationsManager().update_one(participation)
                return [ { 'index': i, 'text': challenge.hints[i]['text'] } for i in hint_indexes]  