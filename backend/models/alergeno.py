from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import INTEGER as MyINTEGER

from database.connection import Base


class Alergeno(Base):
    __tablename__ = "alergenos"

    alergeno_id = Column(MyINTEGER(unsigned=True), primary_key=True, autoincrement=True)
    nombre = Column(String(30), unique=True, nullable=False)
