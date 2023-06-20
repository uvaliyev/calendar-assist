import os
from telethon import TelegramClient, events
from dotenv import load_dotenv
import pycronofy
from script import eventer

load_dotenv()

access_token = os.environ['ACCESS_TOKEN']
client_secret = os.environ['CLIENT_SECRET']
calendar_id = os.environ['CALENDAR_ID']
key = os.environ['OPENAI_API']
api_id = os.environ['API_ID']  # Telethon app id
api_hash = os.environ['API_HASH']  # Telethon app hash
bot_token = os.environ['BOT_TOKEN']

cronofy = pycronofy.Client(access_token=access_token)

client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond('Hello! I am a bot to schedule your events. Send me the details.')

@client.on(events.NewMessage(pattern='/schedule'))
async def schedule(event):
    prompt = event.text.replace('/schedule ', '')
    v = eventer(key, prompt)
    event_info = eval(v)
    cronofy.upsert_event(calendar_id=calendar_id, event=event_info)
    await event.respond('Your event has been scheduled.')

client.run_until_disconnected()