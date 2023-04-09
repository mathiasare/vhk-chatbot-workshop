import os
import discord
from dotenv import load_dotenv
from bot import *

# Laeme globaalsed muutujad .env failist
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Seame juturoboti õigused
intents = intents=discord.Intents.default()
# intents.message_content = True

# Loome discordiga suhtlemise "client" objekti
client = discord.Client(intents = intents)

# Event listener meetodid, sündmustele reageerimiseks
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


####################################################
######## LISA SIIA on_message() FUNKTSIOON #########




####################################################

# Programmi käivitamine
client.run(TOKEN)