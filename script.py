
import openai

def eventer(key, prompt):
    openai.api_key = key

    baseprompt="""Schedule me a Board meeting in the Board room, describing Discuss plans for the next quarter, for July 16, from 21:30 to 23:00 (UTC+6).

    You need to response me with one message like this:

    '''
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
    '''
    If you understand, without any text, with only json code, """

    baseprompt = baseprompt + prompt
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature = 0.2,
        max_tokens = 1000,
        messages = [
        {"role": "user", "content": baseprompt}
        ]
    )

    return response['choices'][0]['message']['content']