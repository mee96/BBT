from sqlalchemy import Column, String, Text, Boolean, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER as MyINTEGER

from database.connection import Base


class BubbleTea(Base):
    __tablename__ = "bubbletea"

    bubbletea_id = Column(MyINTEGER(unsigned=True), primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    tipo_bubbletea = Column(String(50), nullable=False)
    descripcion = Column(Text, nullable=True)
    categoria_id = Column(
        MyINTEGER(unsigned=True),
        ForeignKey("categoria.categoria_id", onupdate="CASCADE", ondelete="SET NULL"),
        nullable=True,
    )
    disponible_caliente = Column(Boolean, nullable=False, default=False)
    es_vegano = Column(Boolean, nullable=False, default=False)
    tiene_cafeina = Column(Boolean, nullable=False, default=False)
    stock = Column(MyINTEGER(unsigned=True), default=0)
    active = Column(Boolean, nullable=False, default=True)

    categoria = relationship("Categoria", back_populates="bubbleteas")
    tamanos = relationship(
        "BubbleTeaTamano", back_populates="bubbletea", cascade="all, delete-orphan"
    )
    alergenos = relationship(
        "BubbleTeaAlergeno", back_populates="bubbletea", cascade="all, delete-orphan"
    )


class BubbleTeaTamano(Base):
    __tablename__ = "bubbletea_tamano"

    bubbletea_id = Column(
        MyINTEGER(unsigned=True),
        ForeignKey("bubbletea.bubbletea_id", onupdate="CASCADE", ondelete="CASCADE"),
        primary_key=True,
    )
    tamano_id = Column(
        MyINTEGER(unsigned=True),
        ForeignKey("tamano.tamano_id", onupdate="CASCADE", ondelete="RESTRICT"),
        primary_key=True,
    )
    precio = Column(DECIMAL(8, 2), nullable=False)
    disponible = Column(Boolean, nullable=False, default=True)

    bubbletea = relationship("BubbleTea", back_populates="tamanos")
    tamano = relationship("Tamano")


class BubbleTeaAlergeno(Base):
    __tablename__ = "bubbletea_alergeno"

    bubbletea_id = Column(
        MyINTEGER(unsigned=True),
        ForeignKey("bubbletea.bubbletea_id", onupdate="CASCADE", ondelete="CASCADE"),
        primary_key=True,
    )
    alergeno_id = Column(
        MyINTEGER(unsigned=True),
        ForeignKey("alergenos.alergeno_id", onupdate="CASCADE", ondelete="CASCADE"),
        primary_key=True,
    )

    bubbletea = relationship("BubbleTea", back_populates="alergenos")
    alergeno = relationship("Alergeno")
