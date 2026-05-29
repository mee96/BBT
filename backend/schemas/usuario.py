from typing import Optional
from pydantic import BaseModel, ConfigDict


class UsuarioBase(BaseModel):
    nombre: str
    nombre_usuario: str
    email: str
    pais: Optional[str] = None
    ciudad: Optional[str] = None
    direccion: Optional[str] = None
    telf: Optional[int] = None


class UsuarioCreate(UsuarioBase):
    firebase_uid: str


class UsuarioUpdate(BaseModel):
    nombre: Optional[str] = None
    nombre_usuario: Optional[str] = None
    pais: Optional[str] = None
    ciudad: Optional[str] = None
    direccion: Optional[str] = None
    telf: Optional[int] = None


class UsuarioRead(UsuarioBase):
    usuario_id: int
    firebase_uid: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)
