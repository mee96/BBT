from decimal import Decimal
from pydantic import BaseModel, ConfigDict


class ToppingRead(BaseModel):
    topping_id: int
    nombre: str
    precio_extra: Decimal

    model_config = ConfigDict(from_attributes=True)
