import discord
import random
import asyncio
from discord.ext import commands, ipc
import time
from dotenv import load_dotenv
import os
import sqlite3
from utils import get_prefix
import builtins
db = sqlite3.connect("database.db")
db.execute("""
CREATE TABLE IF NOT EXISTS guilds (
    GuildID integer PRIMARY KEY,
    Prefix text DEFAULT "'"
);""")
db.commit()
builtins.db = db


class MyBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ipc = ipc.Server(self, secret_key="scpinfoepic23")  # create our IPC Server

    async def on_ready(self):
        """Called upon the READY event"""
        print("Bot is ready.")

    async def on_ipc_ready(self):
        """Called upon the IPC Server being ready"""
        print("Ipc is ready.")

    async def on_ipc_error(self, endpoint, error):
        """Called upon an error being raised within an IPC route"""
        print(endpoint, "raised", error)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')



intents = discord.Intents.default()
intents.messages = True
bot = MyBot(command_prefix="'", intents=intents, case_insensitive=True)
builtins.bot = bot
import misc
bot.launch_time = time.time()

embed_color = discord.Colour(0x992d22)

access_denied = discord.Embed(
    title=':octagonal_sign:Uh Oh!', description=f"Looks like you don\'t have permission!", colour=discord.Colour(0x992d22)
)
access_denied.set_footer(
    text=f'Access Denied | Administrator Permission Required'
)

@bot.event
async def on_message(message):
    ctx = await bot.get_context(message)
    # print("got context")
    if isinstance(ctx.channel, discord.channel.DMChannel):
        return
    else:
        prefix = get_prefix(ctx.guild.id)
    # print("got prefix")
    # print(prefix)
    # print(message.content[0:len(prefix)])
    # print(message.content)
    if message.content[0:len(prefix)] == prefix:
        message.content = f"'{message.content[len(prefix):len(message.content)]}"
        # print("checked prefix")
        await bot.process_commands(message)
        # print("Finished")
    else:
        await bot.process_commands(message)


async def ch_pr():
    await bot.wait_until_ready()

    while not bot.is_closed():
        statuses = ["SCP Info | 'help", f"on {len(bot.guilds)} servers! | 'help",
                    "with SCP-999", "'help | scpinfo.xyz", "on scpinfo.xyz", "with SCP-682", "SCP: Secret Laboratory"]

        status = random.choice(statuses)

        await bot.change_presence(activity=discord.Game(name=status))
        await asyncio.sleep(60)

bot.loop.create_task(ch_pr())


# @bot.event
# async def on_guild_join(guild):
#     embed_added = discord.Embed(
#         title="Thanks for adding me to your Server!",
#         description="Hello! Thanks so much for adding me! I will now attempt to give a brief rundown of what I can do. Just to get this out of the way, my prefix is `'`.\n\n Using high powered python packages, I am able to search the web for any SCP you specify. This is my main command, you can try it by running `'scp (number)`. I also have various other commands such as 05 council member info, fun containment commands to fool your friends, and much more!.\n\n For info on any commands I have, run `'help` in your server! You may also join the [Support Server](https://discord.gg/DaWMTsXUYZ) for any questions, concerns, or ideas!\n\n [Invite](https://discord.com/oauth2/authorize?client_id=818294562677588009&permissions=2553671104&scope=bot) | [Support](https://discord.com/invite/hTPqf53abp) | [Website](https://www.scpinfo.xyz/)",
#         colour=discord.Colour(3066993)
#     )
#     embed_added.set_footer(
#         text=f"Thanks for adding me {guild.owner}! | Hope you enjoy my company :D"
#     )
#
#     await guild.owner.send(embed=embed_added)





@bot.ipc.route()
async def get_server_count(data):
    return len(bot.guilds)  # return the member count to the client

import scp
import admincommands
import beta
import languages
import settings
bot.load_extension("help")
bot.add_cog(scp.Foundation())
bot.add_cog(beta.Beta())
bot.add_cog(settings.Settings())
bot.add_cog(languages.Languages())
bot.add_cog(misc.Misc())
bot.add_cog(admincommands.Administrator())

if __name__ == "__main__":
    bot.ipc.start()  # start the IPC Server
    bot.run(TOKEN)
