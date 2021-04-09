import discord
import random
import asyncio
from discord.ext import commands, tasks
import GetSCP
from dotenv import load_dotenv
from itertools import cycle
import os
import builtins
import urllib

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="'", intents=intents)
bot.remove_command('help')

builtins.bot = bot

access_denied = discord.Embed(
    title=':octagonal_sign:Uh Oh!', description=f"Looks like you don\'t have permission!", colour=discord.Colour(0x992d22)
)
access_denied.set_footer(
    text=f'Access Denied | Administrator Permission Required'
)

invalid_command = discord.Embed(
    title='"octagonal_sign:Invalid Command', description=f"Looks like that command doesn't exist! Try `'help`."
)

invalid_command.set_footer(
    text=f'Try another command!'
)


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="SCP Info | 'help"))
    print("We are up!")


@bot.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    embed_help = discord.Embed(
        title="Help", description=f"Hi! I am a Discord bot focused on giving you info on any SCP of your choice!\n\n **Prefix:** `'`\n\n **General**\n\n :question: `'help` | Shows this Message\n\n :question: `'scp (number)` | Displays info on the specified SCP\n\n **Misc**\n\n :question: `'code` | Brings you to this bot's GitHub Repository\n\n :question: `'contain (user)` | Contains specified user. But be careful, it's risky!\n\n :question: `'support` | In case you want help or news on Updates and Fixes\n\n :question: `'servercount` | In case you wanna know how many servers this bot is in!\n\n :question: `'invite` | In case you wanna invite this bot to your server! HINT: You should!\n\n [Invite](https://discord.com/api/oauth2/authorize?client_id=818294562677588009&permissions=2553671104&scope=bot) | [Support](https://discord.gg/DaWMTsXUYZ)", colour=discord.Colour(0x992d22))

    embed_help.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)

    embed_help.set_footer(
        text=f"SCP Info | Created by Tqter#1696"
    )

    await ctx.send(embed=embed_help)


@bot.command()
async def invite(ctx):
    author = ctx.message.author
    embed_invite = discord.Embed(
        title='Invite me to Your Server!', description='Click [here](https://discord.com/api/oauth2/authorize?client_id=818294562677588009&permissions=2553671104&scope=bot) to invite me to your server!', colour=discord.Colour(0x992d22)
    )

    await ctx.send(embed=embed_invite)


@bot.command()
async def support(ctx):
    author = ctx.message.author
    embed_updates = discord.Embed(
        title="Updates", description=f"Do you need help or have suggestions/bugs? Well then join the [Support Server](https://discord.gg/DaWMTsXUYZ).", colour=discord.Colour(0x992d22)
    )
    await ctx.send(embed=embed_updates)


@bot.command()
async def code(ctx):
    embed_code = discord.Embed(
        title="Code", description='This bot is currently not open source.', colour=discord.Colour(0x992d22)
    )
    await ctx.send(embed=embed_code)


@bot.command()
async def servercount(ctx):
    author = ctx.message.author
    embed_serverCount = discord.Embed(
        title='Server Count', description=f'I\'m in **{len(bot.guilds)}** servers!', colour=discord.Colour(0x992d22)
    )

    embed_serverCount.set_footer(
        text=f'Administrator Command | Access Granted'
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
bot.add_cog(scp.CommandSCP())
bot.run(TOKEN)
