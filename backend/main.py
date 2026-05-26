from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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

app.include_router(bbt.router)

app.include_router(categorias.router)
app.include_router(toppings.router)
app.include_router(usuarios.router)
app.include_router(pedidos.router)

@app.get("/", tags=["Root"])
def root() -> dict[str, object]:
    return {
        "mensaje": "🧋 Bienvenido a la BubbleTea API",
        "version": "1.0.0",
        "docs": "/docs",
    }