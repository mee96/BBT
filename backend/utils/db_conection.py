import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

conn = None


# # conn is None — la primera vegada que s'executa, conn val None perquè no s'ha connectat mai. Llavors entra al if i crea la connexió.
# not conn.open — si conn ja existeix però la connexió s'ha tallat (timeout, caiguda de xarxa, etc.), conn.open val False. El not ho inverteix, és a dir, si no està oberta, entra al if i reconnecta.
# En resum:

# Connexió nova → conn is None → connecta
# Connexió tallada → not conn.open → reconnecta
# Connexió activa → no entra al if → reutilitza la mateixa

# # SINGELTON!!!(una sola connexio, com es algo simple ho hem de fer natros, si ya esta ya no lo vuelvo a crear lo retorno, si no esta, lo creo)  És el patró lazy connection — només connecta quan cal i reutilitza la connexió existent si ja funciona. Estalvia recursos i evita obrir mil connexions innecessàries.


def get_connection():
    global conn
    if conn is None or not conn.open:
        conn = pymysql.connect(
            charset=os.getenv("CHARSET", ""),
            cursorclass=pymysql.cursors.DictCursor,
            host=os.getenv("HOST", ""),
            connect_timeout=int(os.getenv("CONNECT_TIMEOUT", "10")),
            db=os.getenv("DB", ""),
            password=os.getenv("PASSWORD", ""),
            read_timeout=int(os.getenv("READ_TIMEOUT", "10")),
            port=int(os.getenv("PORT", "")),
            user=os.getenv("USER", ""),
            write_timeout=int(os.getenv("WRITE_TIMEOUT", "10")),
        )
    return conn

