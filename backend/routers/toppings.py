from fastapi import APIRouter, HTTPException
from models import Topping, Alergeno
from data import toppings, alergenos

router = APIRouter(tags=["Toppings y Alérgenos"])


@router.get("/toppings")
def get_toppings() -> list[Topping]:
    return toppings


@router.get("/toppings/{topping_id}")
def get_topping(topping_id: int) -> Topping:
    t = next((t for t in toppings if t["topping_id"] == topping_id), None)
    if not t:
        raise HTTPException(status_code=404, detail="Topping no encontrado")
    return t


@router.get("/alergenos")
def get_alergenos() -> list[Alergeno]:
    return alergenos
