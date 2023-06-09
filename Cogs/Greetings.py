import discord
from discord.ext import commands

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        """
        Event를 가져오려면 @commands.Cog.listener()를 사용
        """
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f'{member.mention} 님, {member.guild}에 어서오세요!')

    @commands.hybrid_command(name="안녕", with_app_command=True)
    async def hello(self, ctx: commands.Context, *, member: discord.Member = None):
        """ 안녕을 출력합니다. """
        member = member or ctx.author
        await ctx.send(f'{member.mention} 님, 안녕하세요!')


async def setup(bot): # Cog를 추가하는 코루틴
    await bot.add_cog(Greetings(bot)) # add the cog to the bot