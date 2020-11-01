import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix="j!")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="JavaScript Object Notation is fun!"))
    print(f"We have logged in as {bot.user}. Bot is ready.")

for i in os.listdir('./cogs'):
    if i.endswith('.py'):
        bot.load_extension(f'cogs.{i[:-3]}')
        print(f"Loaded {i[:-3]}!")

@bot.command(brief="Returns the latency of the bot.", help="Returns the latency of the bot.")
async def ping(ctx):
    await ctx.send(f":ping_pong: Pong!\nLatency: **{round(bot.latency * 1000)}ms**")

@bot.command(hidden=True)
async def extload(ctx, cog):
    if str(ctx.author.id) == os.environ.get("OWNER"):
        bot.load_extension(f'cogs.{cog}')
        await ctx.send(f'Loaded extension `{cog}`!')
    else:
        await ctx.send("Sorry, but you don't have permission to do that.")

@bot.command(hidden=True)
async def extunload(ctx, cog):
    if str(ctx.author.id) == os.environ.get("OWNER"):
        bot.unload_extension(f'cogs.{cog}')
        await ctx.send(f'Unloaded extension `{cog}`!')
    else:
        await ctx.send("Sorry, but you don't have permission to do that.")

@bot.command(hidden=True)
async def extreload(ctx, cog):
    if str(ctx.author.id) == os.environ.get("OWNER"):
        bot.unload_extension(f'cogs.{cog}')
        bot.load_extension(f'cogs.{cog}')
        await ctx.send(f'Reloaded extension `{cog}`!')
    else:
        await ctx.send("Sorry, but you don't have permission to do that.")

@bot.command(hidden=True)
async def extlist(ctx):
    if str(ctx.author.id) == os.environ.get("OWNER"):
        exts = []
        for i in os.listdir('./cogs'):
            if i.endswith('.py'):
                exts.append(i[:-3])
        message = ''
        for j in exts:
            message += f'''`{j}`\n'''
        await ctx.send(message)
    else:
        await ctx.send("Sorry, but you don't have permission to do that.")

bot.run(os.environ.get("TOKEN"))