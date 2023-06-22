import discord 
from discord import File, app_commands, integrations
from discord.ext import commands, tasks

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

    @app_commands.command(name="serverinfo", description="Show information about the server")
    async def serverinfo(self, inte: discord.interactions):
        guild = inte.guild
        total_members = guild.member_count
        online_members = sum(member.status != discord.Status.offline for member in guild.members)
        text_channels = len(guild.text_channels)
        voice_channels = len(guild.voice_channels)
        server_owner = guild.owner.display_name
        guild_id = inte.guild_id
        get_guild = self.bot.get_guild(guild_id)
        icon_url = get_guild.icon.url if get_guild.icon else None

        embed = discord.Embed(title="Server Information", color=0x00ff00)
        embed.add_field(name="Total Members", value=total_members, inline=False)
        embed.add_field(name="Online Members", value=online_members, inline=False)
        embed.add_field(name="Text Channels", value=text_channels, inline=False)
        embed.add_field(name="Voice Channels", value=voice_channels, inline=False)
        embed.add_field(name="Server Owner", value=server_owner, inline=False)
        embed.set_thumbnail(url=icon_url)
        embed.set_footer(text="Created by github.com/KuczeQ", icon_url="https://avatars.githubusercontent.com/u/65510168?v=4")

        await inte.response.send_message(embed=embed)


    @app_commands.command(name="userinfo", description="Show information about a user")
    async def userinfo(self, inte: discord.interactions, member:discord.Member):
        username = member.name
        discriminator = member.discriminator
        idpog = member.id
        avatar_url = member.avatar.url if member.avatar else None

        embed = discord.Embed(title="User Information", color=0x00ff00)
        embed.add_field(name="Username", value=f"{username}#{discriminator}", inline=False)
        embed.add_field(name="Joined Server", value=member.joined_at.strftime("%Y-%m-%d %H:%M:%S"), inline=False)
        embed.add_field(name="ID", value=f"{idpog}", inline=False)
        embed.set_thumbnail(url=avatar_url)
        embed.set_footer(text="Created by github.com/KuczeQ", icon_url="https://avatars.githubusercontent.com/u/65510168?v=4")

        roles = [role.name for role in member.roles if role.name != "@everyone"]
        if roles:
            embed.add_field(name="Roles", value=", ".join(roles), inline=False)
        else:
            embed.add_field(name="Roles", value="No roles", inline=False)

        await inte.response.send_message(embed=embed)


async def setup(bot:commands.Bot) -> None:
    print("Uploaded Main Cog")
    await bot.add_cog(Main(bot))