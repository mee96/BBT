from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.connection import get_db
from models import Usuario
from schemas import UsuarioCreate, UsuarioUpdate

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])


def _serialize(u: Usuario) -> dict:
    return {
        "usuario_id": u.usuario_id,
        "firebase_uid": u.firebase_uid,
        "nombre": u.nombre,
        "nombre_usuario": u.nombre_usuario,
        "email": u.email,
        "pais": u.pais,
        "ciudad": u.ciudad,
        "direccion": u.direccion,
        "telf": u.telf,
    }


@router.get("/")
def get_usuarios(db: Session = Depends(get_db)):
    try:
        rows = db.query(Usuario).all()
        return {"ok": True, "result": [_serialize(u) for u in rows]}
    except Exception as e:
        return {"ok": False, "error": str(e)}


@router.get("/{usuario_id}")
def get_usuario(usuario_id: int, db: Session = Depends(get_db)):
    try:
        u = db.query(Usuario).filter(Usuario.usuario_id == usuario_id).first()
        return {"ok": True, "result": _serialize(u) if u else None}
    except Exception as e:
        return {"ok": False, "error": str(e)}


@router.get("/firebase/{firebase_uid}")
def get_usuario_by_firebase(firebase_uid: str, db: Session = Depends(get_db)):
    try:
        u = db.query(Usuario).filter(Usuario.firebase_uid == firebase_uid).first()
        return {"ok": True, "result": _serialize(u) if u else None}
    except Exception as e:
        return {"ok": False, "error": str(e)}


@router.post("/")
def create_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    try:
        nuevo = Usuario(
            firebase_uid=usuario.firebase_uid,
            nombre=usuario.nombre,
            nombre_usuario=usuario.nombre_usuario,
            email=usuario.email,
            pais=usuario.pais,
            ciudad=usuario.ciudad,
            direccion=usuario.direccion,
            telf=usuario.telf,
        )
        db.add(nuevo)
        db.commit()
        db.refresh(nuevo)
        return {"ok": True, "result": _serialize(nuevo)}
    except Exception as e:
        db.rollback()
        return {"ok": False, "error": str(e)}


@router.put("/firebase/{firebase_uid}")
def update_usuario(
    firebase_uid: str, usuario: UsuarioUpdate, db: Session = Depends(get_db)
):
    try:
        u = db.query(Usuario).filter(Usuario.firebase_uid == firebase_uid).first()
        if u is None:
            return {"ok": False, "error": "Usuario no trobat"}

        data = usuario.model_dump(exclude_unset=True)
        for key, value in data.items():
            if value is not None:
                setattr(u, key, value)

        db.commit()
        db.refresh(u)
        return {"ok": True, "result": _serialize(u)}
    except Exception as e:
        db.rollback()
        return {"ok": False, "error": str(e)}
