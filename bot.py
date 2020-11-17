import discord
from discord.ext import commands
import random
from datetime import datetime

import shufer
import puns

BOT_TOKEN = ''
bot = commands.Bot(command_prefix='?', description='this bot is very swag')

@bot.event
async def on_ready():
    print(f'{bot.user.name} is ready!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.endswith('מה'):
        await message.channel.send('פליץ')

    elif message.content.endswith(' כן') or message.content.endswith(' קן'):
        await message.channel.send('גרו')

    elif message.content.endswith('לא'):
     await message.channel.send('זית')

    elif message.content.endswith('מי'):
     await message.channel.send('קרונזיה')

    elif message.content.endswith('ma'):
        await message.channel.send("flitz")

    elif message.content.endswith('lo'):
        await message.channel.send("zit")

    if "ממני" in message.content:
        await message.channel.send('מי זה מני?')
    

    await bot.process_commands(message)


@bot.command()
async def join(ctx):
    voice = ctx.author.voice

    if voice:
        await voice.channel.connect()
    else:
        await ctx.send("You're not connected to any voice chat!")

@bot.command()
async def leave(ctx):
    voice = ctx.voice_client

    if voice:
        await voice.disconnect()
    else:
        await ctx.send("I'm not connected to any voice chat!")


@bot.command()
async def someone(ctx):
    await ctx.send(random.choice(ctx.channel.members).mention)

@bot.command()
async def shufersal(ctx, *args):
    speed = 1.0
    reverse = False
    time = False
    mode = ''

    try:
        arg_ptr = 0
        product_id = int(args[0])
        while arg_ptr < len(args)-1:
            arg_ptr += 1
            arg = args[arg_ptr]

            if arg == '-s':
                arg_ptr += 1
                arg = float(args[arg_ptr])
                reverse = arg < 0
                speed = abs(arg)
            elif arg == '-m':
                arg_ptr += 1
                mode = args[arg_ptr]
            elif arg == '-r':
                reverse = True
            elif arg == '-t':
                time = True
            else:
                await ctx.send("Wrong Arguments! Usage: ?shufersal ID [-s SPEED] [-r] [-t] [-m MODE]")
                return
    except Exception as e:
        print(e)
        await ctx.send("Wrong Arguments! Usage: ?shufersal ID [-s SPEED] [-r] [-t] [-m MODE]")
        return

    if time:    
        startTime = datetime.now()

    gif = shufer.get_gif(product_id, fps=speed*10, reverse=reverse, mode=mode)

    if gif:
        await ctx.send(f"{(datetime.now() - startTime).total_seconds()}'s" if time else None, file=discord.File(gif,  f"{product_id}.gif"))
    else:
        await ctx.send("Error has occured!")

@bot.command()
async def merge(ctx, *args):
    word = ""
    count = 1
    verbose= False

    try:
        arg_ptr = 0
        word = args[arg_ptr]
        while arg_ptr < len(args)-1:
            arg_ptr += 1
            arg = args[arg_ptr]

            if arg == '-n':
                arg_ptr += 1
                count = int(args[arg_ptr])
            elif arg == '-v':
                verbose = True
            else:
                await ctx.send("Wrong Arguments! (aaaa i dont want to write a help message lol)")
                return
    except Exception as e:
        await ctx.send("Wrong Arguments! (aaaa i dont want to write a help message lol)")
        return
    
    print(word, verbose, count)

    merged_words = puns.get_portmanteaus(word)
    
    for n in range(count):
        merge = random.choice(merged_words)

        original_words = merge['source'].split(',')
        new_words = merge['combined'].split(',')

        await ctx.send(f"{f'{original_words[0]} + {original_words[1]} = ' if verbose else ''}{random.choice(new_words)}")


bot.run(BOT_TOKEN)