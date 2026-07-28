import discord
from discord import app_commands
from discord.ext import commands
from bd.models import _Session, Usuario, Estatistica, Progresso
from constants.categorias import Categoria

def get_options(interact: discord.Interaction):

    escolha = interact.data['values'][0]
    categorias = {}

    for index, categoria in enumerate(Categoria):
        categorias[f'{index}'] = f'{categoria.value}'
    escolhido = categorias[escolha]

    return escolhido

def get_select():

    menuSelection = discord.ui.Select(placeholder='Selecione uma área matemática')
    options = list()
    for index, categoria in enumerate(Categoria):
        options.append(discord.SelectOption(label=f'{categoria.value}', value=f'{index}'))

    menuSelection.options = options

    async def callback(interaction: discord.Interaction):
        escolhido = get_options(interact=interaction)
        menuSelection.disabled = True
        await interaction.response.edit_message(
            view=view
        )

        await interaction.followup.send(
            f"Área escolhida: {escolhido}"
        )
    menuSelection.callback = callback
    view = discord.ui.View()
    view.add_item(menuSelection)

    return view

