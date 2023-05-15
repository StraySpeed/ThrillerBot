import discord
from discord.ext import commands
from Cogs.ArmyData import ArmyData

class Army(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="군대", with_app_command=True)
    async def army(self, ctx, *, member: discord.Member = None):
        """ 군대 정보를 출력합니다. """
        member = member or ctx.author
        await ctx.send(f'{member.mention} 님은 {ArmyData.getInfo(member.id)}')


async def setup(bot): # Cog를 추가하는 코루틴
    await bot.add_cog(Army(bot)) # add the cog to the bot