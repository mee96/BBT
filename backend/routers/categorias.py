from fastapi import APIRouter
from utils.db_conection import get_connection

router = APIRouter(prefix="/categorias", tags=["Categorías"])


@router.get("/")
def get_categorias():
    try:
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM categoria")
            rows = cur.fetchall()
        return {"ok": True, "result": rows}
    except Exception as e:
        return {"ok": False, "error": str(e)}


@router.get("/{categoria_id}")
def get_categoria(categoria_id: int):
    try:
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM categoria WHERE categoria_id = %s",
                (categoria_id,)
            )
            row = cur.fetchone()
        return {"ok": True, "result": row}
    except Exception as e:
        return {"ok": False, "error": str(e)}