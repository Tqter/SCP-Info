import discord
import random
import asyncio
from discord.ext import commands, tasks
import dislash
from dislash.interactions import *
import time
from dotenv import load_dotenv
import os
import aiosqlite
import builtins
from discord.utils import find



class MyBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.ipc = ipc.Server(self, host="localhost", port=8767, secret_key = os.getenv("SECRET_KEY"))

    # Let's us know when the bot comes online
    async def on_ready(self):
        print("Bot is ready.")

    async def on_ipc_ready(self):
	    """Called upon the IPC Server being ready"""
	    print("Ipc server is ready.")

    async def on_ipc_error(self, endpoint, error):
	    """Called upon an error being raised within an IPC route"""
	    print(endpoint, "raised", error)

# Loads .env with info and passes it into a variable
load_dotenv()
TOKEN = os.getenv('Dev_Token')

# Declare intents
intents = discord.Intents.default()
intents.messages = True

# Initiate bot
bot = MyBot(command_prefix="'", intents=intents, case_insensitive=True)
slash = dislash.SlashClient(bot)
builtins.bot = bot
builtins.slash = slash

# Import other Cog utils
import Cogs.misc as misc
from Utils.utils import *

# Set global Variables
bot.launch_time = time.time()

# Look for and handles custom prefixes
@bot.event
async def on_message(message):
    ctx = await bot.get_context(message)
    if isinstance(ctx.channel, discord.channel.DMChannel):
        return
    else:
        prefix = await get_prefix(ctx.guild.id)
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

# @ipc.server.route()
# async def get_guild_count(data):
# 	return len(bot.guilds) # returns the len of the guilds to the client

# @ipc.server.route()
# async def get_guild_ids(data):
# 	final = []
# 	for guild in bot.guilds:
# 		final.append(guild.id)
# 	return final # returns the guild ids to the client

# @ipc.server.route()
# async def get_guild(data):
# 	guild = bot.get_guild(data.guild_id)
# 	if guild is None: return None

# 	guild_data = {
# 		"name": data,
# 		"id": data,
# 		"prefix" : "?"
# 	}

# 	return guild_data

# Importing and loading Cogs
from Cogs import scp
from Cogs import beta
from Cogs import settings
from Cogs import languages
from Cogs import misc
from Cogs import admin_commands
from Cogs import help

# Importing and loading Slash Cogs
from Slash import misc_slash
from Slash import scp_slash
from Slash import beta_slash
from Slash import settings_slash
from Slash import help_slash

# Normal Cogs
bot.add_cog(help.Help())
bot.add_cog(scp.Foundation())
bot.add_cog(beta.Beta())
bot.add_cog(settings.Settings())
bot.add_cog(languages.Languages())
bot.add_cog(misc.Misc())
bot.add_cog(admin_commands.Administrator())

# Slash Cogs
bot.add_cog(misc_slash.Misc_Slash())
bot.add_cog(scp_slash.SCP_Slash())
bot.add_cog(beta_slash.Beta_Slash())
bot.add_cog(help_slash.Help())
bot.add_cog(settings_slash.Settings_Slash())

if __name__ == "__main__":
    bot.run(TOKEN)