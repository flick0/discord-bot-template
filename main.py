import json

from bot.bot import Bot

with open("./config.json") as f:
    config = json.load(f)
    TOKEN = config["token"]

if __name__ == "__main__":
    Bot().run(TOKEN)