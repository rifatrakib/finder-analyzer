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


def build_match_query(query_parameters):
    match_query = {}
    
    for key, value in query_parameters.items():
        field_name = key.upper()
        if type(value) == list:
            match_query[field_name] = {"$in": value}
        else:
            match_query[field_name] = {
                "$gte": float(value["min"]),
                "$lte": float(value["max"])
            }
    
    return match_query
