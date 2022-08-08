from pydantic import BaseModel
from typing import List, Dict, Optional


class PayloadModel(BaseModel):
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
