import discord
from discord.ext import commands
import os
import cogs


TOKEN = os.getenv("BOT_TOKEN")

bot = commands.Bot(command_prefix="!", description="Bot qui check l'état des PC de TC")

# Cogs
bot.add_cog(cogs.ScanRoomCommand(bot))


@bot.event
async def on_ready():
    print(f"{bot.user} connected to discord")

if __name__ == '__main__':
    bot.run(TOKEN)
