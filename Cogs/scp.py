import get_scp
import languages
import discord
import datetime
import random
import council_members
from discord.ext import commands
from builtins import bot

embed_color = discord.Colour(0x992d22)


class Foundation(commands.Cog):
    def __init__(self):
        self.bot = bot

    @commands.command(help="Gives info on any SCP you enter.")
    async def scp(self, ctx, scp_number):

        if isinstance(ctx.channel, discord.DMChannel):
            language = "english"
        else:
            language = languages.get_language(ctx.guild.id)

        scp_int = int(scp_number)

        if 100 > scp_int >= 10:
            scp_number = f"0{scp_int}"
        elif 1 < scp_int < 10:
            scp_number = f"00{scp_int}"
        elif scp_int == 1:
            print("ERROR - 1")
            return

        x = get_scp.get_scp(scp_number, language)

        text_lists = []
        scp_len = len(x)
        scp_count = 0
        while scp_count < scp_len:
            scp_string = x[scp_count:scp_count + 2024]
            text_lists.append(scp_string)
            scp_count += 2024

        embed_list = []
        for x in range(0, len(text_lists)):
            embed_scp = None
            if x != len(text_lists) - 1:
                embed_scp = discord.Embed(
                    title=f'SCP-{scp_number}', url=fr"{languages.langauge_to_website[language]}scp-{scp_number}",
                    description=text_lists[x] + '... **Read More**',
                    colour=discord.Colour(0x992d22))
            else:
                embed_scp = discord.Embed(
                    title=f'SCP-{scp_number}', description=text_lists[x],
                    colour=discord.Colour(0x992d22))

            embed_list.append(embed_scp)

        place = 0

        message = await ctx.send(embed=embed_list[0])

        await message.add_reaction("◀")
        await message.add_reaction("▶")
        await message.add_reaction("🔄")

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

            elif reaction.emoji == "🔄":
                if place > 0:
                    place = 0
                await message.edit(embed=embed_list[place])
                await message.remove_reaction(emoji="🔄", member=ctx.author)

    @scp.error
    async def scp_error(self, ctx, error):
        embed_scp_error = discord.Embed(
            title=':octagonal_sign:Oops!',
            description='You might have missed an argument or put an invalid number in! Try `\'scp {001 - 5999}`',
            colour=discord.Colour(0x992d22))
        await ctx.send(embed=embed_scp_error)

    @commands.command(help="`Contain` your friends and play some pranks on them!")
    async def contain(self, ctx, user: discord.Member):
        author = ctx.message.author
        id_contain = str(user.id)
        contain_list = [
            f'{author.mention} contained <@{id_contain}>, termination cause **Micro-HID**.',
            f'{author.mention} was ripped to shreds by <@{id_contain}> in an attempt to contain them.',
            f'{author.mention} contained <@{id_contain}>, termination cause **P90**.',
            f'{author.mention} contained <@{id_contain}>, termination cause **SCP-018.**',
            f'{author.mention} was ripped to shreds by <@{id_contain}> in an attempt to contain them.',
            f'{author.mention} died to puncture wounds while trying to contain <@{id_contain}>.',
            f'{author.mention} contained <@{id_contain}>, termination cause **Micro-HID**.',
            f'{author.mention} died to automatic security while running from <@{id_contain}>.',
            f'{author.mention} contained <@{id_contain}>, termination cause **Frag Grenade**.',
            f'{author.mention} died to puncture wounds while trying to contain <@{id_contain}>.',
            f'{author.mention} got their neck snapped while trying to contain <@{id_contain}>.',
            f'{author.mention} contained <@{id_contain}>, termination cause **SCP-018.**',
            f'{author.mention} died to automatic security while running from <@{id_contain}>.',
            f'{author.mention} was sent to another dimension in an attempt to contain <@{id_contain}>.',
            f'{author.mention} died to automatic security while running from <@{id_contain}>.',
            f'{author.mention} contained <@{id_contain}>, termination cause **Micro-HID**.',
            f'{author.mention} was ripped to shreds by <@{id_contain}> in an attempt to contain them.',
            f'{author.mention} contained <@{id_contain}>, termination cause **P90**.',
            f'{author.mention} contained <@{id_contain}>, termination cause **SCP-018.**',
            f'{author.mention} was ripped to shreds by <@{id_contain}> in an attempt to contain them.',
            f'{author.mention} died to puncture wounds while trying to contain <@{id_contain}>.',
            f'{author.mention} contained <@{id_contain}>, termination cause **Micro-HID**.',
            f'{author.mention} died to automatic security while running from <@{id_contain}>.',
            f'{author.mention} contained <@{id_contain}>, termination cause **Frag Grenade**.',
            f'{author.mention} died to puncture wounds while trying to contain <@{id_contain}>.',
            f'{author.mention} got their neck snapped while trying to contain <@{id_contain}>.',
            f'{author.mention} contained <@{id_contain}>, termination cause **SCP-018.**',
            f'{author.mention} died to automatic security while running from <@{id_contain}>.',
            f'{author.mention} was sent to another dimension in an attempt to contain <@{id_contain}>.',
            f'{author.mention} died to automatic security while running from <@{id_contain}>.',
            f'{author.mention} contained <@{id_contain}>, termination cause **Micro-HID**.',
            f'{author.mention} was ripped to shreds by <@{id_contain}> in an attempt to contain them.',
            f'{author.mention} contained <@{id_contain}>, termination cause **P90**.',
            f'{author.mention} contained <@{id_contain}>, termination cause **SCP-018.**',
            f'{author.mention} was ripped to shreds by <@{id_contain}> in an attempt to contain them.',
            f'{author.mention} died to puncture wounds while trying to contain <@{id_contain}>.',
            f'{author.mention} contained <@{id_contain}>, termination cause **Micro-HID**.',
            f'{author.mention} died to automatic security while running from <@{id_contain}>.',
            f'{author.mention} contained <@{id_contain}>, termination cause **Frag Grenade**.',
            f'{author.mention} died to puncture wounds while trying to contain <@{id_contain}>.',
            f'{author.mention} got their neck snapped while trying to contain <@{id_contain}>.',
            f'{author.mention} contained <@{id_contain}>, termination cause **SCP-018.**',
            f'{author.mention} died to automatic security while running from <@{id_contain}>.',
            f'{author.mention} was sent to another dimension in an attempt to contain <@{id_contain}>.',
            f'{author.mention} died to automatic security while running from <@{id_contain}>.',
        ]
        await ctx.send(random.choice(contain_list))

    @contain.error
    async def contain_error(self, ctx, error):
        embed_contain_error = discord.Embed(title=':octagonal_sign:Oops!',
                                            description="""
                                            Make sure you enter a valid user! Check that you spell their name correctly! (Case Sensitive)
                                            """,
                                            colour=embed_color
                                            )
        await ctx.send(embed=embed_contain_error)

    @commands.command(name="O5", pass_context=True, aliases=['05'],
                      help="View info on the Specified O5 Council Member.")
    async def council(self, ctx, council_member: int):
        embed_council = discord.Embed(
            title=f'O5-{council_member}: "{(council_members.council_nickname[council_member])}"',
            description=(
                            council_members.council_members[
                                council_member]) + "\n\n **View other contradictory reports at**: [The SCP Wiki](http://www.scpwiki.com/o5-command-dossier)",
            colour=embed_color
        )
        await ctx.send(embed=embed_council)

    @council.error
    async def council_error(self, ctx, error):
        embed_council_error = discord.Embed(
            title=':octagonal_sign:Oops!',
            description='Looks like that isn\'t a valid O5 Council member! Try `\'O5 {1 - 13}`',
            colour=discord.Colour(0x992d22))
        await ctx.send(embed=embed_council_error)

    @commands.command(help="View an illustrated and explained chart of SCP Classification.",
                      aliases=["class", "classes"])
    async def classification(self, ctx):
        author = ctx.message.author
        embed_classes = discord.Embed(
            title="SCP Classification",
            colour=embed_color,
            timestamp=datetime.datetime.now(datetime.timezone.utc)
        )

        embed_classes.set_footer(
            text=f"Command invoked by {ctx.message.author.name}", icon_url=author.avatar_url
        )

        embed_classes.set_image(url="https://i.redd.it/qpx6kphvs7o41.png")

        await ctx.send(embed=embed_classes)
