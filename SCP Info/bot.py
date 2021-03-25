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
        title="Help", description=f"Hi! I am a Discord bot focused on giving you info on different SCPs!\n\n **Prefix:** `'`\n\n :question: `'scp help` | Shows this Message\n\n :question: `'scp (number)` | Displays info on the specified SCP", colour=discord.Colour.orange())

    embed_help.set_footer(
        text=f"SCP Info | Created by Tqter#9300"
    )

    await ctx.send(embed=embed_help)


@bot.command()
async def scp(ctx, scp_number):
    author = ctx.message.author
    x = GetSCP.GetSCP(int(scp_number))
    embed_scp = discord.Embed(
        title=f'SCP-{scp_number}', description=x, colour=discord.Colour.blurple()
    )

    await ctx.send(embed=embed_scp)


bot.run('ODE4Mjk0NTYyNjc3NTg4MDA5.YEV-Mg.9sU0HkbuQWKhGUxfS2N2eEIcCCA')
