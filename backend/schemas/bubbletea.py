from typing import Optional, List
from decimal import Decimal
from pydantic import BaseModel, ConfigDict


class BubbleTeaBase(BaseModel):
    nombre: str
    tipo_bubbletea: str
    descripcion: Optional[str] = None
    categoria_id: Optional[int] = None
    disponible_caliente: bool = False
    es_vegano: bool = False
    tiene_cafeina: bool = False
    stock: int = 0
    active: bool = True


class BubbleTeaCreate(BubbleTeaBase):
    pass


class BubbleTeaUpdate(BubbleTeaBase):
    pass


class BubbleTeaRead(BaseModel):
    bubbletea_id: int
    nombre: str
    tipo_bubbletea: str
    descripcion: Optional[str] = None
    categoria_id: Optional[int] = None
    disponible_caliente: bool
    es_vegano: bool
    tiene_cafeina: bool
    stock: Optional[int] = 0
    activo: bool
    precio_M: Optional[Decimal] = None
    precio_L: Optional[Decimal] = None
    alergenos: List[str] = []

    model_config = ConfigDict(from_attributes=True)
