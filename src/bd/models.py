from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker

db = create_engine('sqlite:///banco.db')
Base = declarative_base()

_Session = sessionmaker(db)

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column('id', Integer, primary_key = True, autoincrement = True)
    id_usuario = Column('id_usuario', Integer, unique = True)
    nome = Column('nome', String, nullable = False)

    xp = Column('xp', Integer, default = 0, nullable = False)
    nivel = Column('nivel', Integer, default = 0, nullable = False)
    moedas = Column('moedas', Integer, default = 0, nullable = False)
    streak = Column('streak', Integer, default = 0, nullable = False)

    def __init__(self, nome, id_usuario, xp, nivel, moedas, streak):
        self.nome = nome
        self.id_usuario = id_usuario
        self.xp = xp
        self.nivel = nivel
        self.moedas = moedas
        self.streak = streak

class Estatistica(Base):
    __tablename__ = 'estatisticas'

    id = Column('id', Integer, primary_key = True, autoincrement = True)
    id_usuario = Column('id_usuario', Integer, ForeignKey('usuarios.id'), nullable = False)
    acerto = Column('acerto', Integer, default = 0, nullable = False)
    erro = Column('erro', Integer, default = 0, nullable = False)
    tempo_total = Column('tempo_total', Integer, default = 0, nullable = False)
    melhor_streak = Column('melhor_streak', Integer, default = 0, nullable = False)

    def __init__(self, id_usuario, acerto, erro, tempo_total, melhor_streak):
        self.id_usuario = id_usuario
        self.acerto = acerto
        self.erro = erro
        self.tempo_total = tempo_total
        self.melhor_streak = melhor_streak

class Progresso(Base):
    __tablename__ = 'progressos'

    id = Column('id', Integer, autoincrement = True, primary_key = True)
    id_usuario = Column('id_usuario', Integer, ForeignKey('usuarios.id'), nullable = False)
    categoria = Column('categoria', String, nullable = False)
    nivel = Column('nivel', Integer, default = 0, nullable = False)
    xp = Column('xp', Integer, default = 0, nullable = False)

    def __init__(self, id_usuario, categoria, nivel, xp):
        self.id_usuario = id_usuario
        self.categoria = categoria
        self.nivel = nivel
        self.xp = xp

Base.metadata.create_all(db)