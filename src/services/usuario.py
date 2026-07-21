import discord
from discord import app_commands
from discord.ext import commands
from bd.models import _Session, Usuario, Estatistica, Progresso
from constants.categorias import Categoria

def get_or_create_user(ctx):
    with _Session() as sessao:
        usuario = sessao.query(Usuario).filter(Usuario.id_usuario == ctx.author.id).first()
    
        if usuario:
            return usuario

        new_usuario = Usuario(ctx.author.name, ctx.author.id, xp=0, nivel=0, moedas=0, streak=0)
        sessao.add(new_usuario)

        new_estatistic = Estatistica(ctx.author.id, acerto=0, erro=0, tempo_total=0, melhor_streak=0)
        sessao.add(new_estatistic)

        for categoria in Categoria:
            progresso = Progresso(
                id_usuario=ctx.author.id,
                categoria=categoria.value,
                nivel=0,
                xp=0
                
            )
            sessao.add(progresso)
        

        sessao.commit()
        return new_usuario