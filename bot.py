from dotenv import load_dotenv
from discord.ext import commands
import os
from danbooru_api import danbooru_pic


# This loads environtmental values (download python-dotenv from pypi)
load_dotenv()
token = os.getenv('DISCORD_TOKEN')
spacer = "=+"*40

# Initalize bot instance
bot = commands.Bot(command_prefix='!!')

# Output to console as bot is turned on
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord')

@bot.command(name='grab_pic', help='When the \'!!grab_pic [number of pics]\' is invoked, a random pic(s) from safebooru.donmai.us will be posted. ')
async def grab_pic(ctx, limit_amount=1):
    raw_grab = danbooru_pic(limit_amount)
    for posts in range(len(raw_grab)):
        #raw_grab is a list - slice at [posts] and then at ['file_url'] for picture URL, if it does not exist send 'preview_file_url'
        try:
            source = raw_grab[posts]['id']
            message = (f'{spacer} \n You can find this pic at this url: \'<https://safebooru.donmai.us/posts/{source}>\' \n')
            pic = raw_grab[posts]['file_url']
        except:
            message = 'Sorry Senpai, there was an issue with the request. 悪い、先輩。残念リクエストが失敗しました'
            pic = None
        await ctx.send(message)
        await ctx.send(pic)

bot.run(token)