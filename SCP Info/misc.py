import urllib
import GetSCP
import discord
import datetime
import random
import council_members
from discord.ext import commands
from builtins import bot

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
            title="<:code:830641334145777685> Code", description='This bot is currently not open source.', colour=discord.Colour(0x992d22)
        )
        await ctx.send(embed=embed_code)

    @commands.command(aliases=['v'], help="Vote for me on [Top.gg](https://top.gg/bot/818294562677588009)!")
    async def vote(self, ctx):
        embed_vote = discord.Embed(
            title='<a:upvote:833057127098220544> Support SCP Info!',
            description='Click [here](https://top.gg/bot/818294562677588009/vote) to vote for SCP Info!',
            colour=embed_color
        )
        await ctx.send(embed=embed_vote)

    @commands.command(aliases=['servers'], help="See how many Servers i'm in!")
    async def servercount(self, ctx):
        author = ctx.message.author
        embed_serverCount = discord.Embed(
            title='<a:countup:830789232431202336> Server Count', description=f'I\'m in **{len(bot.guilds)}** servers!',
            colour=discord.Colour(0x992d22),
            timestamp=datetime.datetime.now(datetime.timezone.utc)
        )

        await ctx.send(embed=embed_serverCount)

    @commands.command(aliases=["information"], help="Learn more about me!")
    async def info(self, ctx):
        author = ctx.message.author
        embed_info = discord.Embed(
            title="<:info:833058122213883905> About Me",
            description="Hi, i'm SCP info 👋! I was created as a fun little tool for the SCP Community. I can give info on SCPs, council members, and users! I also have many commands; view them all by running `'help`.",
            colour=embed_color
        )

        await ctx.send(embed=embed_info)