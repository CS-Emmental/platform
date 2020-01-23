from flask import current_app,jsonify
from uuid import uuid4
import time

class MongoManager():
    def __init__(self, collection: str):
        self.collection = current_app.mongo.db[collection]

    def get_all(self):
        return self.collection.find()

    def update_one(self,data):
        return self.collection.update({"_id":data["category_id"]},{"$set":data})

    def remove_one(self,data):
        return self.collection.remove({"_id":data["category_id"]})
    
    def insert_one(self,data):
        return self.collection.insert(data)
        