from typing import TYPE_CHECKING

from discord.ext import commands

from .cache.cache import MsgCache


class Context(commands.Context):
    async def test():
        return "test"
    
    async def send(self, *args,**kwargs):
        oldmsg = MsgCache.get_cache(self.message.id)
        newmsg=None
        if oldmsg:
            to_edit = super().channel.get_message(oldmsg)
            newmsg = await to_edit.edit(*args,**kwargs)
            MsgCache.update(self.message.id,newmsg.id)
        return newmsg or await super().send(*args,**kwargs)


    async def reply(self, *args,**kwargs):
        oldmsg = MsgCache.get_cache(super().message.id)
        newmsg=None
        if oldmsg:
            to_edit = super().channel.get_message(oldmsg)
            newmsg = await to_edit.edit(*args,**kwargs)
            MsgCache.update(super().message.id,newmsg.id)
        return newmsg or await super().reply(*args,**kwargs)




