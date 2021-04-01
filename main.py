import discord
from discord.ext import commands
from discord_slash import SlashCommand

intents = discord.Intents.all()
bot = commands.Bot(
    command_prefix="::",
    case_insensitive=True,
    intents=intents
)
slash = SlashCommand(bot, sync_commands=True)


@bot.event
async def on_ready():
    print(bot.user)
    print("Readying up")

extensions = [
    "cogs.games"
]

if __name__ == "__main__":
    for extension in extensions:
        bot.load_extension(extension)
        print(f"Loaded {extension}")

_TOKEN = open("TOKEN", 'r').read()
bot.run(_TOKEN)
