from pydantic import BaseModel
from typing import List, Dict, Optional


class QueryParametersModel(BaseModel):
    county: Optional[List[str]]
    city: Optional[List[str]]
    zipcode: Optional[List[str]]
    type: Optional[List[str]]
    form: Optional[List[str]]
    price: Optional[Dict[str, float]]
    date: Optional[Dict[str, float]]
    area: Optional[Dict[str, float]]
    discount: Optional[Dict[str, float]]
    estimate: Optional[Dict[str, float]]


class PayloadModel(BaseModel):
    query_parameters = Optional[QueryParametersModel()]
    bbox = Optional[List[List[float]]]
    sort_parameters = Optional[Dict[str, int]]
    page_number = Optional[int]
