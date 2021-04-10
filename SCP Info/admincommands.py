import discord
from discord.ext import commands
from builtins import bot
import datetime


embed_color = discord.Colour(0x992d22)


access_denied = discord.Embed(
    title=':octagonal_sign:Uh Oh!', description=f"Looks like you don\'t have permission!", colour=discord.Colour(0x992d22)
)
access_denied.set_footer(
    text=f'Access Denied | Administrator Permission Required'
)

invalid_command = discord.Embed(
    title='"octagonal_sign:Invalid Command', description=f"Looks like that command doesn't exist! Try `'help`."
)

invalid_command.set_footer(
    text=f'Try another command!'
)


class CommandsAdministrator(commands.Cog):
    def __init__(self):
        self.bot = bot

    @commands.command(aliases=['r'])
    async def restart(self, ctx):
        author = ctx.message.author
        if ctx.author.id == int('704052817760878592'):
            embed_restart = discord.Embed(
                title=f'{bot.user.name} Restarting!',
                color=discord.Colour(0x992d22),
                timestamp=datetime.datetime.now(datetime.timezone.utc)
            )

            restart_success = await ctx.send(embed=embed_restart)
            await ctx.message.add_reaction('✅')
            await bot.close()

        else:
            restart_failure = await ctx.send(embed=access_denied)
            await ctx.message.add_reaction('🚫')