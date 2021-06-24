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

    async def on_ready(self):
        print("Bot is ready.")


load_dotenv()
TOKEN = os.getenv('Dev_Token')
DBL_Token = os.getenv('DBL_Token')

intents = discord.Intents.default()
intents.messages = True
bot = MyBot(command_prefix="'", intents=intents, case_insensitive=True)
builtins.bot = bot
bot.dblpy = dbl.DBLClient(bot, DBL_Token, autopost=True)
import Cogs.misc as misc
from Cogs.utils import get_prefix

bot.launch_time = time.time()

embed_color = discord.Colour(0x992d22)

access_denied = discord.Embed(
    title=':octagonal_sign:Uh Oh!', description=f"Looks like you don\'t have permission!",
    colour=discord.Colour(0x992d22)
)
access_denied.set_footer(
    text=f'Access Denied | Administrator Permission Required'
)


# @tasks.loop(minutes=30)
# async def update_stats():
#     """This function runs every 30 minutes to automatically update your server count."""
#     try:
#         await bot.dblpy.post_guild_count()
#         print(f'Posted server count ({bot.dblpy.guild_count})')
#     except Exception as e:
#         print('Failed to post server count\n{}: {}'.format(type(e).__name__, e))

# update_stats.start()


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


async def ch_pr():
    await bot.wait_until_ready()

    while not bot.is_closed():
        statuses = ["SCP Info | 'help", f"on {len(bot.guilds)} servers! | 'help",
                    "with SCP-999", "'help | scpinfo.xyz", "on scpinfo.xyz", "with SCP-682", "SCP: Secret Laboratory"]

        status = random.choice(statuses)

        await bot.change_presence(activity=discord.Game(name=status))
        await asyncio.sleep(60)


bot.loop.create_task(ch_pr())


async def generate_table():
    db.execute("drop table if exists guilds")
    db.execute("""
    CREATE TABLE guilds (
        GuildID integer PRIMARY KEY,
        Prefix text DEFAULT "\'",
        Language text DEFAULT "english"
    );""")
    db.commit()


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