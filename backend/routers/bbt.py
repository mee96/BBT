from fastapi import APIRouter, Query
from typing import Optional
import random
from models.models import BubbleTeaCreate
from utils.db_conection import get_connection

router = APIRouter(prefix="/bubbleteas", tags=["BubbleTeas"])


@router.get("/random")
def get_bubble_tea_random():
    try:
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM bubbletea WHERE active = TRUE")
            rows = cur.fetchall()
        if not rows:
            return {"ok": False, "error": "No hi ha begudes actives"}
        return {"ok": True, "result": random.choice(rows)}
    except Exception as e:
        return {"ok": False, "error": str(e)}


@router.get("/")
def get_bubble_teas(
    categoria_id: Optional[int]  = Query(None, description="Filtrar per categoria"),
    vegano:       Optional[bool] = Query(None, description="Només vegans"),
    caliente:     Optional[bool] = Query(None, description="Disponibles en calent"),
    activo:       Optional[bool] = Query(None, description="True = actives | False = inactives"),
):
    try:
        conn = get_connection()
        with conn.cursor() as cur:
            query = "SELECT * FROM bubbletea WHERE 1=1"
            params = []

            if categoria_id is not None:
                query += " AND categoria_id = %s"
                params.append(categoria_id)
            if vegano is not None:
                query += " AND es_vegano = %s"
                params.append(vegano)
            if caliente is not None:
                query += " AND disponible_caliente = %s"
                params.append(caliente)
            if activo is not None:
                query += " AND active = %s"
                params.append(activo)

            cur.execute(query, params)
            rows = cur.fetchall()
        return {"ok": True, "result": rows}
    except Exception as e:
        return {"ok": False, "error": str(e)}


@router.get("/{bubbletea_id}")
def get_bubble_tea_by_id(bubbletea_id: int):
    try:
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM bubbletea WHERE bubbletea_id = %s",
                (bubbletea_id,)
            )
            row = cur.fetchone()
        return {"ok": True, "result": row}
    except Exception as e:
        return {"ok": False, "error": str(e)}


@router.post("/")
def create_bubble_tea(bubble_tea: BubbleTeaCreate):
    try:
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute(
                """INSERT INTO bubbletea 
                (nombre, tipo_bubbletea, descripcion, categoria_id,
                disponible_caliente, es_vegano, tiene_cafeina, stock, active)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                (bubble_tea.nombre, bubble_tea.tipo_bubbletea,
                bubble_tea.descripcion, bubble_tea.categoria_id,
                bubble_tea.disponible_caliente, bubble_tea.es_vegano,
                bubble_tea.tiene_cafeina, bubble_tea.stock, bubble_tea.active)
            )
            conn.commit()
        return {"ok": True, "result": bubble_tea}
    except Exception as e:
        return {"ok": False, "error": str(e)}


@router.put("/{bubbletea_id}")
def update_bubble_tea(bubbletea_id: int, bubble_tea: BubbleTeaCreate):
    try:
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute(
                """UPDATE bubbletea SET 
                nombre = %s, tipo_bubbletea = %s, descripcion = %s,
                categoria_id = %s, disponible_caliente = %s,
                es_vegano = %s, tiene_cafeina = %s, stock = %s, active = %s
                WHERE bubbletea_id = %s""",
                (bubble_tea.nombre, bubble_tea.tipo_bubbletea,
                bubble_tea.descripcion, bubble_tea.categoria_id,
                bubble_tea.disponible_caliente, bubble_tea.es_vegano,
                bubble_tea.tiene_cafeina, bubble_tea.stock,
                bubble_tea.active, bubbletea_id)
            )
            conn.commit()
        return {"ok": True, "result": bubble_tea}
    except Exception as e:
        return {"ok": False, "error": str(e)}


@router.delete("/{bubbletea_id}")
def delete_bubble_tea(bubbletea_id: int):
    try:
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE bubbletea SET active = FALSE WHERE bubbletea_id = %s",
                (bubbletea_id,)
            )
            conn.commit()
        return {"ok": True}
    except Exception as e:
        return {"ok": False, "error": str(e)}