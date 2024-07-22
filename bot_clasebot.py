import discord
from discord.ext import commands
from bot_logic import *
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Se ha logueado {bot.user}')

@bot.command()
async def hola(ctx):
    await ctx.send(f'Hola, soy {bot.user}! bienvenido denuevo')

@bot.command()
async def chau(ctx):
    await ctx.send(f'Nos vemos pronto!')

@bot.command()
async def password(ctx, count_heh = 5):
    await ctx.send(gen_pass (10))

@bot.group()
async def cool(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')

@bot.command()
async def cool1(ctx):
    await ctx.send('Yes, El_Admin#0714 is cool.')

@bot.command()
async def meme(ctx):
    with open('images/mem1.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

import os
print(os.listdir('images'))

with open(f'images/mem1.jpg', 'rb') as f:
            picture = discord.File(f)

def meme_ch():
    memes = [
        "mem1.jpg",
        "mem2.jpg",
        "mem3.jpg"
        ]
    return random.choice(meme_ch)

def get_dog_image():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('dog')
async def dog(ctx):
    image_url = get_dog_image()
    await ctx.send(image_url)

@bot.command()
async def basura(ctx):
    await ctx.send(f'Introduce tu tipo de basura')

@bot.command()
async def plastico(ctx):
    await ctx.send(f'Este va en el bote amarillo')

@bot.command()
async def papel(ctx):
    await ctx.send(f'Este va en el bote azul')

@bot.command()
async def vidrio(ctx):
    await ctx.send(f'Este va en el bote verde')

@bot.command()
async def tip(ctx):
    await ctx.send(f'Recicla cada material en el lugar que corresponde.')

bot.run("...")