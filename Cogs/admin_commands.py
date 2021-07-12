import discord
from discord.ext import commands
import Utils.utils as utils
from builtins import bot, db
import datetime


class Administrator(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self):
        self.bot = bot

    @commands.command(aliases=['r'])
    async def restart(self, ctx):
        author = ctx.message.author
        for developer in utils.developers[ctx.author.id]:
            embed_restart = discord.Embed(
                title=f'{bot.user.name} Restarting!',
                color=discord.Colour(0x992d22),
                timestamp=datetime.datetime.now(datetime.timezone.utc)
            )

            embed_restart.set_footer(
                text=f"Command invoked by {ctx.message.author.name}", icon_url=author.avatar.url
            )

            await ctx.message.add_reaction('✅')
            restart_success = await ctx.send(embed=embed_restart)
            await bot.close()

    @restart.error
    async def restart_error(self, ctx, error):
        await ctx.send(embed=utils.admin_access_denied)
        await ctx.message.add_reaction("🚫")
