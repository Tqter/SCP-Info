import datetime
import time
from builtins import bot, slash
import Utils.utils as utils
import discord
from discord.ext import commands



class Misc_Slash(commands.Cog):
    def __init__(self):
        self.bot = bot

    
    @slash.command(name="invite", description="How to Invite SCP Info") 
    async def invite(self, inter):
        embed_invite = discord.Embed(
            title='<:invite:830789505212612629> Invite me to Your Server!',
            description='Click [here](https://scpinfo.xyz/invite) to invite me to your server!',
            colour=utils.embed_color
        )

        await inter.reply(embed=embed_invite)

    @slash.command(name="support", description="How to get Support for SCP Info" )
    async def support(self, inter):
        embed_updates = discord.Embed(
            title="<:ticket:833056259409969252> Support",
            description=f"Do you need help or have suggestions/bugs? Well then join the [Support Server](https://discord.gg/DaWMTsXUYZ).",
            colour=utils.embed_color
        )
        await inter.reply(embed=embed_updates)

    @slash.command(name="code", description="View SCP Info's source code" )
    async def code(self, inter):
        embed_code = discord.Embed(
            title="<:code:830641334145777685> Code", description='View my Source Code! [GitHub](https://github.com/Tqter/SCP-Info)',
            colour=utils.embed_color
        )
        await inter.reply(embed=embed_code)

    @slash.command(name="vote", description="How to Vote for SCP Info" )
    async def vote(self, inter):
        embed_vote = discord.Embed(
            title='<a:upvote:833057127098220544> Support SCP Info!',
            description='Click [here](https://scpinfo.xyz/vote) to vote for SCP Info!',
            colour=utils.embed_color
        )
        await inter.reply(embed=embed_vote)

    @slash.command(name="servers", description="View how many servers SCP Info is in" )
    async def servercount(self, inter):
        embed_serverCount = discord.Embed(
            title=':file_folder: Server Count', description=f'I\'m in **{len(bot.guilds)}** servers!',
            colour=discord.Colour(0x992d22),
            timestamp=datetime.datetime.now(datetime.timezone.utc)
        )
        await inter.reply(embed=embed_serverCount)

    @slash.command(name="uptime", description="See how long SCP Info has been running" )
    async def uptime(self, inter):
        current_time = time.time()
        difference = int(round(current_time - bot.launch_time))
        text = str(datetime.timedelta(seconds=difference))
        embed = discord.Embed(title=":timer: Uptime",
                              description=text,
                              colour=utils.embed_color,
                              timestamp=datetime.datetime.now(
                                  datetime.timezone.utc)
                              )
        try:
            await inter.reply(embed=embed)
        except discord.HTTPException:
            await inter.reply(embed="Current uptime: " + text)

    @slash.command(name="website", description="How to find SCP Info's Website" )
    async def website(self, inter):
        await inter.reply("https://scpinfo.xyz")

    @slash.command(name="privacy", description="View SCP Info's Privacy Policy" )
    async def privacy(self, inter):
        embed_privacy = discord.Embed(
            title=":white_check_mark: Privacy",
            description="As of now, SCP Info does not collect ANY user information. If in the future we do and you run into a problem, please contact us at `scpinfoteam@gmail.com`. \n\nFor more information on our **websites** `Privacy` and `Terms of Service`, visit [Our Site](https://scpinfo.xyz/privacy)",
            colour=utils.embed_color
        )

        await inter.reply(embed=embed_privacy)

    @slash.command(name="prefix", description="View your servers current Prefix" )
    async def prefix(self, inter):
        await inter.reply(f"My prefix for this Server is `{utils.get_prefix(inter.guild.id)}`!")