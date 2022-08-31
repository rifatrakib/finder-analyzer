from geojson_pydantic import Feature, Polygon
from pydantic import BaseModel, Field
from typing import List, Dict, Union


class RangeQuery(BaseModel):
    min: float
    max: float


class QueryParametersModel(BaseModel):
    county_number: Union[List[str], None]
    city_number: Union[List[str], None]
    postal_region: Union[List[str], None]
    property_type: Union[List[str], None]
    ownership_form: Union[List[str], None]
    price: Union[RangeQuery, None]
    renovated_year: Union[RangeQuery, None]
    land_area: Union[RangeQuery, None]
    discount_relative: Union[RangeQuery, None]
    prediction: Union[RangeQuery, None]
    bedroom: Union[RangeQuery, None]
    room: Union[RangeQuery, None]
    floor: Union[RangeQuery, None]


class SortParametersModel(BaseModel):
    sort_fields: Union[List[str], None]
    sort_directions: Union[List[int], None]


class PayloadModel(BaseModel):
    query_parameters: Union[QueryParametersModel, None]
    sort_parameters: Union[SortParametersModel, None]
    bbox: Union[Feature[Polygon, Dict], None]
    page_number: int = 1
