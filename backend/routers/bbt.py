from fastapi import APIRouter, Query
from typing import Optional
import random
from models.models import BubbleTeaCreate
from utils.db_conection import get_connection

router = APIRouter(prefix="/bubbleteas", tags=["BubbleTeas"])

BASE_QUERY = """
    SELECT 
        b.bubbletea_id,
        b.nombre,
        b.tipo_bubbletea,
        b.descripcion,
        b.categoria_id,
        b.disponible_caliente,
        b.es_vegano,
        b.tiene_cafeina,
        b.stock,
        b.active AS activo,
        bt_m.precio AS precio_M,
        bt_l.precio AS precio_L,
        GROUP_CONCAT(a.nombre SEPARATOR ',') AS alergenos
    FROM bubbletea b
    LEFT JOIN bubbletea_tamano bt_m ON b.bubbletea_id = bt_m.bubbletea_id AND bt_m.tamano_id = 1
    LEFT JOIN bubbletea_tamano bt_l ON b.bubbletea_id = bt_l.bubbletea_id AND bt_l.tamano_id = 2
    LEFT JOIN bubbletea_alergeno ba ON b.bubbletea_id = ba.bubbletea_id
    LEFT JOIN alergenos a ON ba.alergeno_id = a.alergeno_id
"""

def parse_alergenos(rows: list) -> list:
    for row in rows:
        if row["alergenos"]:
            row["alergenos"] = row["alergenos"].split(",")
        else:
            row["alergenos"] = []
    return rows

def parse_alergeno(row: dict) -> dict:
    if row and row["alergenos"]:
        row["alergenos"] = row["alergenos"].split(",")
    elif row:
        row["alergenos"] = []
    return row


@router.get("/random")
def get_bubble_tea_random():
    try:
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute(
                BASE_QUERY + " WHERE b.active = TRUE GROUP BY b.bubbletea_id"
            )
            rows = cur.fetchall()
        if not rows:
            return {"ok": False, "error": "No hi ha begudes actives"}
        rows = parse_alergenos(rows)
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
            query = BASE_QUERY + " WHERE 1=1"
            params = []

            if categoria_id is not None:
                query += " AND b.categoria_id = %s"
                params.append(categoria_id)
            if vegano is not None:
                query += " AND b.es_vegano = %s"
                params.append(vegano)
            if caliente is not None:
                query += " AND b.disponible_caliente = %s"
                params.append(caliente)
            if activo is not None:
                query += " AND b.active = %s"
                params.append(activo)

            query += " GROUP BY b.bubbletea_id"

            cur.execute(query, params)
            rows = cur.fetchall()
        rows = parse_alergenos(rows)
        return {"ok": True, "result": rows}
    except Exception as e:
        return {"ok": False, "error": str(e)}


@router.get("/{bubbletea_id}")
def get_bubble_tea_by_id(bubbletea_id: int):
    try:
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute(
                BASE_QUERY + " WHERE b.bubbletea_id = %s GROUP BY b.bubbletea_id",
                (bubbletea_id,)
            )
            row = cur.fetchone()
        row = parse_alergeno(row)
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