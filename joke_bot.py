from slackclient import SlackClient
import requests
import time
import os


bot_token = os.environ["bot_token"]
sc = SlackClient(bot_token)
url = 'https://icanhazdadjoke.com/'
headers = {'Accept': 'text/plain'}


while True:
    r = requests.get(url, headers=headers)
    joke = r.content
    sc.api_call(
        "chat.postMessage",
        channel="#lab",
        text=joke
    )
    time.sleep(14400)
