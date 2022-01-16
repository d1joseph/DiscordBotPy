#!/usr/bin/env python3
import discord
import os
import logging
from dotenv import load_dotenv

# token
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# logs
logging.basicConfig(filename='../logs/bot.log', encoding='utf-8', level=logging.DEBUG)

def main():
    
    # init client
    client = discord.Client()

    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')
        logging.info('SUCCESS: Client Ready')

    client.run(TOKEN)

if __name__ == "__main__":
    main()
