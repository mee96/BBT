from sqlalchemy import Column, String, DECIMAL
from sqlalchemy.dialects.mysql import INTEGER as MyINTEGER

from database.connection import Base


class Topping(Base):
    __tablename__ = "topping"

    topping_id = Column(MyINTEGER(unsigned=True), primary_key=True, autoincrement=True)
    nombre = Column(String(60), nullable=False)
    precio_extra = Column(DECIMAL(4, 2), nullable=False, default=0.00)
