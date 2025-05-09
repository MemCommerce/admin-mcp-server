from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str
    description: str


class CategoryData(CategoryBase):
    pass


class Category(CategoryBase):
    id: str
