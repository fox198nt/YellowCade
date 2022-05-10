import discord
import os
import discord.ext
import random
import praw
from discord.ext import commands

client = discord.Client()

client = commands.Bot(command_prefix = 'y?')

reddit = praw.Reddit(client_id = "rOn9qtyJnviLZW73lDUVYQ",
                    client_secret = "zcl6gbiYCpMaNUJoIe3s1A-f_bA_5Q",
                    password = "dpccyc1663",
                    username = "Fox198YT",
                    user_agent = "python")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='if anyone says y?help!'))
    print("online")

@client.command(description='see the bot latency')
async def ping(ctx: commands.Context):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")

@client.command()
async def cats(ctx):
    subreddit = reddit.subreddit("memes")
    subs = []
    top = subreddit.top(limit = 5)
    for submission in top: print(submission.title)
    
@client.command(description="deez nuts.")
async def deeznuts(ctx):
    await ctx.send('deez nuts in yo jaw')

@client.command()
async def emoji(ctx):
    emoji = ["😃", "😁", "😅", "🤣", "😭", "😉", "😗", "😘", "😍", "🥳", "🙃", "😜", "😇", "😏", "😌", "😐", "🤔", "🤫", "🥱", "🐧", "😱", "🙄", "😤", "🥺", "🙁", "🤐", "😨" ]
    await ctx.send(random.choice(emoji))

@client.command(description="Sends what you want the bot to say.")
async def say(ctx, *, content):
    await ctx.send(content)

@client.command(description="The Bot Server")
async def server(ctx):
    embed=discord.Embed(title="Bot Server", url="https://discord.gg/MjXNdEu7JC", description="Click the text above to join the server!", color=ffff80)
    embed.set_footer(text="Yellowcade by fox198nt#5762")
    await ctx.send(embed=embed)

@client.command(description="Kicks a member")
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    if reason==None:
      reason="No reason provided."
    await ctx.guild.kick(member)
    await ctx.send(f'Kicked user {member.mention}. Reason: {reason}')

#couldn't add mute
    
import keep_alive
keep_alive.keep_alive()
client.run(os.getenv("TOKEN"))