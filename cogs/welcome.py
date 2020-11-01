from discord.ext import commands

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(772498152825552966)
        await channel.send(f"<@{str(member.id)}> has joined the server. Welcome, <@{str(member.id)}>.")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(772498152825552966)
        await channel.send(f"<@{str(member.id)}> has left the server. Farewell, <@{str(member.id)}>.")

def setup(bot):
    bot.add_cog(Welcome(bot))