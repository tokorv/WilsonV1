import os
import discord
from keep_alive import keep_alive
from discord.ext import commands
import lib.math as math

bot = commands.Bot(
	command_prefix="::",  
	case_insensitive=True
)

bot.author_id = None # for now

@bot.event 
async def on_ready(): 
    print("I'm in")
    print(bot.user) 

extensions = [
	"cogs.dev",
	"cogs.math"
]

if __name__ == '__main__':  
	for extension in extensions:
		bot.load_extension(extension)

keep_alive()  
token = os.environ.get("DISCORD_BOT_SECRET") 
bot.run(token)  