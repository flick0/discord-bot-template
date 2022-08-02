import traceback
from typing import TYPE_CHECKING

from discord.ext import commands

if TYPE_CHECKING:
    from ..bot import Bot


class CommandErrorHandler(commands.Cog):

    def __init__(self, bot):
        self.bot:'Bot' = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx:commands.Context, error:commands.CommandError):

        if hasattr(ctx.command, 'on_error'):
            return

        cog = ctx.cog
        if cog:
            if cog._get_overridden_method(cog.cog_command_error) is not None:
                return

        ignored = (commands.CommandNotFound, )

        error = getattr(error, 'original', error)

        if isinstance(error, ignored):
            return
        else:
            try:
                raise error
            except:
                self.bot.log.exception(f'Error in command {ctx.command}')
                await ctx.send(f'Error in command {ctx.command}```py\n{traceback.format_exc()}\n```')

    @commands.command()
    async def error(self, ctx:commands.Context):
        await ctx.send(0/0)
    
    @commands.command()
    async def test1(self, ctx:commands.Context):
        await ctx.send(1)

    @commands.command()
    async def test2(self, ctx:commands.Context):
        await ctx.reply(2)



async def setup(bot):
    await bot.add_cog(CommandErrorHandler(bot))