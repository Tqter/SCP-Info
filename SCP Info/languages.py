import urllib
import GetSCP
import discord
import datetime
import time
import json
import random
import council_members
from discord.ext import commands
from builtins import bot

embed_color = discord.Colour(0x992d22)


class Languages(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self):
        self.bot = bot

    @commands.command()
    async def french(self, ctx, off_on):
        if off_on == "on":
            is_french = True
        else:
            is_french = False

        with open('french.json', 'a') as french:
            data = json.load(french)
            json.dump(f'\n{{"{ctx.guild.id}":{is_french}}}', data)
