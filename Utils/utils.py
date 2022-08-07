import sqlite3
import builtins
import aiosqlite
import discord
from discord.ext import commands
from builtins import bot

# Set global variables

command_emojis = {"info": "<:info:833058122213883905>", "code": "<:code:830641334145777685>", "privacy": ":lock:",
                  "servercount": "<countup:830789232431202336>", "uptime": ":timer:",
                  "website": "<website:833430346632658974>", "prefix": ":pencil:", "language": ":speaker:"}

langauge_to_website = {
    "English": "http://scp-wiki.wikidot.com/",
    "Russian": "http://scp-ru.wikidot.com/",
    # "Korean": "http://ko.scp-wiki.net",
    "Chinese": "http://scp-wiki-cn.wikidot.com/",
    "French": "http://fondationscp.wikidot.com/",
    "Spanish": "http://lafundacionscp.wikidot.com/",
    "Japanese": "http://scp-jp.wikidot.com/",
    "German": "http://scp-wiki-de.wikidot.com/"
}
admin_access_denied = discord.Embed(
    title=':octagonal_sign:Uh Oh!', description=f"Looks like you don\'t have permission!", colour=discord.Colour(0x992d22)
)
admin_access_denied.set_footer(
    text=f'Access Denied | Administrator Permission Required'
)

developers = {704052817760878592: "Tqter",
              337619230583291904: "Keagan"}

embed_color = discord.Colour(0x992d22)

# Define functions
async def generate_table():
    async with aiosqlite.connect("database.db") as db:
        await db.execute("drop table if exists guilds")
        await db.execute("""
        CREATE TABLE guilds (
            GuildID integer PRIMARY KEY,
            Prefix text DEFAULT "\'",
            Language text DEFAULT "english"
        );""")
        await db.commit()

async def generate_place_table():
    async with aiosqlite.connect("database.db") as db:
        await db.execute("drop table if exists currentPlace")
        await db.execute("""
        CREATE TABLE currentPlace (
        MessageID integer PRIMARY KEY,
        Place integer DEFAULT 0
        );""")
        await db.commit()

async def get_prefix(guild_id):
    db = await aiosqlite.connect("database.db")
    cursor = await db.cursor()

    await cursor.execute("select prefix from guilds where GuildId = ?", (guild_id,))
    data = await cursor.fetchone()
    
    if data is None:
        await db.execute("insert into guilds (GuildID) values (?)", (guild_id,))
        await db.commit()
        await cursor.close()
        return "'"
    else:
        return data[0]

async def get_current_place(message_id):
    db = await aiosqlite.connect("database.db")
    cursor = await db.cursor()
    await cursor.execute("select place from currentPlace where MessageID = ?", (message_id,))
    data = await cursor.fetchone()

    if data is None:
        data = 0

    await cursor.close()
    return data

async def add_place(place, message_id):
    async with aiosqlite.connect("database.db") as db:
        await db.execute("UPDATE currentPlace SET Place = ? WHERE MessageID = ?", (place, message_id))
        await db.commit()
        await db.close()

