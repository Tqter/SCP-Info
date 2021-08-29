import discord
import datetime
import time
import aiosqlite
import Cogs.languages as languages
from discord.ext import commands
from builtins import bot
import Utils.utils as utils


class Settings(commands.Cog):
    def __init__(self):
        self.bot = bot

    @commands.group(pass_context=True, invoke_without_command=True, help="Settings for SCP Info!", usage="settings")
    @commands.has_permissions(manage_guild=True)
    async def settings(self, ctx):
        embed_settings = discord.Embed(
            title="SCP Info | Settings",
            description=f"Settings for SCP Info!\n\n React with :pencil: to edit the `Prefix` for this Server!\n\n React with :speaker: to change the `Language` of the `{await utils.get_prefix(ctx.guild.id)}scp` command for this Server!",
            colour=utils.embed_color
        )

        embed_prefix = discord.Embed(
            title="Settings | Prefix",
            description=f"Settings to change SCP Info's Prefix!\n\n :pencil:**Change Prefix**: `{await utils.get_prefix(ctx.guild.id)}settings prefix <new_prefix>`\n\n *:information_source:Make sure your new Prefix is no longer than `5` characters! (e.g., `^`)*",
            colour=utils.embed_color
        )

        embed_language = discord.Embed(
            title="Settings | Language",
            description=f"Settings to change the Language of the `{await utils.get_prefix(ctx.guild.id)}scp` command!\n\n :pencil:**Change Language**: `{await utils.get_prefix(ctx.guild.id)}settings language <new_language>`\n\n **:information_source:Valid Languages**:\n `English`\n `French`\n `Spanish`\n `Russian`\n `Chinese`\n `Japanese`\n `German`",
            colour=utils.embed_color
        )

        message = await ctx.send(embed=embed_settings)
        await message.add_reaction("📝")
        await message.add_reaction("🔈")
        await message.add_reaction("🏠")

        while True:
            reaction, member = await bot.wait_for('reaction_add')

            if member.id != ctx.author.id or reaction.message.id != message.id or member.bot:
                continue

            if reaction.emoji == "📝":
                await message.edit(embed=embed_prefix)
                await message.remove_reaction(emoji="📝", member=ctx.author)

            elif reaction.emoji == "🔈":
                await message.edit(embed=embed_language)
                await message.remove_reaction(emoji="🔈", member=ctx.author)

            elif reaction.emoji == "🏠":
                await message.edit(embed=embed_settings)
                await message.remove_reaction(emoji="🏠", member=ctx.author)

    @settings.command(pass_context=True, help="Change the Prefix for your Server!",
                      usage="settings prefix <New Prefix>")
    @commands.has_permissions(manage_guild=True)
    async def prefix(self, ctx, new_prefix: str):
        embed_error_too_long = discord.Embed(
            title=":octagonal_sign:Whoops!",
            description="Your prefix can't be more than `5` Characters long!",
            colour=utils.embed_color
        )

        if len(new_prefix) >= 5:
            await ctx.send(embed=embed_error_too_long)

        else:
            async with aiosqlite.connect("database.db") as db:
                await db.execute("UPDATE guilds SET Prefix = ? WHERE GuildID = ?", (new_prefix, ctx.guild.id))
                await db.commit()
                await ctx.send(f"Set prefix to `{new_prefix}`!")

    @settings.command(pass_context=True, help="Change the Language of the SCP command for your Server!",
                      usage="settings language <New Language>")
    @commands.has_permissions(manage_guild=True)
    async def language(self, ctx, new_language: str):
        if new_language not in utils.langauge_to_website.keys():
            embed_error = discord.Embed(
                title=":octagonal_sign:Whoops!",
                description="Looks like we don't support that language yet...",
                colour=utils.embed_color
            )
            await ctx.send(embed=embed_error)
            return

        else:
            async with aiosqlite.connect("database.db") as db:
                await db.execute("UPDATE guilds SET Language = ? WHERE GuildID = ?", (new_language, ctx.guild.id))
                await db.commit()
                await ctx.send(f"Set language to `{new_language}`!")

    @settings.error
    async def change_prefix_error(self, ctx, error):
        embed_error = discord.Embed(
            title=":octagonal_sign:Whoops!",
            description="Looks like you don't have permission! Make sure you have the `manage_guild` permission!",
            colour=utils.embed_color
        )
        await ctx.send(embed=embed_error)

    @prefix.error
    async def set_error(self, ctx, error):
        embed_error = discord.Embed(
            title=":octagonal_sign:Whoops!",
            description="Looks like you don't have permission! Make sure you have the `manage_guild` permission!",
            colour=utils.embed_color
        )
        await ctx.send(embed=embed_error)
