import discord
import random
import asyncio
from discord.ext import commands
import time
from dotenv import load_dotenv
import os
import sqlite3
from Cogs.utils import get_prefix
import builtins

db = sqlite3.connect("database.db")

builtins.db = db


class MyBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        await generate_table()
        for guild in bot.guilds:
            db.execute("insert into guilds (GuildID) values (?)", (guild.id,))
            db.commit()
        print("Bot is ready.")


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.messages = True
bot = MyBot(command_prefix="'", intents=intents, case_insensitive=True)
builtins.bot = bot
import Cogs.misc as misc

bot.launch_time = time.time()

embed_color = discord.Colour(0x992d22)

access_denied = discord.Embed(
    title=':octagonal_sign:Uh Oh!', description=f"Looks like you don\'t have permission!",
    colour=discord.Colour(0x992d22)
)
access_denied.set_footer(
    text=f'Access Denied | Administrator Permission Required'
)


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
    db.execute("""
    CREATE TABLE IF NOT EXISTS guilds (
        GuildID integer PRIMARY KEY,
        Prefix text DEFAULT "\'",
        Language text DEFAULT "english"
    );""")
    db.commit()


import Cogs.scp as scp
import Cogs.admin_commands as admin_commands
import Cogs.beta as beta
import Cogs.languages as languages
import Cogs.settings as settings

bot.load_extension("Cogs.help")
bot.add_cog(scp.Foundation())
bot.add_cog(beta.Beta())
bot.add_cog(settings.Settings())
bot.add_cog(languages.Languages())
bot.add_cog(misc.Misc())
bot.add_cog(admin_commands.Administrator())

if __name__ == "__main__":
    bot.run(TOKEN)
