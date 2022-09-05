from functions.utils import MongoConnectionManager, build_match_query, build_geospatial_query

ITEM_PER_PAGE = 50


def build_table_sort_query(sort_parameters, geoquery=False):
    sort_fields = sort_parameters["sort_fields"][::-1]
    sort_directions = sort_parameters["sort_directions"][::-1]
    
    if geoquery:
        sort_query = list()
    else:
        sort_query = dict()
    
    for field, direction in zip(sort_fields, sort_directions):
        if geoquery:
            sort_query.append((field.upper(), int(direction)))
        else:
            sort_query[field.upper()] = int(direction)
    
    return sort_query


def use_aggregation_pipeline(uri, query_parameters, sort_parameters, page_number):
    pipeline = []
    offset = (page_number - 1) * ITEM_PER_PAGE
    
    match_query = build_match_query(query_parameters)
    pipeline.append({"$match": match_query})
    
    if sort_parameters:
        sort_query = build_table_sort_query(sort_parameters)
        pipeline.append({"$sort": sort_query})
    
    pipeline.extend([
        {"$skip": offset},
        {"$limit": ITEM_PER_PAGE},
        {"$project": {"_id": 0}}
    ])
    
    with MongoConnectionManager(uri, "realestate", "listings") as collection:
        data = list(collection.aggregate(pipeline))
    
    return data


def use_geospatial_pipeline(uri, query_parameters, sort_parameters, bbox, page_number):
    offset = (page_number - 1) * ITEM_PER_PAGE
    sort_query = None
    query = build_geospatial_query(bbox, query_parameters)
    
    if sort_parameters:
        sort_query = build_table_sort_query(sort_parameters, geo_query=True)
    
    with MongoConnectionManager(uri, "realestate", "listings") as collection:
        if sort_query:
            data = list(collection.find(query, {'_id': 0}).sort(sort_query).skip(offset).limit(50))
        else:
            data = list(collection.find(query, {'_id': 0}).skip(offset).limit(50))
    
    return data


def fetch_table_data(uri, payload):
    query_parameters = payload.get("query_parameters", {})
    sort_parameters = payload.get("sort_parameters", {})
    page_number = payload.get("page_number", 1)
    bbox = payload.get("bbox", None)
    
    if bbox:
        data = use_geospatial_pipeline(uri, query_parameters, sort_parameters, bbox, page_number)
    else:
        data = use_aggregation_pipeline(uri, query_parameters, sort_parameters, page_number)
    
    return data
