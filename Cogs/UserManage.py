import discord
from datetime import timedelta
from discord.ext import commands

class UserManage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(kick_members=True)
    @commands.hybrid_command(name="강퇴", with_app_command=True)
    async def kick(self, ctx: commands.Context, member: discord.Member):
        """ 해당 유저를 강퇴시킵니다. """
        guild = ctx.guild
        await guild.kick(member)
        await ctx.send(f'{member.mention} 님을 강퇴했습니다.')

    @commands.has_permissions(ban_members=True)
    @commands.hybrid_command(name="차단", with_app_command=True)
    async def ban(self, ctx: commands.Context, member: discord.Member):
        """ 해당 유저를 밴합니다. """
        guild = ctx.guild
        await guild.ban(member)
        await ctx.send(f'{member.mention} 님을 밴했습니다.')

    @commands.has_permissions(moderate_members=True)
    @commands.hybrid_command(name="타임아웃", with_app_command=True)
    async def timeout(self, ctx: commands.Context, member: discord.Member, *, time: int = 60):
        """ 해당 유저를 TIME초 동안 타임아웃합니다. (기본 1분) """
        await member.timeout(timedelta(seconds=time))
        await ctx.send(f'{member.mention} 님을 {time}초 동안 타임아웃했습니다.')

    @commands.command(name="명명")
    async def self_kick(self, ctx: commands.Context):
        """ 자기 자신을 강퇴시킵니다. """
        guild = ctx.guild
        await guild.kick(ctx.author)
        await ctx.send("**어휴**")

    @self_kick.error
    @kick.error
    @ban.error
    @timeout.error
    async def user_manage_error(self, ctx: commands.Context, error: commands.errors):
        if isinstance(error, commands.errors.MissingPermissions):
            await ctx.send(f"{ctx.author.mention}님, 해당 권한이 없습니다.")
        elif isinstance(error, commands.errors.HybridCommandError):   # hybrid command error
            await ctx.send(f"{ctx.author.mention}님, 해당 명령어를 사용할 수 없습니다.")
        elif isinstance(error, commands.errors.MissingRequiredArgument) or isinstance(error, commands.errors.BadArgument):  # prefix command error
            await ctx.send(f"{ctx.author.mention}님, 명령어를 정확히 입력해 주세요.")
        else:
            await ctx.send(f"오류가 발생했습니다.")
            await ctx.send(f"{error.original}")


async def setup(bot): # Cog를 추가하는 코루틴
    await bot.add_cog(UserManage(bot)) # add the cog to the bot