import os
from telethon import TelegramClient, events, types
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
allowed_user = os.environ['ALLOWED_USER']  # Allowed user's username

cronofy = pycronofy.Client(access_token=access_token)

client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

async def user_allowed(event):
    user = await event.get_sender()
    if user.username != allowed_user:
        await event.respond('You are not allowed to use this bot. author: @uvaliyev_a')
        return False
    return True

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    if await user_allowed(event):
        await event.respond('Hello! I am a bot to schedule your events. Send me the details.')

@client.on(events.NewMessage(pattern='/schedule'))
async def schedule(event):
    if await user_allowed(event):
        prompt = event.text.replace('/schedule ', '')
        v = eventer(key, prompt)
        event_info = eval(v)
        cronofy.upsert_event(calendar_id=calendar_id, event=event_info)
        await event.respond('Your event has been scheduled.')

client.run_until_disconnected()
