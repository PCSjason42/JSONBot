import discord
from discord.ext import commands
import json
import os

class Invite(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        global invites
        invites = {}
        for guild in self.bot.guilds:
            try:
                invites[guild.id] = await guild.invites()
            except discord.errors.Forbidden:
                continue

    def code2inv(self, list, code):
        for invite in list:
            if invite.code == code:
                return invite

    @commands.Cog.listener()
    async def on_member_join(self, member):
        global invites
        if not member.bot:
            old_inv = invites[member.guild.id]
            new_inv = await member.guild.invites()
            for invite in old_inv:
                if invite.uses < int(self.code2inv(new_inv, invite.code).uses):
                    invites[member.guild.id] = new_inv
                    with open('./json/invitechannel.json', 'r') as f:
                        invc = json.load(f)
                        channel = self.bot.get_channel(int(invc[str(member.guild.id)]))
                        embed=discord.Embed(title=f'{member.name} Joined!', color=0xff9000)
                        embed.add_field(name="Joined", value=f"<@{member.id}>", inline=True)
                        embed.add_field(name="Invited by", value=f"<@{invite.inviter.id}>", inline=True)
                        embed.add_field(name="Joined with link", value=f"https://discord.gg/{invite.code}", inline=False)
                    await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        global invites
        try:
            invites[member.guild.id] = await member.guild.invites()
        except discord.errors.Forbidden:
            pass

    @commands.command(hidden=True)
    async def invitechannel(self, ctx, *, channel):
        owner = os.environ.get("OWNER")
        print(ctx.author.id)
        print(owner)
        if str(ctx.author.id) == owner:
            with open('./json/invitechannel.json', 'r') as f:
                invc = json.load(f)
            invc[ctx.guild.id] = channel.replace('<', '').replace('>', '').replace('#', '')
            with open('./json/invitechannel.json', 'w') as f:
                json.dump(invc, f, indent=4)
            await ctx.send(f"`invc[{str(ctx.guild.id)}]` set to `{channel.replace('<', '').replace('>', '').replace('#', '')}`!")
        else:
            await ctx.send("Sorry, but you don't have permission to do that.")

    @commands.command(hidden=True)
    async def inviteremove(self, ctx):
        owner = os.environ.get("OWNER")
        if str(ctx.author.id) == owner:
            with open('./json/invitechannel.json', 'r') as f:
                invc = json.load(f)
                invc.pop(ctx.guild.id)
            with open('./json/invitechannel.json', 'w') as f:
                json.dump(invc, f, indent=4)
            await ctx.send('Removed invite channel!')
        else:
            await ctx.send("Sorry, but you don't have permission to do that.")

def setup(bot):
    bot.add_cog(Invite(bot))