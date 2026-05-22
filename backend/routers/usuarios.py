from fastapi import APIRouter, HTTPException
from models import Usuario
from data import usuarios

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])


@router.get("/")
def get_usuarios() -> list[Usuario]:
    return usuarios


@router.get("/{usuario_id}")
def get_usuario(usuario_id: int) -> Usuario:
    u = next((u for u in usuarios if u["usuario_id"] == usuario_id), None)
    if not u:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return u
