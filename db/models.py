from .database import Base
from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import DateTime as SQLAlchemyDateTime


class Rol(Base):
    __tablename__ = 'roles'
    rol_id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    permisos = Column(Text)
    user = relationship('User', back_populates='rol')


class User(Base):
    __tablename__ = 'user'
    id_user = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    # Clave foránea que referencia a Rol
    rol_id = Column(Integer, ForeignKey('roles.rol_id'))
    # Relación con Rol
    rol = relationship('Rol', back_populates='user')

class Edificio(Base):
    __tablename__ = 'edificio'
    edificio_id = Column(String(20), primary_key=True)
    nombre = Column(String(100))
    descripcion = Column(Text)
    mapa = Column(String(255))
    fecha_creacion = Column(SQLAlchemyDateTime)

    # Relación con Ubicacion
    ubicaciones = relationship("Ubicacion", back_populates="edificio")
    # Relación con Piso
    pisos = relationship("Piso", back_populates="edificio")

class Piso(Base):
    __tablename__ = 'piso'
    id_piso = Column(Integer, primary_key=True)
    nombre = Column(String(30))
    edificio_id = Column(String(20), ForeignKey('edificio.edificio_id')) # Clave foránea a Edificio

    # Relación con Edificio
    edificio = relationship("Edificio", back_populates="piso")
    # Relación con Ambiente
    ambientes = relationship("Ambiente", back_populates="piso")


class Ambiente(Base):
    __tablename__ = 'ambiente'
    id_ambiente = Column(Integer, primary_key=True)
    nomenclatura = Column(String(30))
    descripcion = Column(String(30))
    id_piso = Column(Integer, ForeignKey('piso.id_piso')) # Clave foránea a Piso

    # Relación con Piso
    piso = relationship("Piso", back_populates="ambiente")

class Ubicacion(Base):
    __tablename__ = 'ubicaciones'
    id_Ubicacion =Column(String(60), primary_key=True)
    # Clave foránea a Usuario (usando id_user)
    id_user  = Column(Integer, ForeignKey('user.id_user'))
    edificio_id = Column(String(20), ForeignKey('edificio.edificio_id'))
    id_piso = Column(Integer)
    id_ambiente = Column(String(10))
    hora = Column(SQLAlchemyDateTime)

    # Relación con Usuario (usando id_user)
    user = relationship("User", back_populates="ubicaciones")
    edificio = relationship("Edificio", back_populates="ubicaciones")