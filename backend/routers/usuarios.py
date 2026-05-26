from fastapi import APIRouter
from utils.db_conection import get_connection

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