import discord
from discord.ext import commands
from utils import developers
from builtins import bot, db
import datetime


embed_color = discord.Colour(0x992d22)


access_denied = discord.Embed(
    title=':octagonal_sign:Uh Oh!', description=f"Looks like you don\'t have permission!", colour=discord.Colour(0x992d22)
)
access_denied.set_footer(
    text=f'Access Denied | Administrator Permission Required'
)


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
        await ctx.send(embed=access_denied)
        await ctx.message.add_reaction("🚫")

    # @commands.command()
    # async def leave(self, ctx, get_server: int):
    #     if ctx.author.id == int('704052817760878592'):
    #         get_id = bot.get_guild(get_server)
    #         await get_id.leave()
    #         await ctx.send("Left that Server!")
    #
    #     else:
    #         leave_failure = await ctx.send(embed=access_denied)
    #         await ctx.message.add_reaction('🚫')
    #
    # @commands.command()
    # async def add(self, ctx):
    #     try:
    #         for guild in bot.guilds:
    #             db.execute("insert into guilds (GuildID) values(?)", (guild.id,))
    #             db.commit()
    #         await ctx.send("I did the funny!")
    #
    #     except:
    #         pass