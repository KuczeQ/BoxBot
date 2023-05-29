import discord 
from discord import File, app_commands, integrations
from discord.ext import commands, tasks
import os
import random

class Funny(commands.Cog):
    def __init__(self, bot:commands.Bot) -> None:
        self.bot=bot

    @app_commands.command(name="randomnumber", description="A random number from the range selected by the user")
    async def randomn(self, inte:discord.interactions, frome: int, to: int):
        embed=discord.Embed(title=f"Random Number: {random.randint(frome, to)}", color=0x00ff00)
        await inte.response.send_message(embed=embed)

async def setup(bot:commands.Bot) -> None:
    print("Uploaded Funny Cog")
    await bot.add_cog(Funny(bot))