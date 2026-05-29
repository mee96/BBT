from sqlalchemy import Column, String, Boolean, DECIMAL, ForeignKey, TIMESTAMP, Enum, func
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER as MyINTEGER

from database.connection import Base


class Pedido(Base):
    __tablename__ = "pedido"

    pedido_id = Column(MyINTEGER(unsigned=True), primary_key=True, autoincrement=True)
    usuario_id = Column(
        MyINTEGER(unsigned=True),
        ForeignKey("usuario.usuario_id", onupdate="CASCADE", ondelete="RESTRICT"),
        nullable=False,
    )
    fecha_pedido = Column(TIMESTAMP, nullable=False, server_default=func.current_timestamp())
    envio_nacional = Column(Boolean, default=False)
    direccion_envio = Column(String(60), nullable=True)
    estado = Column(
        Enum("PENDIENTE", "ENVIADO", "RECIBIDO", "DEVUELTO", name="pedido_estado"),
        nullable=False,
        default="PENDIENTE",
    )
    precio_total = Column(DECIMAL(8, 2), default=0.00)

    usuario = relationship("Usuario", back_populates="pedidos")
    lineas = relationship(
        "PedidoLinea", back_populates="pedido", cascade="all, delete-orphan"
    )


class PedidoLinea(Base):
    __tablename__ = "pedido_linea"

    linea_id = Column(MyINTEGER(unsigned=True), primary_key=True, autoincrement=True)
    pedido_id = Column(
        MyINTEGER(unsigned=True),
        ForeignKey("pedido.pedido_id", onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False,
    )
    bubbletea_id = Column(
        MyINTEGER(unsigned=True),
        ForeignKey("bubbletea.bubbletea_id", onupdate="CASCADE", ondelete="RESTRICT"),
        nullable=False,
    )
    tamano_id = Column(
        MyINTEGER(unsigned=True),
        ForeignKey("tamano.tamano_id", onupdate="CASCADE", ondelete="RESTRICT"),
        nullable=False,
    )
    tipo_leche_id = Column(
        MyINTEGER(unsigned=True),
        ForeignKey("tipo_leche.tipo_leche_id", onupdate="CASCADE", ondelete="SET NULL"),
        nullable=True,
    )
    cantidad = Column(MyINTEGER(unsigned=True), nullable=False, default=1)
    nivel_azucar = Column(
        Enum("Extra", "Regular", "70%", "50%", "30%", "Sin azucar", name="nivel_azucar"),
        nullable=False,
        default="Regular",
    )
    nivel_hielo = Column(
        Enum("Extra", "Regular", "Poco", "No", "Tibio", "Caliente", name="nivel_hielo"),
        nullable=False,
        default="Regular",
    )
    precio_unidad = Column(DECIMAL(8, 2), nullable=False)

    pedido = relationship("Pedido", back_populates="lineas")
    bubbletea = relationship("BubbleTea")
    tamano = relationship("Tamano")
    tipo_leche = relationship("TipoLeche")
    toppings = relationship(
        "PedidoLineaTopping", back_populates="linea", cascade="all, delete-orphan"
    )


class PedidoLineaTopping(Base):
    __tablename__ = "pedido_linea_topping"

    linea_id = Column(
        MyINTEGER(unsigned=True),
        ForeignKey("pedido_linea.linea_id", onupdate="CASCADE", ondelete="CASCADE"),
        primary_key=True,
    )
    topping_id = Column(
        MyINTEGER(unsigned=True),
        ForeignKey("topping.topping_id", onupdate="CASCADE", ondelete="RESTRICT"),
        primary_key=True,
    )

    linea = relationship("PedidoLinea", back_populates="toppings")
    topping = relationship("Topping")
