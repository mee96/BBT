from typing import TypedDict, Optional, List


class Categoria(TypedDict):
    categoria_id: int
    nombre: str
    nombre_zh: Optional[str]


class Tamano(TypedDict):
    tamano_id: int
    codigo: str
    nombre: str


class Topping(TypedDict):
    topping_id: int
    nombre: str
    precio_extra: float


class Alergeno(TypedDict):
    alergeno_id: int
    nombre: str


class BubbleTea(TypedDict):
    bubbletea_id: int
    nombre: str
    tipo_bubbletea: str
    descripcion: Optional[str]
    categoria_id: Optional[int]
    disponible_caliente: bool
    es_vegano: bool
    tiene_cafeina: bool
    precio_M: Optional[float]
    precio_L: Optional[float]
    alergenos: List[str]
    activo: bool


class Usuario(TypedDict):
    usuario_id: int
    nombre: str
    nombre_usuario: str
    email: str
    pais: Optional[str]
    ciudad: Optional[str]


class PedidoLinea(TypedDict):
    bubbletea_id: int
    nombre_bebida: str
    tamano: str
    cantidad: int
    nivel_azucar: str
    nivel_hielo: str
    precio_unidad: float
    toppings: List[str]


class Pedido(TypedDict):
    pedido_id: int
    usuario_id: int
    fecha_pedido: str
    estado: str
    precio_total: float
    lineas: List[PedidoLinea]


from pydantic import BaseModel

class BubbleTeaCreate(BaseModel):
    nombre: str
    tipo_bubbletea: str
    descripcion: Optional[str] = None
    categoria_id: Optional[int] = None
    disponible_caliente: bool = False
    es_vegano: bool = False
    tiene_cafeina: bool = False
    stock: int = 0
    active: bool = True