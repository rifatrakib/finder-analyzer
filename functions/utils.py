from pymongo import MongoClient


class MongoConnectionManager():
    def __init__(self, uri, database, collection):
        self.client = MongoClient(uri)
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
        if not value:
            continue
        
        field_name = key.upper()
        if isinstance(value, list):
            match_query[field_name] = {"$in": value}
        elif isinstance(value, dict):
            match_query[field_name] = {
                "$gte": float(value["min"]),
                "$lte": float(value["max"])
            }
    
    return match_query
