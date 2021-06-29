import sqlite3
import builtins
import discord
from discord.ext import commands
from builtins import bot

db = sqlite3.connect("database.db")
db.execute("""
CREATE TABLE IF NOT EXISTS guilds (
    GuildID integer PRIMARY KEY,
    Prefix text DEFAULT "'"
);""")
db.commit()
builtins.db = db

developers = {704052817760878592: "Tqter",
              337619230583291904: "Keagan"}
embed_color = discord.Colour(0x992d22)


def get_prefix(guild_id):
    data = db.execute(
        "select prefix from guilds where GuildId = ?", (guild_id,)).fetchone()
    if data is None:
        db.execute("insert into guilds (GuildID) values (?)", (guild_id,))
        db.commit()
        return "'"
    else:
        return data[0]
