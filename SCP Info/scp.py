import praw
import GetSCP
import discord
import datetime
import urllib
import random
import council_members
from discord.ext import commands
from builtins import bot

embed_color = discord.Colour(0x992d22)

reddit = praw.Reddit(client_id = "w_lVEqKZWECPnA",
                     client_secret = "dmuixS8UTfzVU_i0qWGZAn9Ts3XZ_g",
                     username = "CouchPotato_23",
                     password = "magicSquirt23",
                     user_agent = "scpimages")



class Foundation(commands.Cog):
    def __init__(self):
        self.bot = bot

    @commands.command(help="Gives info on any SCP you enter.")
    async def scp(self, ctx, scp_number):
        author = ctx.message.author
        embed_error = discord.Embed(
            title=':octagonal_sign:Oops!', description='That isn\'t a valid SCP Number! Try `\'scp {001 - 5999}`',
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
        for x in range(0, len(text_lists)):
            embed_scp = None
            if x != len(text_lists) - 1:
                embed_scp = discord.Embed(
                    title=f'SCP-{scp_number}', url=fr"http://www.scpwiki.com/scp-{scp_number}", description=text_lists[x] + '... **Read More**',
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


    @commands.group(name="O5", pass_context=True, aliases=['05'], help="View info on the Specified O5 Council Member.")
    async def council(self, ctx, council_member: int):
        embed_error = discord.Embed(
            title=':octagonal_sign:Oops!', description='That isn\'t a valid O5 Council Member! Try `\'O5 {1 - 13}`',
            colour=discord.Colour(0x992d22))
        try:
            embed_council = discord.Embed(
                title=f'O5-{council_member}: "{(council_members.council_nickname[council_member])}"',
                description=(council_members.council_members[council_member]) + "\n\n **View other contradictory reports at**: [The SCP Wiki](http://www.scpwiki.com/o5-command-dossier)",
                colour=embed_color
            )
            await ctx.send(embed=embed_council)
        except:
            await ctx.send(embed=embed_error)

    @commands.command(help="Grabs top images from [r/SCP](https://www.reddit.com/r/SCP/).", aliases=["image"])
    async def images(self, ctx):
        author = ctx.message.author

        subreddit = reddit.subreddit("SCP")
        all_subs = []
        top = subreddit.top(limit=50)

        for submission in top:
            all_subs.append(submission)

        random_sub = random.choice(all_subs)

        name = random_sub.title
        url = random_sub.url

        embed_reddit = discord.Embed(
            title=name,
            url=url,
            color=embed_color,
            timestamp=datetime.datetime.now(datetime.timezone.utc)
        )

        embed_reddit.set_image(
            url=url
        )

        embed_reddit.set_footer(
            text=f"Command invoked by {ctx.message.author.name}", icon_url=author.avatar_url
        )

        await ctx.send(embed=embed_reddit)




