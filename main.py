import json

from bot.bot import Bot

with open("./.token") as f:
    TOKEN = f.read().strip()

if __name__ == "__main__":
    Bot().run(TOKEN)