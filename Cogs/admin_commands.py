import discord
from discord.ext import commands
from Utils.utils import *
from builtins import bot
import datetime


class Administrator(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self):
        self.bot = bot
            

    @commands.command(aliases=['r'])
    async def restart(self, ctx):
        author = ctx.message.author
        for developer in developers[ctx.author.id]:
            embed_restart = discord.Embed(
                title=f'{bot.user.name} Restarting!',
                color=discord.Colour(0x992d22),
                timestamp=datetime.datetime.now(datetime.timezone.utc)
            )

            embed_restart.set_footer(
                text=f"Command invoked by {ctx.message.author.name}", icon_url=author.avatar_url
            )

            await ctx.message.add_reaction('✅')
            restart_success = await ctx.send(embed=embed_restart)
            await bot.close()

    @restart.error
    async def restart_error(self, ctx, error):
        await ctx.send(embed=admin_access_denied)
        await ctx.message.add_reaction("🚫")

    @commands.command()
    async def gen(self, ctx):
        for developer in developers[ctx.author.id]:
            await generate_place_table()
            # await generate_table()
            await ctx.send("Both tables Successfully Generated")

    @gen.error
    async def gen_error(self, ctx, error):
        await ctx.send(embed=admin_access_denied)
        await ctx.message.add_reaction("🚫")
    
        
