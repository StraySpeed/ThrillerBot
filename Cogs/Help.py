import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="도움말")
    async def help(self, ctx):
        """ 도움말을 출력합니다. """
        await ctx.send(f'도움말을 출력합니다.')


async def setup(bot): # Cog를 추가하는 코루틴
    await bot.add_cog(Help(bot)) # add the cog to the bot