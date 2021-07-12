import discord
from discord.ext import commands
import Utils.utils as utils
from builtins import bot, db


class Languages(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self):
        self.bot = bot


def get_language(guild_id):
    return db.execute("select Language from guilds where GuildID = ?", (guild_id,)).fetchone()[0]


def get_site(guild_id):
    return utils.langauge_to_website[get_language(guild_id)]
