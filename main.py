import pycronofy
from dotenv import load_dotenv
import os

load_dotenv()

access_token = os.environ['ACCESS_TOKEN']
client_secret = os.environ['CLIENT_SECRET']
calendar_id = os.environ['CALENDAR_ID']


cronofy = pycronofy.Client(access_token=access_token)
event = {
    'event_id': "qTtZdczOccgaPncGJaCiLg",
    'summary': "Board meeting",
    'description': "Discuss plans for the next quarter.",
    'start': "2023-06-21T15:30:00Z", # +6H = UTC+6
    'end': "2023-06-21T17:00:00Z",
    'location': {
        'description': "Board room"
    }
}
cronofy.upsert_event(calendar_id=calendar_id, event=event)