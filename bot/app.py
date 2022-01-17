#####################################################################
#
# * This file is part of DiscordBotPy, a role-assigning Discord bot.
# * Written by Huygen (Dhiv Joseph).
# *
# * This program is free software: you can redistribute it and/or modify
# * it under the terms of the GNU General Public License V3 as published by
# * the Free Software Foundation, version 3.
# *
# * This program is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# * GNU General Public License V3 for more details.
# *
# * You should have received a copy of the GNU General Public License V3
# * along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#####################################################################

#!/usr/bin/env python3
import discord
import os
import logging
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# enable intents, see docs to learn about intents in Discord API:
# https://discordpy.readthedocs.io/en/stable/intents.html
intents = discord.Intents.default()

# logs
logging.basicConfig(filename='../logs/bot.log', encoding='utf-8', level=logging.DEBUG)

def main():
    
    # init client
    client = discord.Client()

    @client.event
    async def on_ready():
        guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
        logging.info('SUCCESS: Client Ready')
        
        print(f'{client.user} has connected to:')
        print(f'{guild.name}(id: {guild.id})')

        members = '\n - '.join([member.name for member in guild.members])
        print(f'Guild members:\n - {members}')

    client.run(TOKEN)


if __name__ == "__main__":
    main()
