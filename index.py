import os, signal, sys, time

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
def interrupt(signal, frame) :
    time.sleep(1)
    print('\nEncerrando...')
    sys.exit(0)

signal.signal(signal.SIGINT, interrupt)
signal.signal(signal.SIGQUIT, interrupt)


client = genai.Client()
web_search = types.Tool(
    google_search=types.GoogleSearch
)

config = types.GenerateContentConfig(
    tools=[web_search]
)

execute = True
while execute :
    question = input("Oque te apetece? (Digite 'q' para encerrar): ")
    if question == 'q':
        time.sleep(1)
        print('\nEncerrando...')
        sys.exit(0)

    response = client.models.generate_content(
        model=os.environ.get('MODEL_ID'),
        contents=question,
        config=config
    )

    print(response.text)