import discord
from discord.ext import commands
import GetSCP
from dotenv import load_dotenv
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
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="SCP Info | 'help"))
    print("We are up!")


@bot.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    embed_help = discord.Embed(
        title="Help", description=f"Hi! I am a Discord bot focused on giving you info on any SCP of your choice!\n\n **Prefix:** `'`\n\n :question: `'help` | Shows this Message\n\n :question: `'scp (number)` | Displays info on the specified SCP\n\n :question: `'code` | Brings you to this bot's GitHub Repository", colour=discord.Colour(0x992d22))

    embed_help.set_footer(
        text=f"SCP Info | Created by Tqter#1696"
    )

    await ctx.send(embed=embed_help)


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

    if author.id == int('704052817760878592'):
        await ctx.send(embed=embed_serverCount)

    else:
        await ctx.send(embed=access_denied)

import scp
bot.add_cog(scp.CommandSCP())
bot.run(TOKEN)
