import discord
from math_engine.arithmetic import add, subtract, divide, multiply, potency
from discord import app_commands
from discord.ext import commands

class Arithmetic(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def somar(self, ctx, *numeros: int):
            await ctx.send(add(numeros))

    @commands.command()
    async def subtrair(self, ctx, *numeros: int):
        await ctx.send(subtract(numeros))
    
    @commands.command()
    async def multiplicar(self, ctx, *numeros: int):
        await ctx.send(multiply(numeros))

    @commands.command()
    async def dividir(self, ctx, *numeros: int):
        await ctx.send(divide(numeros))

    @commands.command()
    async def potencia(self, ctx, n1: int, n2: int):
        await ctx.send(potency(n1, n2))

async def setup(bot):
    await bot.add_cog(Arithmetic(bot))