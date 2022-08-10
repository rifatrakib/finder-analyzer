from pymongo import MongoClient
import certifi


class MongoConnectionManager():
    def __init__(self, uri, database, collection):
        self.client = MongoClient(uri, tlsCAFile=certifi.where())
        self.database = database
        self.collection = collection
    
    def __enter__(self):
        self.database = self.client[self.database]
        self.collection = self.database[self.collection]
        return self.collection
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.client.close()
