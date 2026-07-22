import discord
from discord import app_commands
from discord.ext import commands

class General(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def avatar(self, ctx):
        embed = discord.Embed(
            title = 'Seu Avatar',
            color = discord.Color.from_str("#FF55E0")
        )

        embed.set_image(url=ctx.author.avatar.url)
        await ctx.send(embed=embed)

    @commands.command()
    async def hello(self, ctx):
        await ctx.send(
            "Olá! Sou o MathBot 🤖"
        )
    
    @commands.command()
    async def say(self, ctx, content: str):
        await ctx.send(content)

    @commands.command()
    async def help(self, ctx):
        await ctx.send(
            "Estou sendo desenvolvido, confira mais na minha pagina do github."
        )

async def setup(bot):
    await bot.add_cog(General(bot))