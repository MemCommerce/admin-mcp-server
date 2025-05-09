from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    brand: str
    description: str
    category_id: str


class ProductData(ProductBase):
    pass


class Product(ProductBase):
    id: str
