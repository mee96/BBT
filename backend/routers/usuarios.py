from fastapi import APIRouter
from utils.db_conection import get_connection
from pydantic import BaseModel
from typing import Optional

class UsuarioCreate(BaseModel):
    firebase_uid: str
    nombre: str
    nombre_usuario: str
    email: str
    pais: Optional[str] = None
    ciudad: Optional[str] = None
    direccion: Optional[str] = None
    telf: Optional[int] = None

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])


@router.get("/")
def get_usuarios():
    try:
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM usuario")
            rows = cur.fetchall()
        return {"ok": True, "result": rows}
    except Exception as e:
        return {"ok": False, "error": str(e)}


@router.get("/{usuario_id}")
def get_usuario(usuario_id: int):
    try:
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM usuario WHERE usuario_id = %s",
                (usuario_id,)
            )
            row = cur.fetchone()
        return {"ok": True, "result": row}
    except Exception as e:
        return {"ok": False, "error": str(e)}


@router.get("/firebase/{firebase_uid}")
def get_usuario_by_firebase(firebase_uid: str):
    try:
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM usuario WHERE firebase_uid = %s",
                (firebase_uid,)
            )
            row = cur.fetchone()
        return {"ok": True, "result": row}
    except Exception as e:
        return {"ok": False, "error": str(e)}


@router.post("/")
def create_usuario(usuario: UsuarioCreate):
    try:
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute(
                """INSERT INTO usuario 
                (firebase_uid, nombre, nombre_usuario, email, pais, ciudad, direccion, telf)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
                (usuario.firebase_uid, usuario.nombre, usuario.nombre_usuario,
                usuario.email, usuario.pais, usuario.ciudad,
                usuario.direccion, usuario.telf)
            )
            conn.commit()
        return {"ok": True, "result": usuario}
    except Exception as e:
        return {"ok": False, "error": str(e)}