import discord
from discord.ext import commands

bot = commans.Bot(command_prefix="RogerLeBot ")

@bot.event
asyncdef on_ready():
    print("Je suis en vie")

bot.run("2823cb5201179dbd7efef36774cf2c1ce047e95904d75878e0dc6798613cd8f0")
