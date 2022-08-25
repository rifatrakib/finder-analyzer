from pydantic import BaseModel
from typing import List, Dict, Optional


class QueryParametersModel(BaseModel):
    county_number: Optional[List[str]]
    city_number: Optional[List[str]]
    postal_region: Optional[List[str]]
    property_type: Optional[List[str]]
    ownership_form: Optional[List[str]]
    price: Optional[Dict[str, float]]
    renovated_year: Optional[Dict[str, float]]
    land_area: Optional[Dict[str, float]]
    discount_relative: Optional[Dict[str, float]]
    prediction: Optional[Dict[str, float]]
    bedroom: Optional[Dict[str, int]]
    room: Optional[Dict[str, int]]
    floor: Optional[Dict[str, int]]


class SortParametersModel(BaseModel):
    sort_fields: Optional[List[str]]
    sort_directions: Optional[List[int]]


class PolygonModel(BaseModel):
    type: Optional[str]
    coordinates: Optional[List[List[float]]]


class PayloadModel(BaseModel):
    query_parameters: Optional[QueryParametersModel]
    sort_parameters: Optional[SortParametersModel]
    bbox: Optional[PolygonModel]
    page_number: Optional[int] = 1
