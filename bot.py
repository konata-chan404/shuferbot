import discord
from discord.ext import commands

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
async def shufersal(ctx, product_id: int):
    await ctx.send(file=discord.File(shufer.get_gif(product_id), f"{product_id}.gif"))

bot.run(BOT_TOKEN)