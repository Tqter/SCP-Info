import discord
import datetime
from discord.ext import commands
from builtins import bot

embed_color = discord.Colour(0x992d22)
bot.remove_command('help')


access_denied = discord.Embed(
    title=':octagonal_sign:Uh Oh!', description=f"Looks like you don\'t have permission!", colour=discord.Colour(0x992d22)
)
access_denied.set_footer(
    text=f'Access Denied • Administrator Permission Required'
)


class CommandsHelp(commands.Cog):
    def __init__(self):
        self.bot = bot

    @commands.group(invoke_without_command=True, pass_context=True, aliases=['h'])
    async def help(self, ctx):
        author = ctx.message.author
        embed_help = discord.Embed(
            title="Help",
            description=f"Hi! I am a Discord bot focused on giving you info on any SCP of your choice!\n\n **Prefix:** `'`",
            colour=discord.Colour(0x992d22),
            timestamp=datetime.datetime.now(datetime.timezone.utc)
        )

        embed_help.add_field(
            name="SCP",
            value=":question: `'help scp`\n\n [Invite](https://discord.com/api/oauth2/authorize?client_id=818294562677588009&permissions=2553671104&scope=bot) | [Support](https://discord.gg/DaWMTsXUYZ)"
        )

        embed_help.add_field(
            name="Misc",
            value=":question: `'help misc`"
        )



        embed_help.set_footer(
            text=f"Command invoked by {ctx.message.author.name}", icon_url=author.avatar_url
        )
        await ctx.send(embed=embed_help)


    @help.command(aliases=['scps'])
    async def scp(self, ctx):
        author = ctx.message.author
        embed_helpSCP = discord.Embed(
            title="Help | SCP",
            description="All the commands related to the SCP Foundation!\n\n <:scp:830789987397009468> `'scp (number)` **•** Displays info on the specified SCP\n\n <:05:809787013204541440> `'O5 (number)` **•** Displays information on the specified council member\n\n <:mtf:809783726770094121> `'contain (user)` **•** Contains specified user. But be careful, it's risky!\n\n [Invite](https://discord.com/api/oauth2/authorize?client_id=818294562677588009&permissions=2553671104&scope=bot) | [Support](https://discord.gg/DaWMTsXUYZ)",
            colour=embed_color,
            timestamp=datetime.datetime.now(datetime.timezone.utc)
        )


        embed_helpSCP.set_footer(
           text=f"Command invoked by {ctx.message.author.name}", icon_url=author.avatar_url
        )
        await ctx.send(embed=embed_helpSCP)



    @help.command(aliases=['miscellaneous'])
    async def misc(self, ctx):
        author = ctx.message.author
        embed_helpMisc = discord.Embed(
            title="Help | Miscellaneous",
            description="Various random commands that were made as a side dish!\n\n <:code:830641334145777685> `'code` • Brings you to this bot's GitHub Repository\n\n :wrench: `'support` **•** In case you want help or news on Updates and Fixes\n\n <a:countup:830789232431202336> `'servercount` **•** In case you wanna know how many servers this bot is in!\n\n <:invite:830789505212612629> `'invite` **•** In case you wanna invite this bot to your server! HINT: You should!\n\n [Invite](https://discord.com/api/oauth2/authorize?client_id=818294562677588009&permissions=2553671104&scope=bot) | [Support](https://discord.gg/DaWMTsXUYZ)",
            colour=embed_color,
            timestamp=datetime.datetime.now(datetime.timezone.utc)
        )

        embed_helpMisc.set_footer(
            text=f"Command invoked by {ctx.message.author.name}", icon_url=author.avatar_url
        )
        await ctx.send(embed=embed_helpMisc)