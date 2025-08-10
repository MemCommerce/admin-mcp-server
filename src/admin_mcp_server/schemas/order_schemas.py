from typing import Optional

from pydantic import BaseModel


class Order(BaseModel):
    id: str
    status: str
    user_id: Optional[str] = None
    total_price: Optional[float] = None
