import discord
import random
import asyncio
from discord.ext import commands, tasks
import GetSCP
from dotenv import load_dotenv
from itertools import cycle
import os
import datetime
import builtins
import urllib

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="'", intents=intents, case_insensitive=True)

builtins.bot = bot

embed_color = discord.Colour(0x992d22)

access_denied = discord.Embed(
    title=':octagonal_sign:Uh Oh!', description=f"Looks like you don\'t have permission!", colour=discord.Colour(0x992d22)
)
access_denied.set_footer(
    text=f'Access Denied | Administrator Permission Required'
)


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="SCP Info | 'help"))
    print("We are up!")

@bot.event
async def on_guild_join(guild):
    embed_added = discord.Embed(
        title="Thanks for adding me to your Server!",
        description="Hello! Thanks so much for adding me! I will now attempt to give a brief rundown of what I can do. Just to get this out of the way, my prefix is `'`.\n\n Using high powered python packages, I am able to search the web for any SCP you specify. This is my main command, you can try it by running `'scp (number)`. I also have various other commands such as 05 council member info, fun containment commands to fool your friends, and much more!.\n\n For info on any commands I have, run `'help` in your server! You may also join the [Support Server](https://discord.gg/DaWMTsXUYZ) for any questions, concerns, or ideas!",
        colour=discord.Colour(3066993)
    )
    embed_added.set_footer(
        text=f"Thanks for adding me {guild.owner}! | Hope you enjoy my company :D"
    )

    await guild.owner.send(embed=embed_added)



@bot.command(aliases=['i'])
async def invite(ctx):
    author = ctx.message.author
    embed_invite = discord.Embed(
        title='Invite me to Your Server!', description='Click [here](https://discord.com/api/oauth2/authorize?client_id=818294562677588009&permissions=2553671104&scope=bot) to invite me to your server!', colour=discord.Colour(0x992d22)
    )

    await ctx.send(embed=embed_invite)


@bot.command(aliases=['s'])
async def support(ctx):
    author = ctx.message.author
    embed_updates = discord.Embed(
        title="Updates", description=f"Do you need help or have suggestions/bugs? Well then join the [Support Server](https://discord.gg/DaWMTsXUYZ).", colour=discord.Colour(0x992d22)
    )
    await ctx.send(embed=embed_updates)


@bot.command(aliases=['c'])
async def code(ctx):
    embed_code = discord.Embed(
        title="Code", description='This bot is currently not open source.', colour=discord.Colour(0x992d22)
    )
    await ctx.send(embed=embed_code)

@bot.command(aliases=['v'])
async def vote(ctx):
    embed_vote = discord.Embed(
        title='Support SCP Info', description='Click [here](https://top.gg/bot/818294562677588009/vote) to vote for SCP Info!', colour=embed_color
    )
    await ctx.send(embed=embed_vote)



@bot.command(aliases=['servers'])
async def servercount(ctx):
    author = ctx.message.author
    embed_serverCount = discord.Embed(
        title='Server Count', description=f'I\'m in **{len(bot.guilds)}** servers!', colour=discord.Colour(0x992d22),
        timestamp=datetime.datetime.now(datetime.timezone.utc)
    )

    await ctx.send(embed=embed_serverCount)


@bot.command()
async def contain(ctx, user: discord.Member):
    author = ctx.message.author
    id_contain = str(user.id)
    contain_list = [
        f'{author.mention} contained <@{id_contain}>, termination cause **Micro-HID**.',
        f'{author.mention} was ripped to shreds by <@{id_contain}> in an attempt to contain them.',
        f'{author.mention} contained <@{id_contain}>, termination cause **P90**.',
        f'{author.mention} contained <@{id_contain}>, termination cause **SCP-018.**',
        f'{author.mention} was ripped to shreds by <@{id_contain}> in an attempt to contain them.',
        f'{author.mention} died to puncture wounds while trying to contain <@{id_contain}>.',
        f'{author.mention} contained <@{id_contain}>, termination cause **Micro-HID**.',
        f'{author.mention} died to automatic security while running from <@{id_contain}>.',
        f'{author.mention} contained <@{id_contain}>, termination cause **Frag Grenade**.',
        f'{author.mention} died to puncture wounds while trying to contain <@{id_contain}>.',
        f'{author.mention} got their neck snapped while trying to contain <@{id_contain}>.',
        f'{author.mention} contained <@{id_contain}>, termination cause **SCP-018.**',
        f'{author.mention} died to automatic security while running from <@{id_contain}>.',
        f'{author.mention} was sent to another dimension in an attempt to contain <@{id_contain}>.',
        f'{author.mention} died to automatic security while running from <@{id_contain}>.',
        f'{author.mention} contained <@{id_contain}>, termination cause **Micro-HID**.',
        f'{author.mention} was ripped to shreds by <@{id_contain}> in an attempt to contain them.',
        f'{author.mention} contained <@{id_contain}>, termination cause **P90**.',
        f'{author.mention} contained <@{id_contain}>, termination cause **SCP-018.**',
        f'{author.mention} was ripped to shreds by <@{id_contain}> in an attempt to contain them.',
        f'{author.mention} died to puncture wounds while trying to contain <@{id_contain}>.',
        f'{author.mention} contained <@{id_contain}>, termination cause **Micro-HID**.',
        f'{author.mention} died to automatic security while running from <@{id_contain}>.',
        f'{author.mention} contained <@{id_contain}>, termination cause **Frag Grenade**.',
        f'{author.mention} died to puncture wounds while trying to contain <@{id_contain}>.',
        f'{author.mention} got their neck snapped while trying to contain <@{id_contain}>.',
        f'{author.mention} contained <@{id_contain}>, termination cause **SCP-018.**',
        f'{author.mention} died to automatic security while running from <@{id_contain}>.',
        f'{author.mention} was sent to another dimension in an attempt to contain <@{id_contain}>.',
        f'{author.mention} died to automatic security while running from <@{id_contain}>.',
        f'{author.mention} contained <@{id_contain}>, termination cause **Micro-HID**.',
        f'{author.mention} was ripped to shreds by <@{id_contain}> in an attempt to contain them.',
        f'{author.mention} contained <@{id_contain}>, termination cause **P90**.',
        f'{author.mention} contained <@{id_contain}>, termination cause **SCP-018.**',
        f'{author.mention} was ripped to shreds by <@{id_contain}> in an attempt to contain them.',
        f'{author.mention} died to puncture wounds while trying to contain <@{id_contain}>.',
        f'{author.mention} contained <@{id_contain}>, termination cause **Micro-HID**.',
        f'{author.mention} died to automatic security while running from <@{id_contain}>.',
        f'{author.mention} contained <@{id_contain}>, termination cause **Frag Grenade**.',
        f'{author.mention} died to puncture wounds while trying to contain <@{id_contain}>.',
        f'{author.mention} got their neck snapped while trying to contain <@{id_contain}>.',
        f'{author.mention} contained <@{id_contain}>, termination cause **SCP-018.**',
        f'{author.mention} died to automatic security while running from <@{id_contain}>.',
        f'{author.mention} was sent to another dimension in an attempt to contain <@{id_contain}>.',
        f'{author.mention} died to automatic security while running from <@{id_contain}>.',
    ]
    await ctx.send(random.choice(contain_list))



import scp
import admincommands
import help
import council
bot.add_cog(scp.CommandSCP())
bot.add_cog(council.Council())
bot.remove_command('help')
bot.add_cog(help.CommandsHelp())
bot.add_cog(admincommands.CommandsAdministrator())
bot.run(TOKEN)
