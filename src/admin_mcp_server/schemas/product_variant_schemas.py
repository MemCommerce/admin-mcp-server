from typing import Optional

from pydantic import BaseModel


class ProductVariantBase(BaseModel):
    price: float
    product_id: str
    color_id: str
    size_id: str


class ProductVariantData(ProductVariantBase):
    image_name: Optional[str] = None


class ProductVariantCreate(ProductVariantBase):
    image_url: str


class ProductVariant(ProductVariantBase):
    id: str
    image_url: Optional[str] = None
