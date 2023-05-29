import discord 
from discord import File, app_commands, integrations
from discord.ext import commands, tasks
import os
import random
import requests

class Funny(commands.Cog):
    def __init__(self, bot:commands.Bot) -> None:
        self.bot=bot

    @app_commands.command(name="randomnumber", description="A random number from the range selected by the user")
    async def randomn(self, inte:discord.interactions, of: int, to: int):
        embed=discord.Embed(title=f"Random Number: {random.randint(of, to)}", color=0x00ff00)
        await inte.response.send_message(embed=embed)

    @app_commands.command(name="pandaimg", description="Send a Panda image")
    async def panda(self, inte:discord.interactions):
        embed=discord.Embed(title="Panda", color=0x00ff00)
        embed.set_image(url=requests.get("https://some-random-api.com/animal/panda").json()["image"])
        await inte.response.send_message(embed=embed) 

async def setup(bot:commands.Bot) -> None:
    print("Uploaded Funny Cog")
    await bot.add_cog(Funny(bot))   
