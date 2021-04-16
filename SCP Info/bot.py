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



import scp
import admincommands
import help
import misc
bot.add_cog(scp.Foundation())
bot.add_cog(misc.Misc())
bot.remove_command('help')
bot.add_cog(help.HelpCommand())
bot.add_cog(admincommands.Administrator())
bot.run(TOKEN)
