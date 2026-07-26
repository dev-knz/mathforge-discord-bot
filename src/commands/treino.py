import discord
from discord import app_commands
from discord.ext import commands
from random import randint
from services.usuario import get_or_create_user

class Treino(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def treino(self, ctx):
        usuario = get_or_create_user(ctx)

        question = [randint(1,100), randint(1,100)]
        await ctx.send(f'Qual a resposta de: {question[0]} + {question[1]}')

        def check(message):
            return (
                message.author == ctx.author
                and message.channel == ctx.channel
            )

        try:
            answer = await self.bot.wait_for(
                'message',
                check=check,
                timeout = 30
            )

            if int(answer.content) == sum(question):
                await ctx.send('Acertou!')

            else:
                await ctx.send(f'Errou! A resposta era {sum(question)}')
        except TimeoutError:
            await ctx.send('Você demorou para responder')
        except ValueError:
            await ctx.send('Digite apenas números')


async def setup(bot):
    await bot.add_cog(Treino(bot))   