from challenges.manager import ChallengeCategoriesManager, ChallengesManager

def get_challenge_categories():
    categories = ChallengeCategoriesManager().get_all()
    return categories

def get_all_challenges():
    challenges = ChallengesManager().get_all()
    return challenges

def update_challenge(challenge_id: str, inputs: dict):
    challenge = ChallengesManager().get(challenge_id)
    challenge.update(inputs)
    response = ChallengesManager().update_one(challenge)
    return response
