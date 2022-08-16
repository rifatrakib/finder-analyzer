from functions.utils import MongoConnectionManager, build_match_query

ITEM_PER_PAGE = 50


def table_sort_query(sort_parameters):
    sort_fields = sort_parameters["sort_fields"][::-1]
    sort_directions = sort_parameters["sort_directions"][::-1]
    
    sort_query = {}
    for field, direction in zip(sort_fields, sort_directions):
        sort_query[field.upper()] = int(direction)
    
    return sort_query


def fetch_table_data(uri, payload):
    query_parameters = payload.get("query_parameters", {})
    sort_parameters = payload.get("sort_parameters", {})
    page_number = payload.get("page_number", 1)
    
    match_query = build_match_query(query_parameters)
    sort_query = table_sort_query(sort_parameters)
    offset = (page_number - 1) * ITEM_PER_PAGE
    
    pipeline = [
        {"$match": match_query},
        {"$sort": sort_query},
        {"$skip": offset},
        {"$limit": ITEM_PER_PAGE},
        {"$project": {"_id": 0}}
    ]
    
    with MongoConnectionManager(uri, "Dashboard", "listing_collection") as collection:
        data = dict(collection.aggregate(pipeline))
    
    return data
