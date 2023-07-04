import discord
from discord.ext import commands
import random
import requests, json

class Messages(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="주사위", with_app_command=True)
    async def dice(self, ctx: commands.Context):
        """ 주사위를 굴립니다. """
        await ctx.send(f'{random.randint(1, 6)} 이(가) 나왔습니다.')

    @commands.Cog.listener()
    async def on_message(self, message: discord.message.Message):
        """
        메시지가 입력되었을 때 실행되는 함수
        """
        # 서버장은 제외하도록
        if message.author == message.guild.owner:
            return
        #checkEmoji = ['🐍', '🪱']
        checkEmoji = []
        msg = message.content
        for check in checkEmoji:
            if msg.find(check) != -1:
                await message.delete()
                await message.channel.send(f"{message.author.mention}님, 해당 이모티콘은 사용하실 수 없습니다.")
                break

    @commands.hybrid_command(name="스포티파이", with_app_command=True)
    async def spotify(self, ctx: commands.Context):
        """ 현재 재생중인 노래 정보를 출력합니다. """
        # Slash Command를 이용하면 User의 Activity를 가져오지 못하는 문제?
        # 따라서 User ID를 가지고 유저 정보를 가져오기
        activities = discord.utils.get(ctx.guild.members, id=ctx.author.id).activities
        for activity in activities:
            if activity.name == "Spotify":
                embed = discord.Embed(title="Spotify Song🎵", description="현재 재생 중인 노래입니다.", color=activity.color)
                embed.set_thumbnail(url=activity.album_cover_url)
                embed.add_field(name="Title", value=activity.title, inline=True)
                embed.add_field(name="Artists", value=', '.join(activity.artists), inline=True)
                embed.add_field(name="Album", value=activity.album, inline=False)
                embed.add_field(name="Listen on Spotify", value=activity.track_url, inline=False)
                embed.set_footer(text=f"Created by {ctx.author}")

                msg = await ctx.send(embed=embed)
                await msg.add_reaction("🎵")
                return                
        return await ctx.send(f"{ctx.author.mention}님, 현재 노래를 듣고 있지 않습니다.")
    
    @commands.hybrid_command(name="서버", with_app_command=True)
    async def server(self, ctx: commands.Context):
        """ 마인크래프트 서버 정보를 가져옵니다. """
        import base64
        from io import BytesIO
        URL = "https://api.mcsrvstat.us/2/strayspeed.duckdns.org"
        url = requests.get(URL)
        text = url.text
        data: dict = json.loads(text)
        if data["online"]:
            embed = discord.Embed(title="현재 서버 상태 확인하기", description="Using mcsrvstat.us API", color=0x5CD0E5)
            embed.add_field(name="Motd", value="\n".join(data["motd"]["clean"]), inline=False)
            embed.add_field(name="서버 주소", value="strayspeed.duckdns.org" ,inline=False)
            embed.add_field(name="현재 서버 버전", value=data["version"], inline=False)
            embed.add_field(name="현재 서버 접속 인원", value=str(data["players"]["online"]) + " 명", inline=False)
            if data["players"]["online"] > 0:
                for player in data["players"]["list"]:
                    embed.add_field(name="접속자", value=player, inline=True)

            # 아래는 이미지 처리
            # base64형태라서 decode해야 함
            # decode -> discord에 임시 올리기 -> https 형태로
            if data.get("icon", None):
                file = discord.File(BytesIO(base64.b64decode(data["icon"].split(",")[-1])), filename="temp.png")
                embed.set_thumbnail(url="attachment://temp.png")
                await ctx.send(file=file, embed=embed)
            else:
                await ctx.send(embed=embed)
        else:
            await ctx.send("현재 서버가 오프라인입니다.")


async def setup(bot): # Cog를 추가하는 코루틴
    await bot.add_cog(Messages(bot)) # add the cog to the bot