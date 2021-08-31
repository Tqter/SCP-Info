import datetime
import time
import aiosqlite
from builtins import bot, slash
import Utils.utils as utils
import Cogs.languages as languages
from Cogs import council
from Cogs import get_scp
import discord
import datetime
import random
from discord.ext import commands
from dislash import Option, Button, ActionRow, ButtonStyle



class SCP_Slash(commands.Cog):
    place = 0
    def __init__(self):
        self.bot = bot

    @slash.command(name="scp", description="Get Info on ANY SCP of your Choice" , options=[Option("scp_number", "Enter the SCP Number (001 - 5999)")])
    async def scp(self, ctx, scp_number):
        if isinstance(ctx.channel, discord.DMChannel):
            language = "english"
        else:
            language = await languages.get_language(ctx.guild.id)

        scp_int = int(scp_number)

        if 100 > scp_int >= 10:
                scp_number = f"0{scp_int}"
        elif 1 < scp_int < 10:
                scp_number = f"00{scp_int}"
        elif scp_int == 1:
                return

        x = get_scp.get_scp(scp_number, language)

        text_lists = []
        scp_len = len(x)
        scp_count = 0
        
        while scp_count < scp_len:
            scp_string = x[scp_count:scp_count + 2031]
            text_lists.append(scp_string)
            scp_count += 2031

        embed_list = []


        for x in range(0, len(text_lists)):
            embed_scp = None
            if x != len(text_lists) - 1:
                embed_scp = discord.Embed(
                    title=f'SCP-{scp_number}', url=fr"{utils.langauge_to_website[language]}scp-{scp_number}",
                    description=text_lists[x] + '... **Read More**',
                    colour=discord.Colour(0x992d22))
            else:
                embed_scp = discord.Embed(
                    title=f'SCP-{scp_number}', url=fr"{utils.langauge_to_website[language]}scp-{scp_number}", description=text_lists[x],
                    colour=discord.Colour(0x992d22))

            embed_list.append(embed_scp)

        row = ActionRow(
        Button(
            style=ButtonStyle.green,
            label="Back",
            custom_id="back_page"
        ),
        Button(
            style=ButtonStyle.red,
            label="Reset",
            custom_id="restart"
        ),
        Button(
            style=ButtonStyle.green,
            label="Next",
            custom_id="next_page"
        )
    )


        message = await ctx.send(embed=embed_list[0], components=[row])

        on_click = message.create_click_listener(timeout=60)

        @on_click.not_from_user(ctx.author, cancel_others=True, reset_timeout=False)
        async def on_wrong_user(inter):

        # Reply with a hidden message
            await inter.reply("You're not the author", ephemeral=True)

        @on_click.matching_id("back_page")
        async def on_back_page(ctx):
            if SCP_Slash.place > 0:
                SCP_Slash.place -= 1
            await ctx.reply(embed=embed_list[SCP_Slash.place], type=7)

            
        @on_click.matching_id("restart")
        async def on_reset(ctx):
            SCP_Slash.place = 0
            await ctx.reply(embed=embed_list[SCP_Slash.place], type=7)
        
        @on_click.matching_id("next_page")
        async def on_next_page(ctx):
            if SCP_Slash.place < len(embed_list) - 1:
                SCP_Slash.place += 1
                await ctx.reply(embed=embed_list[SCP_Slash.place], type=7)

        @on_click.timeout
        async def on_timeout():
            await message.edit(components=[])


    @scp.error
    async def scp_error(self, ctx, error):
        print(error)
        embed_scp_error = discord.Embed(
            title=':octagonal_sign:Oops!',
            description='You might have missed an argument or put an invalid number in! Try `\'scp {001 - 5999}`',
            colour=discord.Colour(0x992d22))
        await ctx.send(embed=embed_scp_error)