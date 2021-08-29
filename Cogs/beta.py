import discord
import datetime
import aiohttp
import random
from discord.ext import commands
import Utils.utils as utils
from builtins import bot



class Beta(commands.Cog):
    def __init__(self):
        self.bot = bot

    @commands.command(help="Grabs top images from [r/SCP](https://www.reddit.com/r/SCP/).", aliases=["images"], usage="image")
    async def image(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://www.reddit.com/r/SCP.json") as r:
                images = await r.json()

                author = ctx.message.author

                embed_reddit = discord.Embed(
                    title="Random SCP Image | BETA",
                    color=utils.embed_color,
                    timestamp=datetime.datetime.now(datetime.timezone.utc)
                )

                embed_reddit.set_image(
                    url=images["data"]['children'][random.randint(0, 25)]['data']['url'])

                embed_reddit.set_footer(
                    text=f"Command invoked by {ctx.message.author.name}", icon_url=author.avatar_url
                )

                await ctx.send(embed=embed_reddit)
