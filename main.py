import os
import discord
import requests
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"? Logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot or not message.content.strip():
        return
    user_msg = message.content.strip()
    headers = {"x-goog-api-key": GEMINI_API_KEY}
    payload = {
        "contents": [{
            "parts": [{"text": user_msg}]
        }]
    }
    try:
        resp = requests.post(GEMINI_API_URL, json=payload, headers=headers, timeout=12)
        resp.raise_for_status()
        data = resp.json()
        ai_text = data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "I'm here to help!")
    except Exception:
        ai_text = "? Sorry, I'm having trouble reaching Gemini AI right now."
    ai_text += "\n\n?? Check out Aeosync: https://aeosync.deno.dev/"
    await message.reply(ai_text)

bot.run(DISCORD_TOKEN)
