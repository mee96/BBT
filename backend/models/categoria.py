from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER as MyINTEGER

from database.connection import Base


class Categoria(Base):
    __tablename__ = "categoria"

    categoria_id = Column(MyINTEGER(unsigned=True), primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False)
    nombre_zh = Column(String(50), nullable=True)

    bubbleteas = relationship("BubbleTea", back_populates="categoria")
