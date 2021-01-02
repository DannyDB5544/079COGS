# Get it? Watcher, Watch dogs, its a cog, I want to shoot myself...
import discord
from redbot.core import commands, checks, Config
from typing import Optional

class WatchCog(commands.Cog):
    """Indivudual User monitoring for those you're pretty sure are horrible,
    but need hard proof."""

    def __init__(self, bot):
        self.bot = bot
        self.conf = Config.get_conf(self, identifier=32187129, force_registration=True)
        self.conf.register_channel(
            target=None
        )
    
    @commands.is_owner()
    @commands.command()
    async def hardreset(self, ctx, Force: Optional[bool] = False):
        """Forcibly remove all watchCog channels globally (NOTE - WIP)"""
        # TODO - I want to incorperate the currently not existing method along the lines of
        # "DeleteChannel" or whatever to recursively KO channels. mostly a debug tool, really.
        # May probably get removed or tagged as disabled.

    
    @commands.mod_or_permissions(manage_messages = True)
    @commands.group()
    async def watchcog(self, ctx):
        """Base command for watchCog. Start here!"""
    
    @watchcog.command()
    async def add(self, ctx, user: Discord.Member):
        # WIP - awaiting confirmation before continuing
        