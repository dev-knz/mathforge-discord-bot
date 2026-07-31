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

        # Definir a categoria ID, futuramente integrar isso em um comando
        guild = interaction.guild
        categoria = interaction.guild.get_channel(1532107144571125831)

        # Permissoes ; vou ajustar melhor isso aqui depois
        overwrites = {
        interaction.guild.default_role: discord.PermissionOverwrite(
        view_channel=False
        ),
        interaction.user: discord.PermissionOverwrite(
        view_channel=True,
        send_messages=True,
        read_message_history=True
        ),
        interaction.guild.me: discord.PermissionOverwrite(
        view_channel=True
        )
}
        canal = await interaction.guild.create_text_channel(f'treino-{interaction.user.name}', category=categoria, overwrites=overwrites)

        menuSelection.disabled = True
        await interaction.response.edit_message(
            view=view
        )

        await interaction.followup.send(
            f"Canal criado com sucesso, acesse aqui: {canal.mention}", ephemeral=True
        )
        
    menuSelection.callback = callback
    view = discord.ui.View()
    view.add_item(menuSelection)

    return view

