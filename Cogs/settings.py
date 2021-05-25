import discord
import datetime
import time
import languages
from discord.ext import commands
from builtins import bot, db
from utils import get_prefix

embed_color = discord.Colour(0x992d22)


class Settings(commands.Cog):
    def __init__(self):
        self.bot = bot

    @commands.group(pass_context=True, invoke_without_command=True, name="prefix")
    @commands.has_permissions(manage_guild=True)
    async def settings(self, ctx):
        embed_prefix = discord.Embed(
            title="Settings | Prefix",
            description=f"Settings to change SCP Info's Prefix!\n\n My Prefix for this Server is: `{get_prefix(ctx.guild.id)}`\n\n **:pencil:Change Prefix**: `{get_prefix(ctx.guild.id)}prefix set <new_prefix>`\n\n *:information_source:Make sure your new Prefix isn't longer than `5` characters! (e.g., `^`)*",
            colour=embed_color
        )
        await ctx.send(embed=embed_prefix)

    @settings.command(pass_context=True)
    @commands.has_permissions(manage_guild=True)
    async def prefix(self, ctx, new_prefix: str):
        embed_error_too_long = discord.Embed(
            title=":octagonal_sign:Whoops!",
            description="Your prefix can't be more than `5` Characters long!",
            colour=embed_color
        )

        if len(new_prefix) >= 5:
            await ctx.send(embed=embed_error_too_long)

        else:
            db.execute("UPDATE guilds SET Prefix = ? WHERE GuildID = ?", (new_prefix, ctx.guild.id))
            db.commit()
            await ctx.send(f"Set prefix to `{new_prefix}`!")

    @settings.command(pass_context=True)
    @commands.has_permissions(manage_guild=True)
    async def language(self, ctx, language: str):
        if language not in languages.langauge_to_website.keys():
            embed_error = discord.Embed(
                title=":octagonal_sign:Whoops!",
                description="Looks like we don't support that language yet...",
                colour=embed_color
            )
            await ctx.send(embed=embed_error)
            return

        else:
            db.execute("UPDATE guilds SET Language = ? WHERE GuildID = ?", (language, ctx.guild.id))
            db.commit()
            await ctx.send(f"Set language to `{language}`!")

    @settings.error
    async def change_prefix_error(self, ctx, error):
        embed_error = discord.Embed(
            title=":octagonal_sign:Whoops!",
            description="Looks like you don't have permission! Make sure you have the `manage_guild` permission!",
            colour=embed_color
        )
        await ctx.send(embed=embed_error)

    @prefix.error
    async def set_error(self, ctx, error):
        embed_error = discord.Embed(
            title=":octagonal_sign:Whoops!",
            description="Looks like you don't have permission! Make sure you have the `manage_guild` permission!",
            colour=embed_color
        )
        await ctx.send(embed=embed_error)
