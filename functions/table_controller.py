from functions.utils import MongoConnectionManager


def fetch_table_data(uri):
    with MongoConnectionManager(uri, "Dashboard", "listing_collection") as collection:
        data = dict(collection.find_one({}, {"_id": 0}))
    
    return data
