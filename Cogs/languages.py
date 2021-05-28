import discord
from discord.ext import commands
from builtins import bot, db

embed_color = discord.Colour(0x992d22)

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


class Languages(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self):
        self.bot = bot


def get_language(guild_id):
    return db.execute("select Language from guilds where GuildID = ?", (guild_id,)).fetchone()[0]


def get_site(guild_id):
    return langauge_to_website[get_language(guild_id)]
