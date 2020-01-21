from challenges.manager import ChallengeCategoriesManager

def get_challenge_categories():
    categories = ChallengeCategoriesManager().get_all()
    return categories

def update_challenge_categories(data):
    ChallengeCategoriesManager().update_one(data)
    return get_challenge_categories()

def delete_challenge_categories(data):
    ChallengeCategoriesManager().delete_one(data)
    return get_challenge_categories()

def create_challenge_categories(data):
    ChallengeCategoriesManager().create_one(data)
    return get_challenge_categories()