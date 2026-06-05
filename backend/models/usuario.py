from sqlalchemy import Column, String, Boolean, Date

from database.connection import Base


class Usuario(Base):
    __tablename__ = "entity_user"

    usuario_id = Column(String(128), primary_key=True)  # = firebase_uid
    nombre = Column(String(50), nullable=False)
    apellido = Column(String(50), nullable=True)
    email = Column(String(50), unique=True, nullable=False)
    fecha_nacimiento = Column(Date, nullable=True)
    active = Column(Boolean, default=True)
    notifications = Column(Boolean, default=True)
