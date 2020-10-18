import discord
from discord.ext import commands
import random
from datetime import datetime

import shufer

BOT_TOKEN = ''
bot = commands.Bot(command_prefix='?', description='this bot is very swag')

@bot.event
async def on_ready():
    print(f'{bot.user.name} is ready!')

@bot.command()
async def someone(ctx):
    await ctx.send(random.choice(ctx.channel.members).mention)

@bot.command()
async def shufersal(ctx, *args):
    product_id = int(args[0])
    speed = 1.0
    reverse = False
    time = False

    try:
        arg_ptr = 0
        while arg_ptr < len(args)-1:
            arg_ptr += 1
            arg = args[arg_ptr]

            if arg == '-s':
                arg_ptr += 1
                arg = float(args[arg_ptr])
                reverse = arg < 0
                speed = abs(arg)
            elif arg == '-r':
                reverse = True
            elif arg == '-t':
                time = True
            else:
                await ctx.send("Wrong Arguments (remind me to write a usuage message)!")
    except Exception as e:
        await ctx.send("Wrong Arguments (remind me to write a usuage message)!")

    if time:    
        startTime = datetime.now()

    gif = shufer.get_gif(product_id)

    if gif:
        await ctx.send(f"{(datetime.now() - startTime).total_seconds()}'s" if time else None, file=discord.File(shufer.get_gif(product_id, fps=speed*10, reverse=reverse), f"{product_id}.gif"))
    else:
        await ctx.send("Error has occured!")

bot.run(BOT_TOKEN)