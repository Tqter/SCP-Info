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


class MyNewHelp(commands.MinimalHelpCommand):
    async def send_pages(self):
        author = self.context.message.author
        destination = self.get_destination()
        for page in self.paginator.pages:
            embed_help = discord.Embed(
                                       description=page + "\n\n [Invite](https://discord.com/oauth2/authorize?client_id=818294562677588009&permissions=2553671104&scope=bot) | [Support](https://discord.com/invite/hTPqf53abp) | [Website](https://www.scpinfo.xyz/)",
                                       colour=discord.Colour(0x992d22),
                                       timestamp=datetime.datetime.now(datetime.timezone.utc))

            embed_help.set_author(
                name=str(bot.user.name) + " - Help",
                icon_url=str(bot.user.avatar_url)
            )

            embed_help.set_thumbnail(
                url=str(bot.user.avatar_url)
            )


            embed_help.set_footer(
                text=f"Command invoked by {self.context.message.author.name}", icon_url=author.avatar_url
            )

            await destination.send(embed=embed_help)

    def get_command_signature(self, command):
        return '{0.clean_prefix}{1.qualified_name} {1.signature}'.format(self, command)


class Other(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._original_help_command = bot.help_command
        bot.help_command = MyNewHelp()
        bot.help_command.cog = self

    def cog_unload(self):
        self.bot.help_command = self._original_help_command

def setup(bot):
    bot.add_cog(Other(bot))

