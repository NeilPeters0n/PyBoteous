import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import asyncio

bot= commands.Bot(command_prefix=".", intents= discord.Intents.all())

@bot.event
async def on_ready():
    print("PyBoteous is online!")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Stuff"))
    
    try:
        synced_commands= await bot.tree.sync()
    except Exception as e:
        print("An error occured syncing application commands: ", e)

load_dotenv()
Token= os.getenv("TOKEN")
async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with bot:
        await load()
        await bot.start(Token)

asyncio.run(main())

