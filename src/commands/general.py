import discord
from discord import app_commands
from discord.ext import commands
from services.discord_server import Discord_Service

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
    async def say(self, ctx, *,content: str):
        await ctx.send(content)

    @commands.command()
    async def categoria(self, ctx):
        await ctx.send('Copie e cole a categoria ID para a criação dos canais de treino!')

        discord_service = Discord_Service(self.bot)
        category_id = await discord_service.get_answer(ctx)
        discord_service.set_channel_training(category_id, ctx.guild.id)

        await ctx.send("Categoria setada com sucesso.")

        
    @commands.command()
    async def help(self, ctx):
        await ctx.send(
            "Estou sendo desenvolvido, confira mais na minha pagina do github."
        )

async def setup(bot):
    await bot.add_cog(General(bot))