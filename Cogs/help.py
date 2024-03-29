import discord
from discord.ext import commands
import Utils.utils as utils
import datetime
from builtins import bot

bot.remove_command("help")

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
    @commands.group(name="help", aliases=["h", "hel"], help="Displays this message", usage="help <category/command>",
                    pass_context=True, invoke_without_command=True)
    async def help(self, ctx, command_name: str = None):
        if isinstance(ctx, discord.DMChannel):
            prefix = "\'"
        else:
            prefix = await utils.get_prefix(ctx.guild.id)

        if command_name is None:
            help_msg = f"<:scp:830789987397009468> Foundation\n\n:gear: Settings\n\n:star: Misc\n\n [Invite](https://scpinfo.xyz/invite) | [Support](https://discord.com/invite/hTPqf53abp) | [Website](https://www.scpinfo.xyz/) | [Vote](https://scpinfo.xyz/vote) | [Privacy Policy](https://scpinfo.xyz/privacy)"
        else:
            command = await get_command(command_name)
            if command is None:
                await ctx.message.reply(f"`{command_name}` is not a recognized command.")
                return
            else:
                try:
                    emoji = f"{utils.command_emojis[command.name.lower()]} "
                except KeyError:
                    emoji = ""

                help_msg = f"*{command.help}*\n\nUsage:\n```{prefix}{command.usage}```\n\nAliases: {await get_aliases(command_name)}"
                help_title = f"{emoji}{command.name.capitalize()}"

        embed = discord.Embed(
            description=help_msg, color=utils.embed_color,
            timestamp=datetime.datetime.now(datetime.timezone.utc))
        embed.set_footer(
            text=f"Run 'help (category_name) for more info")
        embed.set_author(name="SCP Info - Help",
                         icon_url=bot.user.avatar_url)
        embed.set_thumbnail(
            url=ctx.guild.icon_url
        )

        misc_desc = "<:info:833058122213883905> `info` - Information about SCP Info\n<:code:830641334145777685> `code` - Link to SCP Info's GitHub repository\n:lock: `privacy` - Link to the privacy policy\n<a:countup:830789232431202336> `servercount` - Current number of servers SCP Info is in\n:exclamation: `prefix` - View your server's Prefix!\n:timer: `uptime` - Time since last restart\n<:website:833430346632658974> `website` - Official SCP Info website\n\n [Invite](https://scpinfo.xyz/invite) | [Support](https://discord.com/invite/hTPqf53abp) | [Website](https://www.scpinfo.xyz/) | [Vote](https://scpinfo.xyz/vote) | [Privacy Policy](https://scpinfo.xyz/privacy)"
        embed_misc = discord.Embed(title=":star: Misc",
                                   description=misc_desc, color=utils.embed_color,
                                   timestamp=datetime.datetime.now(datetime.timezone.utc))
        embed_misc.set_footer(
            text=f"Run 'help (command_name) for more info")
        embed_misc.set_author(name="SCP Info - Help",
                              icon_url=bot.user.avatar_url)
        embed_misc.set_thumbnail(
            url=ctx.guild.icon_url
        )
        foundation_desc = "`O5` - Information about an O5 council member\n`classification` - Basic classification information\n`contain` - Attempt to contain a fellow user!\n`SCP` - Read the article of the SCP of your choosing\n\n [Invite](https://scpinfo.xyz/invite) | [Support](https://discord.com/invite/hTPqf53abp) | [Website](https://www.scpinfo.xyz/) | [Vote](https://scpinfo.xyz/vote) | [Privacy Policy](https://scpinfo.xyz/privacy)"
        embed_foundation = discord.Embed(
            title="<:scp:830789987397009468> Foundation", description=foundation_desc, color=utils.embed_color,
            timestamp=datetime.datetime.now(datetime.timezone.utc))
        embed_foundation.set_footer(
            text=f"Run 'help (command_name) for more info")
        embed_foundation.set_author(name="SCP Info - Help",
                                    icon_url=bot.user.avatar_url)
        embed_foundation.set_thumbnail(
            url=ctx.guild.icon_url
        )
        settings_desc = ":pencil: `settings` - View SCP Info's Settings Menu\n\n [Invite](https://scpinfo.xyz/invite) | [Support](https://discord.com/invite/hTPqf53abp) | [Website](https://www.scpinfo.xyz/) | [Vote](https://scpinfo.xyz/vote) | [Privacy Policy](https://scpinfo.xyz/privacy)"
        embed_settings = discord.Embed(title=":gear: Settings",
                                       description=settings_desc, color=utils.embed_color,
                                       timestamp=datetime.datetime.now(datetime.timezone.utc))
        embed_settings.set_footer(
            text=f"Run 'help (command_name) for more info")
        embed_settings.set_author(name="SCP Info - Help",
                                  icon_url=bot.user.avatar_url)
        embed_settings.set_thumbnail(
            url=ctx.guild.icon_url
        )

        message = await ctx.send(embed=embed)

        await message.add_reaction("<:scp:830789987397009468>")
        await message.add_reaction("⚙️")
        await message.add_reaction("⭐")
        await message.add_reaction("🏠")

        while True:
            reaction, member = await bot.wait_for('reaction_add')

            if member.id != ctx.author.id or reaction.message.id != message.id or member.bot:
                continue

            if str(reaction.emoji) == "<:scp:830789987397009468>":
                await message.edit(embed=embed_foundation)
                await message.remove_reaction(emoji="<:scp:830789987397009468>", member=ctx.author)

            elif reaction.emoji == "⚙️":
                await message.edit(embed=embed_settings)
                await message.remove_reaction(emoji="⚙️", member=ctx.author)

            elif reaction.emoji == "⭐":
                await message.edit(embed=embed_misc)
                await message.remove_reaction(emoji="⭐", member=ctx.author)

            elif reaction.emoji == "🏠":
                await message.edit(embed=embed)
                await message.remove_reaction(emoji="🏠", member=ctx.author)

    @help.command(pass_context=True, help="Displays the \"Misc\" help message",
                  usage="help misc")
    async def misc(self, ctx):
        desc = "<:info:833058122213883905> `info` - Information about SCP Info\n<:code:830641334145777685> `code` - Link to SCP Info's GitHub repository\n:lock: `privacy` - Link to the privacy policy\n<a:countup:830789232431202336> `servercount` - Current number of servers SCP Info is in\n:exclamation: `prefix` - View your server's Prefix!\n:timer: `uptime` - Time since last restart\n<:website:833430346632658974> `website` - Official SCP Info website\n\n [Invite](https://scpinfo.xyz/invite) | [Support](https://discord.com/invite/hTPqf53abp) | [Website](https://www.scpinfo.xyz/) | [Vote](https://scpinfo.xyz/vote) | [Privacy Policy](https://scpinfo.xyz/privacy)"
        embed = discord.Embed(title=":star: Misc",
                              description=desc, color=utils.embed_color,
                              timestamp=datetime.datetime.now(datetime.timezone.utc))
        embed.set_footer(
            text=f"Run 'help (command_name) for more info")
        embed.set_author(name="SCP Info - Help",
                         icon_url=bot.user.avatar_url)
        embed.set_thumbnail(
            url=ctx.guild.icon_url
        )
        await ctx.send(embed=embed)

    @help.command(pass_context=True, aliases=["f"], help="Displays the \"Foundation\" help message",
                  usage="help foundation")
    async def foundation(self, ctx):
        desc = "`O5` - Information about an O5 council member\n`classification` - Basic classification information\n`contain` - Attempt to contain a fellow user!\n`SCP` - Read the article of the SCP of your choosing\n\n [Invite](https://scpinfo.xyz/invite) | [Support](https://discord.com/invite/hTPqf53abp) | [Website](https://www.scpinfo.xyz/) | [Vote](https://scpinfo.xyz/vote) | [Privacy Policy](https://scpinfo.xyz/privacy)"
        embed = discord.Embed(
            title="<:scp:830789987397009468> Foundation", description=desc, color=utils.embed_color,
            timestamp=datetime.datetime.now(datetime.timezone.utc))
        embed.set_footer(
            text=f"Run 'help (command_name) for more info")
        embed.set_author(name="SCP Info - Help",
                         icon_url=bot.user.avatar_url)
        embed.set_thumbnail(
            url=ctx.guild.icon_url
        )
        await ctx.send(embed=embed)

    @help.command(pass_context=True, aliases=["setting", "s"], help="Displays the \"Settings\" help message",
                  usage="help settings")
    async def settings(self, ctx):
        desc = ":pencil: `settings` - View SCP Info's Settings Menu\n\n [Invite](https://scpinfo.xyz/invite) | [Support](https://discord.com/invite/hTPqf53abp) | [Website](https://www.scpinfo.xyz/) | [Vote](https://scpinfo.xyz/vote) | [Privacy Policy](https://scpinfo.xyz/privacy)"
        embed = discord.Embed(title=":gear: Settings",
                              description=desc, color=utils.embed_color,
                              timestamp=datetime.datetime.now(datetime.timezone.utc))
        embed.set_footer(
            text=f"Run 'help (command_name) for more info")
        embed.set_author(name="SCP Info - Help",
                         icon_url=bot.user.avatar_url)
        embed.set_thumbnail(
            url=ctx.guild.icon_url
        )
        await ctx.send(embed=embed)
