from unittest import TestCase
from messengerbot import webhooks
from mock import patch


class WebhookTestCase(TestCase):

    def test_message_webhook(self):
        self.payload = {
          "object":"page",
          "entry":[
            {
              "id":"PAGE_ID",
              "time":1458696618911,
              "messaging":[
                {
                  "sender":{
                    "id":"USER_ID"
                  },
                  "recipient":{
                    "id":"PAGE_ID"
                  },
                  "timestamp":1458696618268,
                  "message":{
                    "mid":"mid.1458696618141:b4ef9d19ec21086067",
                    "seq":51,
                    "attachments":[
                      {
                        "type":"image",
                        "payload":{
                          "url":"IMAGE_URL"
                        }
                      }
                    ]
                  }
                }
              ]
            }
          ]
        }

        wh = webhooks.Webhook(self.payload)
        self.assertTrue(
            wh.entries[0].messaging[0].is_message
        )
        

    def test_delivery_webhook(self):
        self.payload = {
           "object":"page",
           "entry":[
              {
                 "id":"PAGE_ID",
                 "time":1458668856451,
                 "messaging":[
                    {
                       "sender":{
                          "id":"USER_ID"
                       },
                       "recipient":{
                          "id":"PAGE_ID"
                       },
                       "delivery":{
                          "mids":[
                             "mid.1458668856218:ed81099e15d3f4f233"
                          ],
                          "watermark":1458668856253,
                          "seq":37
                       }
                    }
                 ]
              }
           ]
        }

        wh = webhooks.Webhook(self.payload)
        self.assertTrue(
            wh.entries[0].messaging[0].is_delivery
        )


    def test_postback_webhook(self):
        self.payload = {
          "object":"page",
          "entry":[
            {
              "id":"PAGE_ID",
              "time":1458692752478,
              "messaging":[
                {
                  "sender":{
                    "id":"USER_ID"
                  },
                  "recipient":{
                    "id":"PAGE_ID"
                  },
                  "timestamp":1458692752478,
                  "postback":{
                    "payload":"USER_DEFINED_PAYLOAD"
                  }
                }
              ]
            }
          ]
        }

        wh = webhooks.Webhook(self.payload)
        self.assertTrue(
            wh.entries[0].messaging[0].is_postback
        )