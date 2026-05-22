from fastapi import APIRouter, HTTPException
from typing import List
from models import Categoria
from data import categorias

router = APIRouter(prefix="/categorias", tags=["Categorías"])


@router.get("/")
def get_categorias() -> list[Categoria]:
    return categorias


@router.get("/{categoria_id}")
def get_categoria(categoria_id: int) -> Categoria:
    cat = next((c for c in categorias if c["categoria_id"] == categoria_id), None)
    if not cat:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return cat
