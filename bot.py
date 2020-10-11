from json import dumps

import requests

import constants as c
import utility as util

def send_new_case_notification(message):
    """Hangouts Chat incoming webhook quickstart."""
    url = 'https://chat.googleapis.com/v1/spaces/AAAAahyjnKw/messages?key={}&token={}%3D'.format(c.GCHAT_API_KEY, c.GCHAT_TOKEN)
    bot_message = {
        'text' : message
    }

    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
    try:
        response = requests.post(url=url,
            headers=message_headers,
            data=dumps(bot_message),
        )

        print(response.content)
    except Exception as e:
        util.update_error_log_transactions('bot', e)
