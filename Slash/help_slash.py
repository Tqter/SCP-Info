import discord
from discord.ext import commands
from Utils.utils import *
import datetime
from dislash import *
from builtins import bot, slash


class Help(commands.Cog):
    @slash.command(name="help", description="Get help with SCP Info")
    async def help(self, ctx):
        help_msg = "<:scp:830789987397009468> Foundation\n\n:gear: Settings\n\n:star: Misc\n\n [Invite](https://discord.com/oauth2/authorize?client_id=818294562677588009&permissions=2553671104&scope=bot) | [Support](https://discord.com/invite/hTPqf53abp) | [Website](https://www.scpinfo.xyz/) | [Vote](https://scpinfo.xyz/vote) | [Privacy Policy](https://scpinfo.xyz/privacy)"

        embed = discord.Embed(
            description=help_msg, color=embed_color,
            timestamp=datetime.datetime.now(datetime.timezone.utc))
        embed.set_footer(
            text=f"Press the buttons for more info.")
        embed.set_author(name="SCP Info - Help",
                         icon_url=bot.user.avatar_url)
        embed.set_thumbnail(
            url=ctx.guild.icon_url
        )

        misc_desc = "<:info:833058122213883905> `info` - Information about SCP Info\n<:code:830641334145777685> `code` - Link to SCP Info's GitHub repository\n:lock: `privacy` - Link to the privacy policy\n<a:countup:830789232431202336> `servercount` - Current number of servers SCP Info is in\n:exclamation: `prefix` - View your server's Prefix!\n:timer: `uptime` - Time since last restart\n<:website:833430346632658974> `website` - Official SCP Info website\n\n [Invite](https://discord.com/oauth2/authorize?client_id=818294562677588009&permissions=2553671104&scope=bot) | [Support](https://discord.com/invite/hTPqf53abp) | [Website](https://www.scpinfo.xyz/) | [Vote](https://scpinfo.xyz/vote) | [Privacy Policy](https://scpinfo.xyz/privacy)"
        embed_misc = discord.Embed(title=":star: Misc",
                                   description=misc_desc, color=embed_color,
                                   timestamp=datetime.datetime.now(datetime.timezone.utc))
        embed_misc.set_footer(
            text=f"Press the buttons for more info.")
        embed_misc.set_author(name="SCP Info - Help",
                              icon_url=bot.user.avatar_url)
        embed_misc.set_thumbnail(
            url=ctx.guild.icon_url
        )
        foundation_desc = "`O5` - Information about an O5 council member\n`classification` - Basic classification information\n`contain` - Attempt to contain a fellow user!\n`SCP` - Read the article of the SCP of your choosing\n\n [Invite](https://discord.com/oauth2/authorize?client_id=818294562677588009&permissions=2553671104&scope=bot) | [Support](https://discord.com/invite/hTPqf53abp) | [Website](https://www.scpinfo.xyz/) | [Vote](https://scpinfo.xyz/vote) | [Privacy Policy](https://scpinfo.xyz/privacy)"
        embed_foundation = discord.Embed(
            title="<:scp:830789987397009468> Foundation", description=foundation_desc, color=embed_color,
            timestamp=datetime.datetime.now(datetime.timezone.utc))
        embed_foundation.set_footer(
            text=f"Press the buttons for more info.")
        embed_foundation.set_author(name="SCP Info - Help",
                                    icon_url=bot.user.avatar_url)
        embed_foundation.set_thumbnail(
            url=ctx.guild.icon_url
        )
        settings_desc = ":pencil: `settings` - View SCP Info's Settings Menu\n\n [Invite](https://discord.com/oauth2/authorize?client_id=818294562677588009&permissions=2553671104&scope=bot) | [Support](https://discord.com/invite/hTPqf53abp) | [Website](https://www.scpinfo.xyz/) | [Vote](https://scpinfo.xyz/vote) | [Privacy Policy](https://scpinfo.xyz/privacy)"
        embed_settings = discord.Embed(title=":gear: Settings",
                                       description=settings_desc, color=embed_color,
                                       timestamp=datetime.datetime.now(datetime.timezone.utc))
        embed_settings.set_footer(
            text=f"Press the buttons for more info.")
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

   