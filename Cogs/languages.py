import discord
import aiosqlite
from discord.ext import commands
import Utils.utils as utils
from builtins import bot


class Languages(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self):
        self.bot = bot


async def get_language(guild_id):
    db = await aiosqlite.connect("database.db")
    cursor = await db.cursor()

    await cursor.execute("select Language from guilds where GuildID = ?", (guild_id,))
    
    data = await cursor.fetchone()
    await cursor.close()

    return data[0]

def get_site(guild_id):
    return utils.langauge_to_website[get_language(guild_id)]
