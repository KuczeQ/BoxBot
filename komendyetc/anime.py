import discord
from discord.ext import commands
from discord import File, app_commands, integrations
from discord.ext import commands, tasks
import requests


query = '''
query ($search: String) {
  Media (search: $search, type: ANIME) {
    id
    title {
      romaji
      english
      native
    }
    description
    averageScore
    episodes
    popularity
    coverImage {
      medium
    }
    bannerImage
  }
}
'''

query_character = '''
query ($search: String) {
  Character (search: $search) {
    id
    name {
      full
      native
    }
    description
    image {
      large
    }
    media {
      nodes {
        title {
          romaji
          english
          native
        }
      }
    }
  }
}
'''

url = 'https://graphql.anilist.co'

class Anime(commands.Cog):
    def __init__(self, bot:commands.Bot) -> None:
        self.bot=bot

    @app_commands.command(name='animesearch', description='Search for chosen anime')
    async def animesearch(self, inte:discord.interactions, search_query: str):
        variables = {
            'search': search_query
        }

        response = requests.post(url, json={'query': query, 'variables': variables})

        if response.status_code == 200:
            data = response.json()
            media = data['data']['Media']
            title = media['title']['romaji']
            description = media['description']
            average_score = media['averageScore']
            popularity = media['popularity']
            episodes = media['episodes']
            image_url = media['coverImage']['medium'] if 'coverImage' in media else None
            banner_url = media['bannerImage'] if 'bannerImage' in media else None

            embed = discord.Embed(title=title, description=description, color=0x00ff00)
            embed.add_field(name='Average Score', value=average_score, inline=True)
            embed.add_field(name='Episodes', value=episodes, inline=True)
            embed.add_field(name='Popularity', value=popularity, inline=True)
            embed.set_footer(text="Create with https://anilist.co/", icon_url="https://avatars.githubusercontent.com/u/65510168?v=4")
            
            if image_url:
              embed.set_thumbnail(url=image_url)
            elif banner_url:
                embed.set_thumbnail(url=banner_url)

            await inte.response.send_message(embed=embed)
        else:
            embed = discord.Embed(title="Error", description="Error with connecting with AniList API", color=0x00ff00)
            embed.set_footer(text="Create with https://anilist.co/", icon_url="https://avatars.githubusercontent.com/u/65510168?v=4")
            await inte.response.send_message(embed=embed)


    @app_commands.command(name='charactersearch', description='Search for chosen anime character')
    async def animecharsearch(self, inte:discord.interactions, search_query: str):
        variables = {
            'search': search_query
        }

        response = requests.post(url, json={'query': query_character, 'variables': variables})

        if response.status_code == 200:
            data = response.json()
            character = data['data']['Character']
            name = character['name']['full']
            description = character['description']
            image_url = character['image']['large'] if 'image' in character else None
            media_nodes = character['media']['nodes']

            embed = discord.Embed(title=name, description=description[:1020] + '...', color=0x00ff00)
            embed.set_footer(text="Create with https://anilist.co/", icon_url="https://avatars.githubusercontent.com/u/65510168?v=4")

            if media_nodes:
                anime_list = '\n'.join([media['title']['romaji'] for media in media_nodes[:20]])
                embed.add_field(name='Występuje w anime', value=anime_list, inline=False)


            if image_url:
                embed.set_thumbnail(url=image_url)

            await inte.response.send_message(embed=embed)
        else:
            embed = discord.Embed(title="Error", description="Error with connecting with AniList API", color=0x00ff00)
            await inte.response.send_message(embed=embed)


async def setup(bot:commands.Bot) -> None:
    print("Uploaded Anime Cog")
    await bot.add_cog(Anime(bot))   

