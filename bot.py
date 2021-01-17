import os, discord
from dotenv import load_dotenv
from shutUp import ShutUpBot

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client= ShutUpBot()
client.run(TOKEN)