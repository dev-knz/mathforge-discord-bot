from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker

db = create_engine('sqlite:///banco.db')
Base = declarative_base()

_Session = sessionmaker(db)

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column('id', Integer, primary_key = True, autoincrement = True)
    nome = Column('nome', String)
    id_usuario = Column('id_usuario', Integer, unique = True)

    def __init__(self, nome, id_usuario):
        self.nome = nome
        self.id_usuario = id_usuario

Base.metadata.create_all(db)