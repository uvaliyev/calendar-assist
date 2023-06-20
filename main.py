import pycronofy
from dotenv import load_dotenv
import os
from script import eventer

load_dotenv()

access_token = os.environ['ACCESS_TOKEN']
client_secret = os.environ['CLIENT_SECRET']
calendar_id = os.environ['CALENDAR_ID']
key = os.environ['OPENAI_API']


cronofy = pycronofy.Client(access_token=access_token)

prompt = """schedule me Speaking club on June 22, 13:00 - 14:30. Topic: "Comfort Zone”, adress is Bayzakov str., 280, American Space & Makerspace.
"""

v = eventer(key, prompt)

event = eval(v)

cronofy.upsert_event(calendar_id=calendar_id, event=event)