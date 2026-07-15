import discord
from math_engine.arithmetic import add
from discord import app_commands
from discord.ext import commands

class Arithmetic(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def soma(self, ctx, *numeros: int):
        await ctx.send(add(numeros))
        
async def setup(bot):
    await bot.add_cog(Arithmetic(bot))