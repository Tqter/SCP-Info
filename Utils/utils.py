import sqlite3
import builtins
import discord
from discord.ext import commands
from builtins import bot

# Database handling
db = sqlite3.connect("database.db")
db.execute("""
CREATE TABLE IF NOT EXISTS guilds (
    GuildID integer PRIMARY KEY,
    Prefix text DEFAULT "'"
);""")
db.commit()
builtins.db = db

# Set global variables
command_emojis = {"info": "<:info:833058122213883905>", "code": "<:code:830641334145777685>", "privacy": ":lock:",
                  "servercount": "<countup:830789232431202336>", "uptime": ":timer:",
                  "website": "<website:833430346632658974>", "prefix": ":pencil:", "language": ":speaker:"}

langauge_to_website = {
    "english": "http://scpwiki.com/",
    "russian": "http://scp-ru.wikidot.com/",
    "korean": "http://ko.scp-wiki.net",
    "chinese": "http://scp-wiki-cn.wikidot.com/",
    "french": "http://fondationscp.wikidot.com/",
    "spanish": "http://lafundacionscp.wikidot.com/",
    "japanese": "http://scp-jp.wikidot.com/",
    "german": "http://scp-wiki-de.wikidot.com/"
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
    db.execute("drop table if exists guilds")
    db.execute("""
    CREATE TABLE guilds (
        GuildID integer PRIMARY KEY,
        Prefix text DEFAULT "\'",
        Language text DEFAULT "english"
    );""")
    db.commit()

def get_prefix(guild_id):
    data = db.execute("select prefix from guilds where GuildId = ?", (guild_id,)).fetchone()
    if data is None:
        db.execute("insert into guilds (GuildID) values (?)", (guild_id,))
        db.commit()
        return "'"
    else:
        return data[0]
