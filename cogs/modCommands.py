import discord
from discord.ext import commands
from discord import app_commands

class Mod (commands.Cog):
    def __init__ (self, bot):
        self.bot= bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} is online")
        
    @app_commands.command(name= "clear", description= "Delete a specified amount of messages from the channel.")
    @app_commands.checks.has_permissions(manage_messages= True)
    async def deleteMessages(self, interaction: discord.Interaction, amount: int):
        if amount < 1:
            await interaction.channel.send(f"{interaction.user.mention}, Please enter a value greater than one.")
            return
        await interaction.response.send_message(f"Clearing {amount} messages.", ephemeral=True)
        await interaction.channel.purge(limit= amount)
        await interaction.channel.reponse.send_message(f"{interaction.user.mention} has deleted {amount} messages.")
        
    @app_commands.command(name= "kick", description= "Kick specified user from server.")
    @app_commands.checks.has_permissions(kick_members= True)
    async def kick(self, interaction: discord.Interaction, member: discord.Member):
        await interaction.guild.kick (member)
        await interaction.response.send_message(f"You have kicked {member.mention}.", ephemeral=True)
        
    @app_commands.command(name= "ban", description= "Ban specified user from server.")
    @app_commands.checks.has_permissions(ban_members= True)
    async def ban(self, interaction: discord.Interaction, member: discord.Member):
        await interaction.guild.ban (member)
        await interaction.response.send_message(f"You have banned {member.mention}.", ephemeral=True)
    
    
        
async def setup(bot):
    await bot.add_cog(Mod(bot))