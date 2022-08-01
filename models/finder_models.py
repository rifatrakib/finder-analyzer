from pydantic import BaseModel
from typing import List, Dict


class PayloadModel(BaseModel):
    county: List[str]
    city: List[str]
    zipcode: List[str]
    type: List[str]
    form: List[str]
    price: Dict[str, float]
    date: Dict[str, int]
    area: Dict[str, float]
    discount: Dict[str, float]
    estimate: Dict[str, float]
