from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from models import Pedido
from data import pedidos

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])


@router.get("/")
def get_pedidos(
    usuario_id: Optional[int] = Query(None, description="Filtrar por usuario"),
    estado:     Optional[str] = Query(None, description="PENDIENTE | ENVIADO | RECIBIDO | DEVUELTO"),
) -> list[Pedido]:
    resultado = pedidos

    if usuario_id is not None:
        resultado = [p for p in resultado if p["usuario_id"] == usuario_id]
    if estado is not None:
        resultado = [p for p in resultado if p["estado"] == estado.upper()]

    return resultado


@router.get("/{pedido_id}")
def get_pedido(pedido_id: int) -> Pedido:
    p = next((p for p in pedidos if p["pedido_id"] == pedido_id), None)
    if not p:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return p
