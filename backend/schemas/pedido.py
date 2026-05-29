from typing import Optional, List
from decimal import Decimal
from datetime import datetime
from pydantic import BaseModel, ConfigDict


class PedidoLineaRead(BaseModel):
    linea_id: int
    pedido_id: int
    bubbletea_id: int
    tamano_id: int
    tipo_leche_id: Optional[int] = None
    cantidad: int
    nivel_azucar: str
    nivel_hielo: str
    precio_unidad: Decimal

    model_config = ConfigDict(from_attributes=True)


class PedidoRead(BaseModel):
    pedido_id: int
    usuario_id: int
    fecha_pedido: datetime
    envio_nacional: Optional[bool] = False
    direccion_envio: Optional[str] = None
    estado: str
    precio_total: Optional[Decimal] = Decimal("0.00")

    model_config = ConfigDict(from_attributes=True)
