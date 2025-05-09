from pydantic import BaseModel


class ColorBase(BaseModel):
    name: str
    hex: str


class ColorData(ColorBase):
    pass


class Color(ColorBase):
    id: str
