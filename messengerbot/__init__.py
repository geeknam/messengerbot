import os
import requests


class MessengerException(Exception):
    pass


class MessengerError(object):

    def __init__(self, *args, **kwargs):
        self.__dict__.update(**kwargs)

    def raise_exception(self):
        raise MessengerError(
            self.error_data
        )


class MessengerClient(object):

    GRAPH_API_URL = 'https://graph.facebook.com/v2.6/me/messages'

    def __init__(self, access_token):
        self.access_token = access_token

    def send(self, message):
        params = {
            'access_token': self.access_token
        }
        response = requests.post(
            self.GRAPH_API_URL, params=params,
            json=message.serialise()
        )
        if response.status_code != 200:
            MessengerError(
                **response.json()['error']
            ).raise_exception()
        return response.json()


ENV_KEY = 'MESSENGER_PLATFORM_ACCESS_TOKEN'

if ENV_KEY in os.environ:
    messenger = MessengerClient(
        access_token=os.environ[ENV_KEY]
    )
