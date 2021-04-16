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

    @commands.command(aliases=['i'])
    async def invite(self, ctx):
        author = ctx.message.author
        embed_invite = discord.Embed(
            title='Invite me to Your Server!',
            description='Click [here](https://discord.com/api/oauth2/authorize?client_id=818294562677588009&permissions=2553671104&scope=bot) to invite me to your server!',
            colour=discord.Colour(0x992d22)
        )

        await ctx.send(embed=embed_invite)

    @commands.command(aliases=['s'])
    async def support(self, ctx):
        author = ctx.message.author
        embed_updates = discord.Embed(
            title="Support",
            description=f"Do you need help or have suggestions/bugs? Well then join the [Support Server](https://discord.gg/DaWMTsXUYZ).",
            colour=discord.Colour(0x992d22)
        )
        await ctx.send(embed=embed_updates)

    @commands.command(aliases=['c'])
    async def code(self, ctx):
        embed_code = discord.Embed(
            title="Code", description='This bot is currently not open source.', colour=discord.Colour(0x992d22)
        )
        await ctx.send(embed=embed_code)

    @commands.command(aliases=['v'])
    async def vote(self, ctx):
        embed_vote = discord.Embed(
            title='Support SCP Info',
            description='Click [here](https://top.gg/bot/818294562677588009/vote) to vote for SCP Info!',
            colour=embed_color
        )
        await ctx.send(embed=embed_vote)

    @commands.command(aliases=['servers'])
    async def servercount(self, ctx):
        author = ctx.message.author
        embed_serverCount = discord.Embed(
            title='Server Count', description=f'I\'m in **{len(bot.guilds)}** servers!',
            colour=discord.Colour(0x992d22),
            timestamp=datetime.datetime.now(datetime.timezone.utc)
        )

        await ctx.send(embed=embed_serverCount)

    @commands.command(aliases=["information"])
    async def info(self, ctx):
        author = ctx.message.author
        embed_info = discord.Embed(
            title="About Me",
            description="Hi, i'm SCP info 👋! I was created as a fun little tool for the SCP Community. I can give info on SCPs, council members, and users! I also have many commands; view them all by running `'help`.",
            colour=embed_color
        )

        await ctx.send(embed=embed_info)