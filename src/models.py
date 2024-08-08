import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from datetime import datetime

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    
    id = Column(Integer, primary_key=True)
    nombre_usuario = Column(String(150), unique=True, nullable=False)
    nombre_completo = Column(String(250))
    email = Column(String(250), unique=True, nullable=False)
    contrasena = Column(String(250), nullable=False)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)
    biografia = Column(Text)

    posts = relationship('Post', back_populates='usuario')
    comentarios = relationship('Comentario', back_populates='usuario')
    seguidores = relationship('Seguidor', foreign_keys='Seguidor.usuario_id', back_populates='usuario')
    siguiendo = relationship('Seguidor', foreign_keys='Seguidor.seguidor_id', back_populates='seguidor')

class Post(Base):
    __tablename__ = 'post'
    
    id = Column(Integer, primary_key=True)
    contenido = Column(Text, nullable=False)
    imagen_url = Column(String(500))
    fecha_publicacion = Column(DateTime, default=datetime.utcnow)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))

    usuario = relationship('Usuario', back_populates='posts')
    comentarios = relationship('Comentario', back_populates='post')

class Comentario(Base):
    __tablename__ = 'comentario'
    
    id = Column(Integer, primary_key=True)
    contenido = Column(Text, nullable=False)
    fecha_comentario = Column(DateTime, default=datetime.utcnow)
    post_id = Column(Integer, ForeignKey('post.id'))
    usuario_id = Column(Integer, ForeignKey('usuario.id'))

    post = relationship('Post', back_populates='comentarios')
    usuario = relationship('Usuario', back_populates='comentarios')

class Seguidor(Base):
    __tablename__ = 'seguidor'
    
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    seguidor_id = Column(Integer, ForeignKey('usuario.id'))

    usuario = relationship('Usuario', foreign_keys=[usuario_id], back_populates='seguidores')
    seguidor = relationship('Usuario', foreign_keys=[seguidor_id], back_populates='siguiendo')

render_er(Base, 'diagram.png')

