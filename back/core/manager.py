from flask import current_app,jsonify
from uuid import uuid4
import time

class MongoManager():
    def __init__(self, collection: str):
        self.collection = current_app.mongo.db[collection]

    def get_all(self):
        return self.collection.find()
        
    def get(self, _id):
        return self.collection.find_one({'_id': _id})

    def update_one(self, _id, update_dict):
        return self.collection.update({'_id': _id}, {'$set': update_dict})
    
    def insert_one(self, insert_dict):
        return self.collection.insert(insert_dict)

    def remove_one(self, delete_id):
        return self.collection.remove({'_id': delete_id})
