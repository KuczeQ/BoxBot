import discord 
from discord import File, app_commands, integrations
from discord.ext import commands, tasks
import os

class Main(commands.Cog):
    def __init__(self, bot:commands.Bot) -> None:
        self.bot=bot
    
    @app_commands.command(name="calculate", description="Make a math expressions")
    async def calculate(self, inte:discord.interactions, calc: str):
        try:
            resultat = eval(calc)
            embed=discord.Embed(title=f"Resultat  {resultat}",description=f"{calc} = {resultat}", color=0x00ff00)
            embed.set_footer(text="Create by github.com/KuczeQ", icon_url="https://avatars.githubusercontent.com/u/65510168?v=4")
            await inte.response.send_message(embed=embed)
        except Exception as e:
            embed=discord.Embed(title="Wrong math expression", color=0x00ff00)
            embed.set_footer(text="Create by github.com/KuczeQ", icon_url="https://avatars.githubusercontent.com/u/65510168?v=4")
            await inte.response.send_message(embed=embed)

    @app_commands.command(name = "useravatar", description="Show user avatar")
    async def avatar(self, inte:discord.Interaction, user:discord.Member):
        embed = discord.Embed(title=f"{user.name} Avatar", color=0x00ff00)
        embed.set_image(url=user.display_avatar.url)
        embed.set_footer(text="Create by github.com/KuczeQ", icon_url="https://avatars.githubusercontent.com/u/65510168?v=4")
        await inte.response.send_message(embed=embed)

async def setup(bot:commands.Bot) -> None:
    print("Uploaded Main Cog")
    await bot.add_cog(Main(bot))