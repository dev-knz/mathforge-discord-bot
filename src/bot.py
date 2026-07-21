import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.all()

class MathBot(commands.Bot):
    
    def __init__(self):
        super().__init__(
            command_prefix = 'k!',
            help_command=None,
            intents = intents
        )

    async def setup_hook(self):
        await self.load_extension('commands.general')
        await self.load_extension('commands.arithmetic')
        await self.load_extension('commands.number_theory')
        await self.load_extension('commands.treino')
    
    async def on_ready(self):
        print(f'Bot conectado com sucesso.')

bot = MathBot()
bot.run(TOKEN)

