import discord
import os
from discord.ext import commands

with open(os.path.join(os.path.dirname(__file__), "thriller_keys.txt")) as f:
    thriller_token, thriller_id = f.readline().strip().split(" ")

intents = discord.Intents.default()
intents.message_content = True

class ThrillerBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="!",
            case_insensitive=False,
            help_command=None,
            description="도움말 제목",
            intents=intents.all(),
            sync_command=True,
        )
        self.thrillerCogs = ["Greetings", "Help"]

    async def setup_hook(self):
        for cog in self.thrillerCogs:
            await self.load_extension(f'Cogs.{cog}')
        await bot.tree.sync()

    async def on_ready(self):
        print("ready!")
        activity = discord.Game("!도움말 입력")
        await self.change_presence(status=discord.Status.online, activity=activity)

bot = ThrillerBot()
bot.run(thriller_token)