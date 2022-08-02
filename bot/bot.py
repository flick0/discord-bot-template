import logging
import os
import time

import discord
from discord.ext import commands
from rich.console import Console
from rich.logging import RichHandler


class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        # init logging
        self.set_logging()

        # store start time
        self.start_time = time.time()

        # create commands.Bot
        super().__init__(command_prefix=";",intents=discord.Intents.all(),*args, **kwargs)
    
    def set_logging(self):
        FORMAT = "%(message)s"
        self.console = Console()
        logging.basicConfig(
            level=logging.INFO, format=FORMAT, datefmt="[%X]", handlers=[RichHandler(rich_tracebacks=True,console=self.console)]
        )
        self.log = logging.getLogger("rich")
        self.log.info("Logging set up.")    

    async def on_ready(self):
        self.log.info(f"Logged in as {self.user.name}")
        self.log.info(f"Connected to {len(self.guilds)} servers")
        self.log.info(f"Connected to {len(self.users)} users")
        self.log.info(f"Bot uptime: {time.time() - self.start_time} seconds")
        await self.load_cogs()

    async def load_cogs(self):
        for filename in os.listdir("./bot/commands"):
            if filename.endswith(".py"):
                self.log.info(f"Loading commands: {filename[:-3]}")
                await self.load_extension(f"bot.commands.{filename[:-3]}")    
    
    async def unload_cogs(self):
        for cog in self.cogs:
            self.log.info(f"Unloading commands: {cog}")
            await self.unload_extension(f"bot.commands.{cog}")



    
