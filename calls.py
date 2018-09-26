# -*- coding: utf-8 -*-
import requests, json, os


base_url = 'https://api.groupme.com/v3/'
token = os.environ['GM_API_KEY']
bot_id = os.environ['ROOMMATE_BOT_ID']

class NotReached(Exception):
    pass


def post_message(string, url="https://api.groupme.com/v3/bots/post", bot_id=bot_id):
    """Posts a string to the groupchat arguments"""

    data = {
    "text": string,
    "bot_id": bot_id
    }

    r = requests.post(url, data=data)

def read_messages(n, url=(base_url + "groups/38611088/messages?")):
    """Returns a list of the last n messages details as (string, sender, time)
    if request fails raise NotReached"""

    limit = "&limit=%d&" % n
    url = url + limit + token
    r = requests.get(url)
    
    try:

        messages = json.loads(r.text)['response']["messages"]
        return [(messes['text'], messes['name'], messes['created_at'], messes['id']) for messes in messages]

    except TypeError:

        raise NotReached("read_message request call returned 'None'")

    except KeyError:

        error_string = "Either a groupme update broke your system, or response code isn't 200. Response code: 
        %d" % json.loads(r.text)['meta']['code']
        raise NotReached(error_string)

def like(id, url=""):
    """Likes message by message id **unimplimented**"""
    pass
