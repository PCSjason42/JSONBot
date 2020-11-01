import discord
from discord.ext import commands
from uuid import uuid4 as uuid
import json

class Json(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Generates a manifest.json file for Minecraft: Bedrock Edition resource packs, given the pack name, pack description and the pack version.", 
    brief="Generates a manifest.json file for resource packs.", 
    usage="This is an example name.:;This is an example description.:;1, 0, 0")
    async def manifestrp(self, ctx, *, args):
        try:
            args = str(args).split(":;")
            with open("./json/manifest/manifestrp.json", "r") as f:
                mani = json.load(f)
            mani["header"]["name"] = args[0]
            mani["header"]["description"] = args[1]
            mani["modules"][0]["description"] = args[1]
            mani["header"]["version"] = list(map(int, args[2].split(", ")))
            mani["modules"][0]["version"] = list(map(int, args[2].split(", ")))
            mani["header"]["uuid"] = str(uuid())
            mani["modules"][0]["uuid"] = str(uuid())
            with open("./json/manifest/manifestrp.json", "w") as f:
                json.dump(mani, f, indent=4)
            with open("./json/manifest/manifestrp.json", "rb") as fp:
                await ctx.channel.send("Here's your `manifest.json` file. Please put it on the **root** of your *resource pack folder*.\n(Root means the top folder, not inside any folders)", file=discord.File(fp, "manifest.json"))
        except (IndexError, TypeError):
            await ctx.send("Invalid argument!")

    @commands.command(help="Generates a manifest.json file for Minecraft: Bedrock Edition behavior packs, given the pack name, pack description and the pack version.", 
    brief="Generates a manifest.json file for behavior packs.", 
    usage="This is an example name.:;This is an example description.:;1, 0, 0")
    async def manifestbp(self, ctx, *, args):
        try:
            args = str(args).split(":;")
            with open("./json/manifest/manifestbp.json", "r") as f:
                mani = json.load(f)
            mani["header"]["name"] = args[0]
            mani["header"]["description"] = args[1]
            mani["modules"][0]["description"] = args[1]
            mani["header"]["version"] = list(map(int, args[2].split(", ")))
            mani["modules"][0]["version"] = list(map(int, args[2].split(", ")))
            mani["header"]["uuid"] = str(uuid())
            mani["modules"][0]["uuid"] = str(uuid())
            with open("./json/manifest/manifestbp.json", "w") as f:
                json.dump(mani, f, indent=4)
            with open("./json/manifest/manifestbp.json", "rb") as fp:
                await ctx.channel.send("Here's your `manifest.json` file. Please put it on the **root** of your *behavior pack folder*.\n(Root means the top folder, not inside any folders)", file=discord.File(fp, "manifest.json"))
        except (IndexError, TypeError):
            await ctx.send("Invalid argument!")

    @commands.command(help=)

def setup(bot):
    bot.add_cog(Json(bot))