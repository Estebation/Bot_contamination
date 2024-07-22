import discord
from discord.ext import commands
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