import discord
import datetime
import council_members
from discord.ext import commands
from builtins import bot

embed_color = discord.Colour(0x992d22)
bot.remove_command('help')


access_denied = discord.Embed(
    title=':octagonal_sign:Uh Oh!', description=f"Looks like you don\'t have permission!", colour=discord.Colour(0x992d22)
)
access_denied.set_footer(
    text=f'Access Denied • Administrator Permission Required'
)


class Council(commands.Cog):
    def __init__(self):
        self.bot = bot

    @commands.group(name='O5', pass_context=True, aliases=['05'])
    async def council(self, ctx, council_member: int):
        embed_error = discord.Embed(
            title=':octagonal_sign:Oops!', description='That isn\'t a valid O5 Council Member! Try `\'O5 {1 - 13}`',
            colour=discord.Colour(0x992d22))
        try:
            embed_council = discord.Embed(
                title=f'O5-{council_member}: "{(council_members.council_nickname[council_member])}"',
                description=(council_members.council_members[council_member]) + "\n\n **View other contradictory reports at**: [The SCP Wiki](http://www.scpwiki.com/o5-command-dossier)",
                colour=embed_color
            )
            await ctx.send(embed=embed_council)
        except:
            await ctx.send(embed=embed_error)
