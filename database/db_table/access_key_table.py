from sqlalchemy import Column, Integer, Float, ForeignKey, Boolean, String, Text, DateTime
from database.database import Base


class AccessKeyDB(Base):
    __tablename__ = "llaves_acceso"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    servicio = Column(String(200), nullable=False)
    usuario = Column(String(30), nullable=False)
    password_encriptado = Column(Text, nullable=False)
    salt = Column(Text, nullable=False)
    iv = Column(Text, nullable=False)
    tag = Column(Text, nullable=False)
    activo = Column(Boolean)
    creado = Column(DateTime)
    actualizado = Column(DateTime)