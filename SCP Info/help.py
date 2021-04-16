import discord
import datetime
from discord.ext import commands
from builtins import bot

embed_color = discord.Colour(0x992d22)


access_denied = discord.Embed(
    title=':octagonal_sign:Uh Oh!', description=f"Looks like you don\'t have permission!", colour=discord.Colour(0x992d22)
)
access_denied.set_footer(
    text=f'Access Denied • Administrator Permission Required'
)


class HelpCommand(commands.Cog):
    def __init__(self):
        self.bot = bot

    @commands.group(invoke_without_command=True, pass_context=True, aliases=['h'])
    async def help(self, ctx):
        class MyNewHelp(commands.MinimalHelpCommand):
            async def send_pages(self):
                author = ctx.message.author
                destination = self.get_destination()
                for page in self.paginator.pages:
                    embed_help = discord.Embed(title="Help",
                        description=page,
                        colour=discord.Colour(0x992d22),
                        timestamp=datetime.datetime.now(datetime.timezone.utc))

                    await destination.send(embed=embed_help)

        bot.help_command = MyNewHelp()