import discord
import random
import asyncio
from discord.ext import commands
from discord.ext import tasks
import time
from dotenv import load_dotenv
import os
import sqlite3
import builtins
import dbl

db = sqlite3.connect("database.db")

builtins.db = db


class MyBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # Let's us know when the bot comes online
    async def on_ready(self):
        print("Bot is ready.")

# Loads .env with info and passes it into a variable
load_dotenv()
TOKEN = os.getenv('Dev_Token')

# Declare intents
intents = discord.Intents.default()
intents.messages = True

# Initiate bot
bot = MyBot(command_prefix="'", intents=intents, case_insensitive=True)
builtins.bot = bot

# Import other Cog utils and set global variables
import Cogs.misc as misc
from Utils.utils import get_prefix, generate_table

bot.launch_time = time.time()

embed_color = discord.Colour(0x992d22)

access_denied = discord.Embed(
    title=':octagonal_sign:Uh Oh!', description=f"Looks like you don\'t have permission!",
    colour=discord.Colour(0x992d22)
)
access_denied.set_footer(
    text=f'Access Denied | Administrator Permission Required'
)

# Looks for and handles custom prefixes
@bot.event
async def on_message(message):
    ctx = await bot.get_context(message)
    if isinstance(ctx.channel, discord.channel.DMChannel):
        return
    else:
        prefix = get_prefix(ctx.guild.id)
    if message.content[0:len(prefix)] == prefix:
        message.content = f"'{message.content[len(prefix):len(message.content)]}"
        await bot.process_commands(message)
    else:
        await bot.process_commands(message)

# Changes prefix dynamically
async def ch_pr():
    await bot.wait_until_ready()

    while not bot.is_closed():
        statuses = ["SCP Info | 'help", f"on {len(bot.guilds)} servers! | 'help",
                    "with SCP-999", "'help | scpinfo.xyz", "on scpinfo.xyz", "with SCP-682", "SCP: Secret Laboratory"]

        status = random.choice(statuses)

        await bot.change_presence(activity=discord.Game(name=status))
        await asyncio.sleep(60)


bot.loop.create_task(ch_pr())

# Generates Language and Prefix tables

# @bot.command()
# async def gen(ctx):
#     await generate_table()
#     await ctx.send("Generated")

# Importing and loading Cogs
from Cogs import scp
from Cogs import beta
from Cogs import settings
from Cogs import languages
from Cogs import misc
from Cogs import admin_commands
from Cogs import help

bot.add_cog(help.Help())
bot.add_cog(scp.Foundation())
bot.add_cog(beta.Beta())
bot.add_cog(settings.Settings())
bot.add_cog(languages.Languages())
bot.add_cog(misc.Misc())
bot.add_cog(admin_commands.Administrator())

if __name__ == "__main__":
    bot.run(TOKEN)