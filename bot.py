import discord
from discord.ext import commands
import random
import re

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

random_messages = [
    "Bravo, encore du racisme <:zizouswag:1019679222438047846> ",
    "Perdu sur twitter encore? <:ahiii:986293070985310229> ",
    "C'est vraiment ça ta source? <:jesus:1004421273289494559> ",
    "Source? <:poker_cat:1014203158865641533> ",
    "Du Nasakisme, je vois... <:poker_cat:1014203158865641533> "
]

# Dictionary to store registered links
registered_links = {}

# Regular expression to detect hyperlinks
url_regex = r'https?://[^\s/$.?#].[^\s]*'


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Find hyperlinks in the message
    hyperlinks = re.findall(url_regex, message.content)

    for link in hyperlinks:
        if link in registered_links:
            await message.channel.send("Bravo le repost, bouffon <:poker_cat:1014203158865641533>")
        else:
            registered_links[link] = True

            # Continue with modifying and sending links
            links = [link for link in message.content.split(
            ) if 'twitter.com' in link or 'x.com' in link]
            for link in links:
                if re.match(r'https?://(twitter|x)\.com/.*', link):
                    modified_link = link.replace(
                        "twitter.com", "fxtwitter.com").replace("x.com", "fxtwitter.com")
                    random_message = random.choice(random_messages)
                    await message.channel.send(f"{modified_link}\n{random_message}")

@bot.command()
async def test(message):
    print('Aqui?')
    await message.send('tg_buffoon')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

# Replace 'YOUR_TOKEN' with your Discord bot token
bot.run('TOKEN')
