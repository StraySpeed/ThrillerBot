import discord
from discord.ext import commands
from Thriller_token import *

intents = discord.Intents.default()
intents.message_content = True

class ThrillerBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="!",
            case_insensitive=False,
            description="도움말 제목",
            intents=intents.all(),
            sync_command=True,
        )
        self.thrillerCogs = ["Greetings", "Help", "Messages", "Army"]

    async def setup_hook(self):
        for cog in self.thrillerCogs:
            await self.load_extension(f'Cogs.{cog}')
        await bot.tree.sync()

    async def on_ready(self):
        print("ready!")
        activity = discord.Game("!도움말 입력")
        await self.change_presence(status=discord.Status.online, activity=activity)

bot = ThrillerBot()
bot.run(THRILLER_TOKEN)