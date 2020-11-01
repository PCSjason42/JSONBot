from discord.ext import commands
from discord.ext.commands import has_permissions
from discord.ext.commands.errors import MissingPermissions
import time

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(hidden=True)
    async def clear(self, ctx, amount):
        if not await has_permissions(manage_channels=True).predicate(ctx):
            raise MissingPermissions(["manage_channels"])
        await ctx.channel.purge(limit = int(amount) + 1)
        message = await ctx.send(f'**{amount}** message(s) have been deleted!')
        time.sleep(5)
        await message.delete()

def setup(bot):
    bot.add_cog(Misc(bot))