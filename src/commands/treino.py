import discord
from discord import app_commands
from discord.ext import commands
from random import randint
from services.usuario import get_or_create_user
from math_engine.arithmetic import add
from services.treino import get_select

class Treino(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def treino(self, ctx):
        usuario = get_or_create_user(ctx)

        view = get_select()

        await ctx.reply(view=view)

    @commands.command()
    async def calcular(self, ctx):
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

            if int(answer.content) == add(question):
                await ctx.send('Acertou!')

            else:
                await ctx.send(f'Errou! A resposta era {add(question)}')
        except TimeoutError:
            await ctx.send('Você demorou para responder')
        except ValueError:
            await ctx.send('Digite apenas números')
    @commands.command()
    async def enviar_botao(self, ctx):
        async def oie(interaction: discord.Interaction):
            await interaction.response.send_message('Botão pressionado')

        view = discord.ui.View()
        button = discord.ui.Button(label='Botão', style=discord.ButtonStyle.red)    
        button.callback = oie

        view.add_item(button)

        await ctx.reply(view=view)

async def setup(bot):
    await bot.add_cog(Treino(bot))   