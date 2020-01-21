from flask import current_app
from uuid import uuid4
import time

class MongoManager():
    def __init__(self, collection: str):
        self.collection = current_app.mongo.db[collection]

    def get_all(self):
        return self.collection.find()

    def update_one(self,data):
        print(data)
        self.collection.update({"_id":data["category_id"]},{"$set":data})
        return self.collection.find({"_id":data["category_id"]})

    def delete_one(self,data):
        self.collection.remove({"_id":data["category_id"]})
        return {"message":"Successfully deleted"}
    
    def insert_one(self,data):
        self.collection.insert(data)
        return self.collection.find()