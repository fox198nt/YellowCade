import discord
import os
import discord.ext
from discord.ext import commands

client = discord.Client()

client = commands.Bot(command_prefix = 'y?')

@client.event
async def on_ready():
    print("online")

@client.command(name='ping', description='see the bot latency')
async def ping(ctx: commands.Context):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")

@client.command(name='deeznuts', description="deez nuts.")
async def deeznuts(ctx):
    await ctx.send('deez nuts in yo jaw')

@client.command(name='say', description="Sends what you want the bot to say.")
async def say(ctx, *, content):
    await ctx.send(content)

import keep_alive
keep_alive.keep_alive()
client.run(os.getenv("TOKEN"))