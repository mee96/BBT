from fastapi import APIRouter, Query
from typing import Optional
from utils.db_conection import get_connection

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])


@router.get("/")
def get_pedidos(
    usuario_id: Optional[int] = Query(None, description="Filtrar por usuario"),
    estado:     Optional[str] = Query(None, description="PENDIENTE | ENVIADO | RECIBIDO | DEVUELTO"),
):
    try:
        conn = get_connection()
        with conn.cursor() as cur:
            query = "SELECT * FROM pedido WHERE 1=1"
            params = []

            if usuario_id is not None:
                query += " AND usuario_id = %s"
                params.append(usuario_id)
            if estado is not None:
                query += " AND estado = %s"
                params.append(estado.upper())

            cur.execute(query, params)
            rows = cur.fetchall()
        return {"ok": True, "result": rows}
    except Exception as e:
        return {"ok": False, "error": str(e)}


@router.get("/{pedido_id}")
def get_pedido(pedido_id: int):
    try:
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM pedido WHERE pedido_id = %s",
                (pedido_id,)
            )
            row = cur.fetchone()
        return {"ok": True, "result": row}
    except Exception as e:
        return {"ok": False, "error": str(e)}