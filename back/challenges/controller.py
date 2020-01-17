from challenges.manager import ChallengeCategoriesManager, ChallengesManager

def get_challenge_categories():
    categories = ChallengeCategoriesManager().get_all()
    return categories

def get_all_challenges():
    challenges = ChallengesManager().get_all()
    return challenges