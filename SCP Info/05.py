import discord
import datetime
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


class CommandsHelp(commands.Cog):
    def __init__(self):
        self.bot = bot

    @commands.group(name='05', invoke_without_command=True, pass_context=True)
    async def council(self, ctx, council_member: int):

        council_members = {1:"",
                           2:"",
                           3:"",
                           4:"",
                           5:"",
                           6:"",
                           7:"",
                           8:"",
                           9:"",
                           10:"",
                           11:"",
                           12:"",
                           13:"",



                           }

