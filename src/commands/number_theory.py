import discord
from discord import app_commands
from discord.ext import commands
from math_engine.number_theory import primo

class Number_theory(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def primo(self, ctx, number: int):
        number = primo(number)
        if number:
            await ctx.send('Seu número é primo')
            return 
        await ctx.send('Seu número não é primo')

async def setup(bot):
    await bot.add_cog(Number_theory(bot))   