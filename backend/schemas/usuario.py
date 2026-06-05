from typing import Optional
from datetime import date
from pydantic import BaseModel, ConfigDict


class UsuarioCreate(BaseModel):
    firebase_uid: str  # s'assigna com a usuario_id (PK)
    nombre: str
    apellido: Optional[str] = None
    email: str
    fecha_nacimiento: Optional[date] = None


class UsuarioUpdate(BaseModel):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    fecha_nacimiento: Optional[date] = None
    active: Optional[bool] = None
    notifications: Optional[bool] = None


class UsuarioRead(BaseModel):
    usuario_id: str
    nombre: str
    apellido: Optional[str] = None
    email: str
    fecha_nacimiento: Optional[date] = None
    active: bool
    notifications: bool

    model_config = ConfigDict(from_attributes=True)
