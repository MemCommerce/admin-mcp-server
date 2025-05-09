from pydantic import BaseModel


class SizeBase(BaseModel):
    label: str


class SizeData(SizeBase):
    pass


class Size(SizeBase):
    id: str
