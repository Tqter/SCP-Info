import discord
from discord.ext import commands
import Cogs.utils as utils
from datetime import datetime
from builtins import bot

bot.remove_command("help")

embed_color = 0x992d22
command_emojis = {"info": "<:info:833058122213883905>", "code": "<:code:830641334145777685>", "privacy": ":lock:",
                  "servercount": "<countup:830789232431202336>", "uptime": ":timer:",
                  "website": "<website:833430346632658974>", "prefix": ":pencil:", "language": ":speaker:"}


async def get_aliases(command_name: str):
    aliases = ""
    command = await get_command(command_name)
    for alias in command.aliases:
        aliases += f"{alias}"
        if alias == command.aliases[-1]:
            aliases += ""
        else:
            aliases += ", "
    if aliases == "":
        return "`No Aliases.`"
    return f"`{aliases}`"


async def get_command(command_name: str):
    command = bot.get_command(name=command_name)
    return command


class Help(commands.Cog):
    @commands.group(name="help", aliases=["h", "hel"], help="Displays this message", usage="help <section/command>",
                    pass_context=True, invoke_without_command=True)
    async def help(self, ctx, command_name: str = None):
        if isinstance(ctx, discord.DMChannel):
            prefix = "\'"
        else:
            prefix = utils.get_prefix(ctx.guild.id)

        if command_name is None:
            help_msg = f"<:scp:830789987397009468> Foundation\n\n:gear: Settings\n\n:star: Misc"
            help_title = ":question: Help"
        else:
            command = await get_command(command_name)
            if command is None:
                await ctx.message.reply(f"`{command_name}` is not a recognized command.")
                return
            else:
                try:
                    emoji = f"{command_emojis[command.name.lower()]} "
                except KeyError:
                    emoji = ""

                help_msg = f"*{command.help}*\n\nUsage:\n```{prefix}{command.usage}```\n\nAliases: {await get_aliases(command_name)}"
                help_title = f"{emoji}{command.name.capitalize()}"

        embed = discord.Embed(title=help_title, description=help_msg, color=embed_color)
        embed.set_footer(text=f"Invoked by {ctx.author.display_name} - {datetime.now().strftime('%H:%M:%S')}")
        embed.set_author(name="SCP Info Help Menu", icon_url=bot.user.avatar_url)

        await ctx.send(embed=embed)

    @help.command(pass_context=True, help="Displays the \"Misc\" help message",
                  usage="help misc")
    async def misc(self, ctx):
        desc = "<:info:833058122213883905> Info - `Information about SCP Info`\n<:code:830641334145777685> Code - `Link to SCP Info's GitHub repository (currently private)`\n:lock: Privacy - `Link to the privacy policy`\n<countup:830789232431202336> servercount - `Current number of servers SCP Info is in`\n:timer: uptime - `Time since last restart`\n<website:833430346632658974> website - `Official SCP Info website`"
        embed = discord.Embed(title=":gear: Settings", description=desc, color=embed_color)
        embed.set_footer(text=f"Invoked by {ctx.author.display_name} - {datetime.now().strftime('%H:%M:%S')}")
        embed.set_author(name="SCP Info Help Menu", icon_url=bot.user.avatar_url)
        await ctx.send(embed=embed)

    @help.command(pass_context=True, aliases=["f"], help="Displays the \"Foudnation\" help message",
                  usage="help foundation")
    async def foundation(self, ctx):
        desc = "O5 - `Information about an O5 council member`\nClassification - `Basic classification information`\nContain - `Attempt to contain a fellow user!`\nSCP - `Read the article of the SCP of your choosing`"
        embed = discord.Embed(title="<:scp:830789987397009468> Foundation", description=desc, color=embed_color)
        embed.set_footer(text=f"Invoked by {ctx.author.display_name} - {datetime.now().strftime('%H:%M:%S')}")
        embed.set_author(name="SCP Info Help Menu", icon_url=bot.user.avatar_url)
        await ctx.send(embed=embed)

    @help.command(pass_context=True, aliases=["setting", "s"], help="Displays the \"Settings\" help message",
                  usage="help settings")
    async def settings(self, ctx):
        desc = ":pencil: Prefix - `Change the bot's server-wide prefix`\n\n:speaker: Language - `Change the server-wide language of the SCP articles`"
        embed = discord.Embed(title=":gear: Settings", description=desc, color=embed_color)
        embed.set_footer(text=f"Invoked by {ctx.author.display_name} - {datetime.now().strftime('%H:%M:%S')}")
        embed.set_author(name="SCP Info Help Menu", icon_url=bot.user.avatar_url)
        await ctx.send(embed=embed)
