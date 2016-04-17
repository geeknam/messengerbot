from unittest import TestCase
from messengerbot import webhooks
from mock import patch


class WebhookTestCase(TestCase):

    def setUp(self):
        self.payload = {
            "object": "page",
            "entry": [{
                "id": '123',
                "time": 1460905554,
                "messaging": [
                    {
                        "sender": {
                            "id": '1234'
                        },
                        "recipient": {
                            "id": '1234'
                        },
                        "timestamp": 1460905554
                    }
                ]
            }]
        }

    def test_message_webhook(self):
        self.payload['entry'][0]['messaging'][0]['message'] = {
            "mid": "mid.1457764197618:41d102a3e1ae206a38",
            "seq": 73,
            "text": "hello, world!"
        }
        wh = webhooks.Webhook(self.payload)
        self.assertTrue(
            wh.entries[0].messaging[0].is_message
        )

    def test_delivery_webhook(self):
        self.payload['entry'][0]['messaging'][0]['delivery'] = {
            "mids": [
                "mid.1458668856218:ed81099e15d3f4f233"
            ],
            "watermark": 1458668856253,
            "seq": 37
        }
        wh = webhooks.Webhook(self.payload)
        self.assertTrue(
            wh.entries[0].messaging[0].is_delivery
        )

