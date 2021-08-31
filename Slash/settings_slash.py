import discord
import datetime
import time
import aiosqlite
import asyncio
import Cogs.languages as languages
from discord.ext import commands
from dislash import *
from builtins import bot, slash
import Utils.utils as utils


class Settings_Slash(commands.Cog):
    def __init__(self):
        self.bot = bot

    @slash.command(name="settings", description="View the SCP Info Settings Menu" ) 
    @slash_commands.has_permissions(manage_guild=True)
    async def settings(self, ctx):
        pass

    @settings.sub_command(description="Change your Server's Prefix", options=[Option("new_prefix", "Enter a new Prefix (Can be no longer than 5 characters)")]) 
    @slash_commands.has_permissions(manage_guild=True)
    async def prefix(self, ctx, new_prefix: str):
        embed_error_too_long = discord.Embed(
            title=":octagonal_sign:Whoops!",
            description="Your prefix can't be more than `5` Characters long!",
            colour=utils.embed_color
        )

        if len(new_prefix) >= 5:
            await ctx.reply(embed=embed_error_too_long)

        else:
            async with aiosqlite.connect("database.db") as db:
                await db.execute("UPDATE guilds SET Prefix = ? WHERE GuildID = ?", (new_prefix, ctx.guild.id))
                await db.commit()
                await ctx.reply(f"Set prefix to `{new_prefix}`!")

    @settings.sub_command(description="Change your Server's Language (For the SCP Command)") 
    @slash_commands.has_permissions(manage_guild=True)
    async def language(self, ctx):
        msg = await ctx.reply("Choose a Language Below", 
        components=[
            SelectMenu(
                custom_id="set_language",
                placeholder="Choose a Language",
                max_values=1,
                options=[
                    SelectOption("English", "e"),
                    SelectOption("Spanish", "s"),
                    SelectOption("Russian", "r"),
                    SelectOption("Chinese", "c"),
                    # SelectOption("Korean", "k"),
                    SelectOption("Japanese", "j"),
                    SelectOption("French", "f"),
                    SelectOption("German", "g")
                ]
            )
        ]
    )
        def check(inter):
            return inter.author == ctx.author

        try:
            menu_inter = await msg.wait_for_dropdown(check, timeout=60)

        except asyncio.TimeoutError:
            await msg.delete()
        
        labels = [option.label for option in menu_inter.select_menu.selected_options]

        async with aiosqlite.connect("database.db") as db:
            await db.execute("UPDATE guilds SET Language = ? WHERE GuildID = ?", (labels[0], ctx.guild.id))
            await db.commit()
            await menu_inter.create_response(
                f"Set Language to `{labels[0]}`",
                components=[],
                type=7
        )

    @settings.error
    async def change_prefix_error(self, ctx, error):
        embed_error = discord.Embed(
            title=":octagonal_sign:Whoops!",
            description="Looks like you don't have permission! Make sure you have the `manage_guild` permission!",
            colour=utils.embed_color
        )
        await ctx.reply(embed=embed_error)

    @language.error
    async def language_error(self, ctx, error):
        embed_error = discord.Embed(
            title=":octagonal_sign:Whoops!",
            description="An unknown error occured. Try running the command again.",
            colour=utils.embed_color
        )
        await ctx.reply(embed=embed_error)

    @prefix.error
    async def set_error(self, ctx, error):
        embed_error = discord.Embed(
            title=":octagonal_sign:Whoops!",
            description="Looks like you don't have permission! Make sure you have the `manage_guild` permission!",
            colour=utils.embed_color
        )
        await ctx.reply(embed=embed_error)