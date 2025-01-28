from Fly_Bot import get_token
import discord
from discord.ext import commands
from logging import getLogger, DEBUG
from discord.utils import setup_logging
from Fly_Bot.translator import Translator
from dotenv import load_dotenv
import asyncio

# Setup logging
_log = getLogger(__name__)
setup_logging(
    # level=DEBUG
)

# Get envriomental variables.
load_dotenv()
TOKEN = get_token()


class Bot(commands.Bot):
    def __init__(self, command_prefix, *, help_command=None,
                 intents: discord.Intents):
        super().__init__(command_prefix=command_prefix,
                         help_command=help_command,
                         intents=intents)

    async def setup_hook(self):
        await self.tree.set_translator(Translator())
        await self.tree.sync()
        # await self.change_presence(activity=discord.Game(name=";help"))


intents = discord.Intents.all()
intents.reactions = True
intents.members = True
intents.messages = True
intents.dm_messages = True
bot = Bot(command_prefix=None,
          intents=intents)

asyncio.run(bot.load_extension("Akane.senders"))

bot.run(TOKEN)
