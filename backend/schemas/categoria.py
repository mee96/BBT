from typing import Optional
from pydantic import BaseModel, ConfigDict


class CategoriaRead(BaseModel):
    categoria_id: int
    nombre: str
    nombre_zh: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)
