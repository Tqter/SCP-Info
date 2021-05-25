import datetime
import time
from builtins import bot
from Cogs.utils import get_prefix
import discord
from discord.ext import commands

embed_color = discord.Colour(0x992d22)


class Misc(commands.Cog):
    def __init__(self):
        self.bot = bot

    @commands.command(aliases=['i'], help="Invite me to Your Server!")
    async def invite(self, ctx):
        author = ctx.message.author
        embed_invite = discord.Embed(
            title='<:invite:830789505212612629> Invite me to Your Server!',
            description='Click [here](https://discord.com/api/oauth2/authorize?client_id=818294562677588009&permissions=2553671104&scope=bot) to invite me to your server!',
            colour=discord.Colour(0x992d22)
        )

        await ctx.send(embed=embed_invite)

    @commands.command(aliases=['s'])
    async def support(self, ctx):
        author = ctx.message.author
        embed_updates = discord.Embed(
            title="<:ticket:833056259409969252> Support",
            description=f"Do you need help or have suggestions/bugs? Well then join the [Support Server](https://discord.gg/DaWMTsXUYZ).",
            colour=discord.Colour(0x992d22)
        )
        await ctx.send(embed=embed_updates)

    @commands.command(aliases=['c'], help="View my source code!")
    async def code(self, ctx):
        embed_code = discord.Embed(
            title="<:code:830641334145777685> Code", description='This bot is currently not open source.',
            colour=discord.Colour(0x992d22)
        )
        await ctx.send(embed=embed_code)

    @commands.command(aliases=['v'], help="Vote for me on [Top.gg](https://top.gg/bot/818294562677588009)!")
    async def vote(self, ctx):
        embed_vote = discord.Embed(
            title='<a:upvote:833057127098220544> Support SCP Info!',
            description='Click [here](https://scpinfo.xyz/vote) to vote for SCP Info!',
            colour=embed_color
        )
        await ctx.send(embed=embed_vote)

    @commands.command(aliases=['servers'], help="See how many Servers i'm in!")
    async def servercount(self, ctx):
        author = ctx.message.author
        embed_serverCount = discord.Embed(
            title=':file_folder: Server Count', description=f'I\'m in **{len(bot.guilds)}** servers!',
            colour=discord.Colour(0x992d22),
            timestamp=datetime.datetime.now(datetime.timezone.utc)
        )

        await ctx.send(embed=embed_serverCount)

    # @commands.command(aliases=['user'], help="See how many Active Users I have!")
    # async def users(self, ctx):
    #     author = ctx.message.author
    #     embed_users = discord.Embed(
    #         title='<:member_join:596576726163914752> Active Users', description=f'I have **{len(bot.users)}** users!',
    #         colour=discord.Colour(0x992d22),
    #         timestamp=datetime.datetime.now(datetime.timezone.utc)
    #     )
    #
    #     embed_users.set_footer(
    #         text=f"Command invoked by {ctx.message.author.name}", icon_url=author.avatar_url
    #     )
    #
    #     await ctx.send(embed=embed_users)

    @commands.command(pass_context=True)
    async def uptime(self, ctx):
        current_time = time.time()
        difference = int(round(current_time - bot.launch_time))
        text = str(datetime.timedelta(seconds=difference))
        embed = discord.Embed(title=":timer: Uptime",
                              description=text,
                              colour=embed_color,
                              timestamp=datetime.datetime.now(datetime.timezone.utc)
                              )
        try:
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send("Current uptime: " + text)

    @commands.command(aliases=["information"], help="Learn more about me!")
    async def info(self, ctx):
        author = ctx.message.author
        embed_info = discord.Embed(
            title="<:info:833058122213883905> About Me",
            description="Hi, i'm SCP info 👋! I was created as a fun little tool for the SCP Community. I can give info on SCPs, council members, and users! I also have many commands; view them all by running `'help`.",
            colour=embed_color
        )

        await ctx.send(embed=embed_info)

    @commands.command(aliases=['web'], help="View my [Website](https://www.scpinfo.xyz/)!")
    async def website(self, ctx):
        await ctx.send("https://scpinfo.xyz")

    @commands.command(aliases=["terms", "protection"], help="View my Privacy Policy and Terms of Service!")
    async def privacy(self, ctx):
        author = ctx.message.author
        embed_privacy = discord.Embed(
            title=":white_check_mark: Privacy",
            description="As of now, SCP Info does not collect ANY user information. If in the future we do and you run into a problem, please contact us at `scpinfoteam@gmail.com`. \n\nFor more information on our **websites** `Privacy` and `Terms of Service`, visit [Our Site](https://scpinfo.xyz/privacy)",
            colour=embed_color
        )

        await ctx.send(embed=embed_privacy)

    # @commands.command()
    # async def report(self, ctx):
    #     await ctx.send("Do you want to report a user for maliciously using SCP Info? (y/n)")
    #     yes_or_no = await bot.wait_for("message")
    #     if yes_or_no == "yes" or "no" or "y" or "n":
    #         await ctx.author.send("Please type the user you want to Report")
    #         message = await bot.wait_for("message")
    #         user = message.user_mentions[0]
    #         await ctx.author.send("Please type why you want to report this user")
    #         await bot.wait_for("message")
    #         reported = True
    #         if reported == True:
    #             await bot.owner.send(f"{ctx.message.author} reported {user}")
    #
    #         await ctx.send("Thanks! Your report has been processed and sent to Staff.")
