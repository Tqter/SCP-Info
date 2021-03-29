import discord
from discord.ext import commands
import GetSCP


intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="\'", intents=intents)

bot.remove_command('help')


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="SCP Info | 'help"))
    print("We are up!")


@bot.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    embed_help = discord.Embed(
        title="Help", description=f"Hi! I am a Discord bot focused on giving you info on different SCPs!\n\n **Prefix:** `'`\n\n :question: `'scp help` | Shows this Message\n\n :question: `'scp (number)` | Displays info on the specified SCP\n\n :question: `'code` | Brings you to this bot's GitHub Repository", colour=discord.Colour.orange())

    embed_help.set_footer(
        text=f"SCP Info | Created by Tqter#1696"
    )

    await ctx.send(embed=embed_help)


@bot.command()
async def code(ctx):
    embed_code = discord.Embed(
        title="Code", description="Click here for the GitHub Repository:\n\n https://github.com/Tqter/SCP-Info"
    )
    await ctx.send(embed=embed_code)


@bot.command()
async def scp(ctx, scp_number):
    author = ctx.message.author
    x = GetSCP.GetSCP(int(scp_number))

    text_lists = []
    scp_len = len(x)
    scp_count = 0
    while scp_count < scp_len:
        scp_string = x[scp_count:scp_count+2024]
        text_lists.append(scp_string)
        scp_count += 2024

    embed_list = []
    for text_group in text_lists:
        embed_scp = discord.Embed(
            title=f'SCP-{scp_number}', description=text_group + '**... Read More**', colour=discord.Colour.blurple())

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


bot.run('token')
