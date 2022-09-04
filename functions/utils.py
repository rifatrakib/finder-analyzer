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


def restructure_polygon_data(geometry):
    restructured_polygon = {
        "type": geometry["type"],
        "coordinates": [[
            list(coordinate)\
                for box in geometry["coordinates"]\
                for coordinate in box
        ]]
    }
    return restructured_polygon


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


def build_geospatial_query(bbox, query_parameters):
    polygon = {"$geometry": restructure_polygon_data(bbox["geometry"])}
    geospatial_query = {"geometry": {"$geoWithin": polygon}}
    
    match_query = build_match_query(query_parameters)
    geospatial_query.update(match_query)
    
    return geospatial_query
