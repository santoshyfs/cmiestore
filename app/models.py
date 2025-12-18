from pydantic import BaseModel
from typing import List, Optional


class Price(BaseModel):
    value: float
    currency: str


class Product(BaseModel):
    name: str
    sku: str
    price: Price
    url: str
    image: Optional[str]
    description: Optional[str]


class ProductSearchResponse(BaseModel):
    total: int
    items: List[Product]
