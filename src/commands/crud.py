import discord
from discord import app_commands
from discord.ext import commands
from bd.models import _Session, Usuario, Atividade

def account_check(ctx):
    with _Session() as sessao:
        usuario = sessao.query(Usuario).filter(Usuario.id_usuario == ctx.author.id).first()
    
    if usuario:
        return True

    if not usuario:
        new_usuario = Usuario(ctx.author.name, ctx.author.id)
        sessao.add(new_usuario)

        new_atividade = Atividade(ctx.author.id, 0, 0, 0)
        sessao.add(new_atividade)

        sessao.commit()
        return False

class Crud(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def create(self, ctx):
        if not account_check(ctx):
            await ctx.send('Conta criada com sucesso.')
            return 
        await ctx.send('Você já possui uma conta. Ao usar os comandos relacionados, o sistema cria automaticamente a sua conta. :D')

async def setup(bot):
    await bot.add_cog(Crud(bot))   