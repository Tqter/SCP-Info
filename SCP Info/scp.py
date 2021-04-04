import urllib
import GetSCP
import discord
from discord.ext import commands
from builtins import bot


class CommandSCP(commands.Cog):
    def __init__(self):
        self.bot = bot

    @commands.command()
    async def scp(self, ctx, scp_number):
        author = ctx.message.author
        embed_error = discord.Embed(
            title=':octagonal_sign:Oops!', description='That isn\'t a valid SCP Number! Try `\'scp {001 - 6000}`',
            colour=discord.Colour(0x992d22))
        scp_int = int(scp_number)

        if 100 > scp_int >= 10:
            scp_number = f"0{scp_int}"
        elif 1 < scp_int < 10:
            scp_number = f"00{scp_int}"
        elif scp_int == 1:
            print("ERROR - 1")
            return

        try:
            x = GetSCP.GetSCP(scp_number)
        except urllib.error.HTTPError:
            await ctx.send(embed=embed_error)

        text_lists = []
        scp_len = len(x)
        scp_count = 0
        while scp_count < scp_len:
            scp_string = x[scp_count:scp_count + 2024]
            text_lists.append(scp_string)
            scp_count += 2024

        embed_list = []
        for text_group in text_lists:
            embed_scp = discord.Embed(
                title=f'SCP-{scp_number}', description=text_group + '... **Read More**',
                colour=discord.Colour(0x992d22))

            embed_list.append(embed_scp)

        place = 0

        message = await ctx.send(embed=embed_list[0])

        await message.add_reaction("◀")
        await message.add_reaction("▶")

        while True:
            reaction, member = await bot.wait_for('reaction_add')

            if member.id != ctx.author.id or reaction.message.id != message.id or member.bot:
                continue

            if reaction.emoji == "◀":
                if place > 0:
                    place -= 1
                await message.edit(embed=embed_list[place])
                await message.remove_reaction(emoji="◀", member=ctx.author)

            elif reaction.emoji == "▶":
                if place < len(embed_list) - 1:
                    place += 1
                await message.edit(embed=embed_list[place])
                await message.remove_reaction(emoji="▶", member=ctx.author)


