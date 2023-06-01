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
        embed.set_footer(text="Create by github.com/Gejfish", icon_url="https://avatars.githubusercontent.com/u/76708563?v=4")
        await inte.response.send_message(embed=embed)

    @app_commands.command(name="pandaimg", description="Send a Panda image")
    async def panda(self, inte:discord.interactions):
        fact = requests.get("https://some-random-api.com/animal/panda").json()["fact"]
        embed=discord.Embed(title="Panda",description=f"The panda fact: {fact}", color=0x00ff00)
        embed.set_image(url=requests.get("https://some-random-api.com/animal/panda").json()["image"])
        embed.set_footer(text="Create with https://some-random-api.com", icon_url="https://avatars.githubusercontent.com/u/65510168?v=4")
        await inte.response.send_message(embed=embed) 
    
    @app_commands.command(name="catimg", description="Send a Cat image")
    async def cat(self, inte:discord.interactions):
        fact = requests.get("https://some-random-api.com/animal/cat").json()["fact"]
        embed=discord.Embed(title="Cat",description=f"The cat fact: {fact}", color=0x00ff00)
        embed.set_image(url=requests.get("https://some-random-api.com/animal/cat").json()["image"])
        embed.set_footer(text="Create with https://some-random-api.com", icon_url="https://avatars.githubusercontent.com/u/65510168?v=4")
        await inte.response.send_message(embed=embed)

    @app_commands.command(name="mcachievement", description="Minecraft aachievement with chosen text")
    async def achievement(self, inte:discord.interactions, text:str):            
        text = text.replace(" ", "+").replace("ś", "s").replace("ę", "e").replace("ż", "z").replace("ź", "z").replace("ł", "l").replace("ó", "o").replace("ą", "a").replace("ć", "c").replace("Ś", "S").replace("Ę", "E").replace("Ż", "Z").replace("Ź", "Z").replace("Ł", "L").replace("Ó", "O").replace("Ą", "A").replace("Ć", "C")
        img = requests.get(f"https://minecraftskinstealer.com/achievement/{random.randint(1, 40)}/Achievement+Get%21/{text}").content
        embed = discord.Embed(title="Achievement", description=text, color=0x00ff00)
        open("achievement.png", "wb").write(img)
        embed.set_image(url="attachment://achievement.png")
        embed.set_footer(text="Create by github.com/Gejfish", icon_url="https://avatars.githubusercontent.com/u/76708563?v=4")
        await inte.response.send_message(file=File("achievement.png"), embed=embed)
        os.remove("achievement.png")

    @app_commands.command(name="kiss", description="Kiss chosen user")
    async def kiss(self, inte:discord.interactions, member: discord.Member):    
        if member.name == inte.user.name:
            embed = discord.Embed(title="U cant kiss yourself", color=0x00ff00)
            embed.set_footer(text="Create with https://nekos.life", icon_url="https://avatars.githubusercontent.com/u/65510168?v=4")
            return await inte.response.send_message(embed=embed)
        else:
            embed = discord.Embed(title=f"**{inte.user.name}** kiss **{member.name}**!", color=0x00ff00) 
            embed.set_image(url=requests.get("https://nekos.life/api/kiss").json()["url"])
            embed.set_footer(text="Create with https://nekos.life", icon_url="https://avatars.githubusercontent.com/u/65510168?v=4")
            return await inte.response.send_message(embed=embed)
    
    @app_commands.command(name="servericon", description="Show server icon")
    async def servericon(self, inte: discord.Interaction):
        guild_id = inte.guild_id
        guild = self.bot.get_guild(guild_id)
        icon_url = guild.icon.url if guild.icon else None
        if icon_url:
            embed = discord.Embed(title="Server Icon", color=0x00ff00)
            embed.set_image(url=icon_url)
            embed.set_footer(text="Create by github.com/KuczeQ", icon_url="https://avatars.githubusercontent.com/u/65510168?v=4")
            await inte.response.send_message(embed=embed)
        else:
            embed = discord.Embed(title="Server does not have an icon", color=0x00ff00)
            embed.set_footer(text="Create by github.com/KuczeQ", icon_url="https://avatars.githubusercontent.com/u/65510168?v=4")
            await inte.response.send_message(embed=embed)

    
async def setup(bot:commands.Bot) -> None:
    print("Uploaded Funny Cog")
    await bot.add_cog(Funny(bot))   
