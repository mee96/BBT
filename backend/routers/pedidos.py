from typing import Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from database.connection import get_db
from models import Pedido

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])


def _serialize(p: Pedido) -> dict:
    return {
        "pedido_id": p.pedido_id,
        "usuario_id": p.usuario_id,
        "fecha_pedido": p.fecha_pedido.isoformat() if p.fecha_pedido else None,
        "envio_nacional": p.envio_nacional,
        "direccion_envio": p.direccion_envio,
        "estado": p.estado,
        "precio_total": float(p.precio_total) if p.precio_total is not None else 0.0,
    }


@router.get("/")
def get_pedidos(
    usuario_id: Optional[int] = Query(None, description="Filtrar por usuario"),
    estado: Optional[str] = Query(
        None, description="PENDIENTE | ENVIADO | RECIBIDO | DEVUELTO"
    ),
    db: Session = Depends(get_db),
):
    try:
        q = db.query(Pedido)
        if usuario_id is not None:
            q = q.filter(Pedido.usuario_id == usuario_id)
        if estado is not None:
            q = q.filter(Pedido.estado == estado.upper())
        rows = q.all()
        return {"ok": True, "result": [_serialize(p) for p in rows]}
    except Exception as e:
        return {"ok": False, "error": str(e)}


@router.get("/{pedido_id}")
def get_pedido(pedido_id: int, db: Session = Depends(get_db)):
    try:
        p = db.query(Pedido).filter(Pedido.pedido_id == pedido_id).first()
        return {"ok": True, "result": _serialize(p) if p else None}
    except Exception as e:
        return {"ok": False, "error": str(e)}
