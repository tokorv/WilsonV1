from discord.ext import commands
import discord, os

class Dev(commands.Cog, name="Developer Commands"):
	def __init__(self, bot):
		self.bot = bot

	@commands.group(
		name="dev",
		pass_context=True
	)
	async def dev(self, ctx):
		"""
		Run developer only commands.
		"""
		if ctx.invoked_subcommand is None:
			embed = discord.Embed(colour=discord.Colour.red())
			embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
			embed.add_field(name="Error",value="Your command required a subcommand. None was provided.", inline=False)
			await ctx.send(embed=embed)
		else:
			self.stream.load(ctx.author.id, "./data/user/")
			if int(self.stream.data["active_access_level"]) == 0:
				self.access = True
			else:
				embed = discord.Embed(colour=discord.Colour.red())
				embed.set_author(name="Authentification failed!", icon_url=ctx.author.avatar_url)
				await ctx.send(embed=embed)
				self.access = False

	@dev.command()
	async def load(self, ctx, extension):
		with open("./config/cogs.txt",'a') as f:
			f.write(f"\n{extension}")
			self.bot.load_extension("cogs." + extension)
			embed = discord.Embed(colour=discord.Colour.purple())
			embed.set_author(name=f"{extension} was loaded!", icon_url=ctx.author.avatar_url)
			await ctx.send(embed=embed)
	

def setup(bot):
	bot.add_cog(Dev(bot))