from messengerbot.messages import Recipient
from datetime import datetime


class WebhookMessaging(object):

    def __init__(self, sender, recipient, timestamp, **kwargs):
        self.sender = Recipient(recipient_id=sender['id'])
        self.recipient = Recipient(recipient_id=sender['id'])
        self.timestamp = datetime.utcfromtimestamp(timestamp)

        for key, value in kwargs.items():
            self.__dict__['_%s' % key] = value

    @property
    def is_message(self):
        return hasattr(self, '_message')

    @property
    def is_delivery(self):
        return hasattr(self, '_delivery')

    @property
    def is_postback(self):
        return hasattr(self, '_postback')


class WebhookEntry(object):

    def __init__(self, id, time, messaging):
        self.id = id
        # TODO parse epoch
        self.time = datetime.utcfromtimestamp(time)
        self.messaging = [
            WebhookMessaging(**each)
            for each in messaging
        ]


class Webhook(object):

    def __init__(self, payload):
        self.payload = payload

    @property
    def entries(self):
        return [
            WebhookEntry(**entry)
            for entry in self.payload['entry']
        ]
