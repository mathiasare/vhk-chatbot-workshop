import os
import discord
from dotenv import load_dotenv
from bot import *

# Laeme globaalsed muutujad .env failist
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Seame juturoboti õigused
intents = intents=discord.Intents.default()
intents.message_content = True

# Loome discordiga suhtlemise "client" objekti
client = discord.Client(intents = intents)

####################################################
# Event listener meetodid, sündmustele reageerimiseks
@client.event
async def on_ready():
    print(f'Tere, maailm! Minu nimi on {client.user}.')
    
    
####################################################
######## LISA SIIA on_message() FUNKTSIOON #########

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await message.channel.send(message.content)


####################################################

# Programmi käivitamine
client.run(TOKEN)