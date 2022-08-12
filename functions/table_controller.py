from functions.utils import MongoConnectionManager, build_match_query


def fetch_table_data(uri, payload):
    match_query = build_match_query(payload)
    pipeline = [
        {"$match": match_query},
        {"$project": {"_id": 0}}
    ]
    
    with MongoConnectionManager(uri, "Dashboard", "listing_collection") as collection:
        data = dict(collection.aggregate(pipeline))
    
    return data
