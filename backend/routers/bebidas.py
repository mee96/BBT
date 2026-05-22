from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from models import BubbleTea
from data import bebidas
import random

router = APIRouter(prefix="/bebidas", tags=["Bebidas"])


@router.get("/random")
def get_bebida_random() -> BubbleTea:
    activas = [b for b in bebidas if b["activo"]]
    return random.choice(activas)


@router.get("/")
def get_bebidas(
    categoria_id: Optional[int]  = Query(None, description="Filtrar por categoría"),
    vegano:       Optional[bool] = Query(None, description="Solo veganos"),
    caliente:     Optional[bool] = Query(None, description="Disponibles en caliente"),
    activo:       Optional[bool] = Query(None, description="True = activas | False = inactivas"),
) -> list[BubbleTea]:
    resultado = bebidas

    if categoria_id is not None:
        resultado = [b for b in resultado if b["categoria_id"] == categoria_id]
    if vegano is not None:
        resultado = [b for b in resultado if b["es_vegano"] == vegano]
    if caliente is not None:
        resultado = [b for b in resultado if b["disponible_caliente"] == caliente]
    if activo is not None:
        resultado = [b for b in resultado if b["activo"] == activo]

    return resultado


@router.get("/{bubbletea_id}")
def get_bebida(bubbletea_id: int) -> BubbleTea:
    bebida = next((b for b in bebidas if b["bubbletea_id"] == bubbletea_id), None)
    if not bebida:
        raise HTTPException(status_code=404, detail="Bebida no encontrada")
    return bebida

