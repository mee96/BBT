from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.connection import get_db
from models import Topping, Alergeno

router = APIRouter(tags=["Toppings y Alérgenos"])


@router.get("/toppings")
def get_toppings(db: Session = Depends(get_db)):
    try:
        rows = db.query(Topping).all()
        return {
            "ok": True,
            "result": [
                {
                    "topping_id": t.topping_id,
                    "nombre": t.nombre,
                    "precio_extra": float(t.precio_extra),
                }
                for t in rows
            ],
        }
    except Exception as e:
        return {"ok": False, "error": str(e)}


@router.get("/toppings/{topping_id}")
def get_topping(topping_id: int, db: Session = Depends(get_db)):
    try:
        t = db.query(Topping).filter(Topping.topping_id == topping_id).first()
        if t is None:
            return {"ok": True, "result": None}
        return {
            "ok": True,
            "result": {
                "topping_id": t.topping_id,
                "nombre": t.nombre,
                "precio_extra": float(t.precio_extra),
            },
        }
    except Exception as e:
        return {"ok": False, "error": str(e)}


@router.get("/alergenos")
def get_alergenos(db: Session = Depends(get_db)):
    try:
        rows = db.query(Alergeno).all()
        return {
            "ok": True,
            "result": [
                {"alergeno_id": a.alergeno_id, "nombre": a.nombre} for a in rows
            ],
        }
    except Exception as e:
        return {"ok": False, "error": str(e)}
