from dotenv import load_dotenv
from discord.ext import commands
import os
from danbooru_api import danbooru_pic


# This loads environtmental values (download python-dotenv from pypi)
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

# Initalize bot instance
bot = commands.Bot(command_prefix='!!')

# Output to console as bot is turned on
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord')

@bot.command(name='grab_pic', help='When the \'!!grab_pic\' is invoked, a random pic from danbooru.donmai.us will be posted. ')
async def grab_pic(ctx):
    response = danbooru_pic()
    for line in response:
        await ctx.send(line)

bot.run(token)