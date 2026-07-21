import discord
from discord import app_commands
from discord.ext import commands
from services.usuario import get_or_create_user

class Treino(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def treino(self, ctx):
        usuario = get_or_create_user(ctx)

        await ctx.send(f'{usuario.nome}')

        

async def setup(bot):
    await bot.add_cog(Treino(bot))   