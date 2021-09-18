from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Profile(Base):
    __tablename__ = 'profiles'
    # Here we define columns for the table profiles
    user_id = Column(String(50), primary_key=True)
    email = Column(String(50), nullable=False, unique=True)
    avatar = Column(String(250))
    presentacion = Column(Text)
    name = Column(String(50), nullable=False)
    website= Column(String(250))
    created_at = Column(DateTime(), default=datetime.now())

class Publicacion(Base):
    __tablename__ = 'publicaciones'
    # Here we define columns for the table publicaciones.
    id_publicaciones = Column(Integer, primary_key=True)
    media = Column(String(250))
    descripcion = Column(Text)
    created_at = Column(DateTime(), default=datetime.now())
    ubicacion = Column(String(250))
    owner = Column(String(250), ForeignKey('profiles.user_id'))


class Comentario(Base):
    __tablename__ = 'comentarios'
    # Here we define columns for the table comentarios.
    id_comentario = Column(Integer, primary_key=True)
    owner_comentario = Column(String(250), ForeignKey('profiles.user_id'))
    contenido = Column(Text)

class Likes(Base):
    __tablename__ = 'likes'
    # Here we define columns for the table likes.
    usuarios = Column(String(250), ForeignKey('profiles.user_id'), primary_key=True)
    id_comentario = Column(Integer, ForeignKey('comentarios.id_comentario'), primary_key=True)
    id_publicaciones = Column(Integer, ForeignKey('publicaciones.id_publicaciones'), primary_key=True)

class Vistos(Base):
    __tablename__ = 'vistos'
    # Here we define columns for the table vistos.
    id_vistos = Column(Integer, primary_key=True)
    usuarios = Column(String(250), ForeignKey('profiles.user_id'))

class Historia(Base):
    __tablename__ = 'historias'
    # Here we define columns for the table historias.
    id_historias = Column(Integer, primary_key=True)
    owner_historia = Column(String(250), ForeignKey('profiles.user_id'))
    media = Column(String(250), nullable=False)
    created_at = Column(DateTime(), default=datetime.now())
    vistos_historias = Column(Integer, ForeignKey('vistos.id_vistos'))

class Followers(Base):
    __tablename__ = 'followers'
    # Here we define columns for the table followers.
    user_from = Column(String(250), ForeignKey('profiles.user_id'), primary_key=True)
    user_to = Column(String(250), ForeignKey('profiles.user_id'), primary_key=True)

def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e