import requests
from messengerbot import MessengerError

class MessengerUserProfile(object):
    available_fields = ['first_name',
                        'last_name',
                        'profile_pic',
                        'locale',
                        'timezone',
                        'gender']
    GRAPH_API_BASE_URL = 'https://graph.facebook.com/v2.6/'

    def __init__(self, access_token, recipient):
        self.access_token = access_token
        self.recipient = recipient
        for af in self.available_fields:
            setattr(self, af, None)

    def get_user_profile(self):
        fields = ','.join(self.available_fields)
        url = '{}{}'.format(self.GRAPH_API_BASE_URL, self.recipient.recipient_id)
        params = {'access_token': self.access_token,
                  'fields' : fields}
        response = requests.get(url, params=params)
        if response.status_code != 200:
            MessengerError(
                **response.json()['error']
                ).raise_exception()
        json_response = response.json()
        for af in self.available_fields:
            if af in json_response:
                setattr(self, af, json_response[af])
        return json_response
