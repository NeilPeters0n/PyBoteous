import discord
from discord.ext import commands
from stuff import *

class Test (commands.Cog):
    def __init__ (self, bot):
        self.bot= bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} is online")
    
    @commands.command(name= "S3CR3T")
    async def S3CR3T(self, ctx):
        await ctx.send(f"{ctx.author.mention} {secretMessage}")
        
async def setup(bot):
    await bot.add_cog(Test(bot))
    