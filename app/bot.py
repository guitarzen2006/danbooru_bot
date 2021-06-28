from discord.ext.commands import errors
from discord.ext.commands.core import Command
from discord.ext.commands.errors import CommandNotFound
from dotenv import load_dotenv
from discord.ext import commands
import os
from danbooru_api import danbooru_pic
import log_bot


# This loads environtmental values (download python-dotenv from pypi)
load_dotenv()
token = os.getenv('DISCORD_TOKEN')
spacer = "=+"*40

# Initalize bot instance
bot = commands.Bot(command_prefix='!!')

def main():
    '''danbooru_bot is a simple discord bot that calls an API to safebooru.donmai.us to pull up to 5 anime pics of kawaii girls '''
    @bot.event
    async def on_ready():
        print(f'{bot.user.name} has connected to Discord')
        log_bot.log_start_app(bot.user.name)
    
    @bot.event
    async def on_disconnect():
        print(f'{bot.user.name} has diconnected from Discord')
        log_bot.log_stopped_app(bot.user.name)

    @bot.command(name='grab_pic', help='When the \'!!grab_pic [number of pics]\' is invoked, a random pic(s) from safebooru.donmai.us will be posted. ')
    async def grab_pic(ctx, limit_amount=1):
        # Identify user
        user = ctx.author.name
        log_bot.log_app_request(limit_amount, user)
        if limit_amount > 5:
            await ctx.send("Please limit your request to 5 pics.")
        elif limit_amount <= 5:
            raw_grab = danbooru_pic(limit_amount)
            if isinstance(raw_grab, list):
                for posts in range(len(raw_grab)):
                    #raw_grab is a list - slice at [posts] and then at ['file_url'] for picture URL, if it does not exist send 'preview_file_url'
                    try:
                        source = raw_grab[posts]['id']
                        message = (f'{spacer} \n {user}, you can find this pic at this url: \'<https://safebooru.donmai.us/posts/{source}>\' \n')
                        pic = raw_grab[posts]['file_url']
                    except:
                        # Error handling if raw_grab is a list but missing the 'file_url' key
                        message = (f'Sorry {user}-senpai, there was an issue with the request. 悪い、{user}-先輩。残念リクエストが失敗しました')
                        pic = None
                        log_bot.log_app_failure(message)
                    await ctx.send(message)
                    await ctx.send(pic)
            else:
                # Error handling if raw_grab is not a list.
                message = (f'Sorry {user} there was an issue with safebooru.conmai.us, or the api. Please contact the administrator.')
                log_bot.log_app_failure(message)
                await ctx.send(message)

    @bot.event
    # Discord bot event handling
    async def on_command_error(ctx, error):
        user = ctx.author.name
        if isinstance(error, errors.CommandNotFound):
            log_bot.log_app_error(error, user)
            await ctx.send(f'The command {user} typed is not found. Type \'!!help\' for more information. :thinking_face:')

    bot.run(token)

if __name__ == "__main__":
    main()