import discord
from discord import app_commands
from discord.ext import commands
from bd.models import Server, _Session

class Discord_Service(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    async def get_answer(self, ctx):
        def check(message):
            return (
                message.author == ctx.author and
                message.channel == ctx.channel
            )

        try:
            answer = await self.bot.wait_for(
                'message',
                check = check,
                timeout = 30
            )

            return answer.content

        except TimeoutError:
            return False

    def set_channel_training(self, channel, guild):
        with _Session() as sessao:

            categoria = Server(id_categoria_treino=channel, guild_id=guild)
            sessao.add(categoria)
            sessao.commit()

async def setup(bot):
    await bot.add_cog(Discord_Service(bot))   