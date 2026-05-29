from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import INTEGER as MyINTEGER

from database.connection import Base


class Tamano(Base):
    __tablename__ = "tamano"

    tamano_id = Column(MyINTEGER(unsigned=True), primary_key=True, autoincrement=True)
    codigo = Column(String(5), nullable=False)
    nombre = Column(String(20), nullable=False)
