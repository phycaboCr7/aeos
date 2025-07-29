import os

# Only load audioop if available (not available in Render)
try:
    import audioop
except ImportError:
    audioop = None
    print("audioop not available, disabling audio features.")

import discord
from discord.ext import commands
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_BOT_TOKEN")
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def ask(ctx, *, prompt):
    await ctx.send("Thinking...")

    # replace this with Gemini API code
    response = f"🤖 Gemini reply to: {prompt}"

    await ctx.send(response)

bot.run(TOKEN)
