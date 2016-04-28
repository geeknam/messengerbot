import os
import requests


class MessengerException(Exception):
    pass


class MessengerError(object):

    def __init__(self, *args, **kwargs):
        self.__dict__.update(**kwargs)

    def raise_exception(self):
        raise MessengerException(
            getattr(self, 'error_data', self.message)
        )

class MessengerClient(object):

    GRAPH_API_URL = 'https://graph.facebook.com/v2.6/me'

    def __init__(self, access_token):
        self.access_token = access_token

    def send(self, message):
        params = {
            'access_token': self.access_token
        }
        response = requests.post(
            '%s/messages' % self.GRAPH_API_URL,
            params=params,
            json=message.to_dict()
        )
        if response.status_code != 200:
            MessengerError(
                **response.json()['error']
            ).raise_exception()
        return response.json()

    def subscribe_app(self):
        """
        Subscribe an app to get updates for a page.
        """
        response = requests.post(
            '%s/subscribed_apps' % self.GRAPH_API_URL,
            params={
                'access_token': self.access_token
            }
        )
        return response.status_code == 200


ENV_KEY = 'MESSENGER_PLATFORM_ACCESS_TOKEN'

if ENV_KEY in os.environ:
    messenger = MessengerClient(
        access_token=os.environ[ENV_KEY]
    )
