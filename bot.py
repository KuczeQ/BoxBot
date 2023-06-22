import discord
from discord.ext import commands
import os

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=".", intents=discord.Intents.all())

    async def setup_hook(self):
        for filename in os.listdir("./komendyetc"):
            if filename.endswith(".py"):
                await self.load_extension(f"komendyetc.{filename[:-3]}")
                await self.tree.sync()

    async def reload_hook(self):
        for filename in os.listdir('./komendyetc'):
            if filename.endswith('.py'):
                await self.reload_extension(f'komendyetc.{filename[:-3]}')
                await self.tree.sync()

    async def on_ready(self):
        print(f"{self.user} Connected with Discord.")

def get_token():
    with open("token.txt", "r") as file:
        token = file.read().strip()
    return token

bot = Bot()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    print('Made by Bartuś O❤#4052 / https://github.com/KuczeQ/Kaguya-Shinomiya-Discord-Bot')
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(name="github.com/KuczeQ", type=discord.ActivityType.watching))

@bot.command(name="restart")
@commands.is_owner()
async def restart(ctx):
    await bot.reload_hook()
    print("restart")

bot.remove_command('help')
bot.run(get_token())