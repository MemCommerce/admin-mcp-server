from pydantic import BaseModel


class ProductVariantBase(BaseModel):
    price: float
    product_id: str
    color_id: str
    size_id: str


class ProductVariantData(ProductVariantBase):
    pass


class ProductVariant(ProductVariantBase):
    id: str
