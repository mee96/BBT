from fastapi import APIRouter
from utils.db_conection import get_connection

router = APIRouter(tags=["Toppings y Alérgenos"])


@router.get("/toppings")
def get_toppings():
    try:
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM topping")
            rows = cur.fetchall()
        return {"ok": True, "result": rows}
    except Exception as e:
        return {"ok": False, "error": str(e)}


@router.get("/toppings/{topping_id}")
def get_topping(topping_id: int):
    try:
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM topping WHERE topping_id = %s",
                (topping_id,)
            )
            row = cur.fetchone()
        return {"ok": True, "result": row}
    except Exception as e:
        return {"ok": False, "error": str(e)}


@router.get("/alergenos")
def get_alergenos():
    try:
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM alergenos")
            rows = cur.fetchall()
        return {"ok": True, "result": rows}
    except Exception as e:
        return {"ok": False, "error": str(e)}