import discord
from discord.ext import commands, tasks
import random
import datetime
import os

TOKEN = os.getenv("DISCORD_TOKEN")
FARZAN_ID = 732079711785582664

reminders = [
    "yo @Farzan ask Chris how her day was u npc 💔",
    "friendly reminder @Farzan to not fumble the bag again today 🥀",
    "bro @Farzan if u forget again ur actually finished 💀",
    "@Farzan daily quest: talk to ur queen chris 🙏",
    "yo @Farzan chris finna replace u with chatgpt if u keep lackin 😭",
]

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.dm_messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    daily_reminder.start()

@tasks.loop(time=datetime.time(hour=18, minute=0))  # 6pm
async def daily_reminder():
    user = await bot.fetch_user(FARZAN_ID)
    if user:
        try:
            await user.send(random.choice(reminders))
        except:
            print("DMs ain't workin, mf got em turned off or smth 💀")

bot.run(TOKEN)
