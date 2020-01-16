from challenges.manager import ChallengeCategoriesManager

def get_challenge_categories():
    categories = ChallengeCategoriesManager().get_all()
    return categories

def update_challenge_categories(data):
    ChallengeCategoriesManager().update_one(data)
    return get_challenge_categories()