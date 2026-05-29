from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER as MyINTEGER

from database.connection import Base


class Usuario(Base):
    __tablename__ = "usuario"

    usuario_id = Column(MyINTEGER(unsigned=True), primary_key=True, autoincrement=True)
    firebase_uid = Column(String(128), unique=True, nullable=True)
    nombre = Column(String(50), nullable=False)
    nombre_usuario = Column(String(30), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    contrasena = Column(String(20), nullable=True)
    pais = Column(String(30), nullable=True)
    ciudad = Column(String(30), nullable=True)
    direccion = Column(String(60), nullable=True)
    telf = Column(Integer, nullable=True)

    pedidos = relationship("Pedido", back_populates="usuario")
