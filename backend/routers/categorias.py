from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.connection import get_db
from models import Categoria

router = APIRouter(prefix="/categorias", tags=["Categorías"])


@router.get("/")
def get_categorias(db: Session = Depends(get_db)):
    try:
        rows = db.query(Categoria).all()
        return {
            "ok": True,
            "result": [
                {
                    "categoria_id": c.categoria_id,
                    "nombre": c.nombre,
                    "nombre_zh": c.nombre_zh,
                }
                for c in rows
            ],
        }
    except Exception as e:
        return {"ok": False, "error": str(e)}


@router.get("/{categoria_id}")
def get_categoria(categoria_id: int, db: Session = Depends(get_db)):
    try:
        c = db.query(Categoria).filter(Categoria.categoria_id == categoria_id).first()
        if c is None:
            return {"ok": True, "result": None}
        return {
            "ok": True,
            "result": {
                "categoria_id": c.categoria_id,
                "nombre": c.nombre,
                "nombre_zh": c.nombre_zh,
            },
        }
    except Exception as e:
        return {"ok": False, "error": str(e)}
