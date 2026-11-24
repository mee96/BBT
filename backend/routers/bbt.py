import random
from typing import Optional

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session, joinedload

from database.connection import get_db
from models import BubbleTea, BubbleTeaAlergeno

router = APIRouter(prefix="/bubbleteas", tags=["BubbleTeas"])


def _serialize(b: BubbleTea) -> dict:
    precio_m = None
    precio_l = None
    for bt in b.tamanos:
        if bt.tamano_id == 1:
            precio_m = float(bt.precio)
        elif bt.tamano_id == 2:
            precio_l = float(bt.precio)

    alergenos = [ba.alergeno.nombre for ba in b.alergenos if ba.alergeno is not None]

    return {
        "bubbletea_id": b.bubbletea_id,
        "nombre": b.nombre,
        "tipo_bubbletea": b.tipo_bubbletea,
        "descripcion": b.descripcion,
        "categoria_id": b.categoria_id,
        "disponible_caliente": b.disponible_caliente,
        "es_vegano": b.es_vegano,
        "tiene_cafeina": b.tiene_cafeina,
        "stock": b.stock,
        "activo": b.active,
        "precio_M": precio_m,
        "precio_L": precio_l,
        "alergenos": alergenos,
    }


def _options():
    return (
        joinedload(BubbleTea.tamanos),
        joinedload(BubbleTea.alergenos).joinedload(BubbleTeaAlergeno.alergeno),
    )


@router.get("/random")
def get_bubble_tea_random(db: Session = Depends(get_db)):
    try:
        rows = (
            db.query(BubbleTea)
            .options(*_options())
            .filter(BubbleTea.active.is_(True))
            .all()
        )
        if not rows:
            return {"ok": False, "error": "No hi ha begudes actives"}
        return {"ok": True, "result": _serialize(random.choice(rows))}
    except Exception as e:
        return {"ok": False, "error": str(e)}


@router.get("/")
def get_bubble_teas(
    categoria_id: Optional[int] = Query(None, description="Filtrar per categoria"),
    vegano: Optional[bool] = Query(None, description="Només vegans"),
    caliente: Optional[bool] = Query(None, description="Disponibles en calent"),
    activo: Optional[bool] = Query(None, description="True = actives | False = inactives"),
    db: Session = Depends(get_db),
):
    try:
        q = db.query(BubbleTea).options(*_options())
        if categoria_id is not None:
            q = q.filter(BubbleTea.categoria_id == categoria_id)
        if vegano is not None:
            q = q.filter(BubbleTea.es_vegano.is_(vegano))
        if caliente is not None:
            q = q.filter(BubbleTea.disponible_caliente.is_(caliente))
        if activo is not None:
            q = q.filter(BubbleTea.active.is_(activo))

        rows = q.all()
        return {"ok": True, "result": [_serialize(b) for b in rows]}
    except Exception as e:
        return {"ok": False, "error": str(e)}


@router.get("/{bubbletea_id}")
def get_bubble_tea_by_id(bubbletea_id: int, db: Session = Depends(get_db)):
    try:
        b = (
            db.query(BubbleTea)
            .options(*_options())
            .filter(BubbleTea.bubbletea_id == bubbletea_id)
            .first()
        )
        return {"ok": True, "result": _serialize(b) if b else None}
    except Exception as e:
        return {"ok": False, "error": str(e)}
