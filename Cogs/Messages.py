import discord
from discord.ext import commands
import random

class Messages(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="주사위", with_app_command=True)
    async def dice(self, ctx: commands.Context):
        """ 주사위를 굴립니다. """
        await ctx.send(f'{random.randint(1, 6)} 이(가) 나왔습니다.')


async def setup(bot): # Cog를 추가하는 코루틴
    await bot.add_cog(Messages(bot)) # add the cog to the bot