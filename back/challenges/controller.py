from challenges.manager import ChallengeCategoriesManager

def get_challenge_categories():
    categories = ChallengeCategoriesManager().get_all()
    return categories