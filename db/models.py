from .database import Base
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
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
    
    # Relación con Rol
    rol = relationship('Rol', back_populates='user')
    rol_id = Column(Integer, ForeignKey('roles.rol_id'))

