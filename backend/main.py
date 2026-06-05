from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from auth import verify_firebase_token
from routers import bbt, categorias, toppings, usuarios, pedidos

app = FastAPI(
    title="🧋 BubbleTea API",
    description="API de gestió de begudes bubble tea",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Catàleg públic (lectura lliure)
app.include_router(bbt.router)
app.include_router(categorias.router)
app.include_router(toppings.router)

# Usuaris: el POST (registre) és públic; el PUT es protegeix dins del router.
app.include_router(usuarios.router)
# Dades sensibles: tot el router requereix token de Firebase
app.include_router(pedidos.router, dependencies=[Depends(verify_firebase_token)])

@app.get("/", tags=["Root"])
def root() -> dict[str, object]:
    return {
        "mensaje": "🧋 Bienvenido a la BubbleTea API",
        "version": "1.0.0",
        "docs": "/docs",
    }