from flask import current_app

class MongoManager():
    def __init__(self, collection: str):
        self.collection = current_app.mongo.db[collection]

    def get_all(self):
        return self.collection.find()