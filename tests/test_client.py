from unittest import TestCase
from messengerbot import MessengerClient, messages, MessengerException
from mock import patch


class ClientTestCase(TestCase):

    @patch('requests.post')
    def test_client_send(self, mock_post):

        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            'success': True
        }

        messenger = MessengerClient(access_token='1234')

        recipient = messages.Recipient(recipient_id='123')
        message = messages.Message(text='Hello World')
        request = messages.MessageRequest(recipient, message)
        messenger.send(request)

        mock_post.assert_called_with(
            'https://graph.facebook.com/v2.6/me/messages',
            json={
                "message": {"text": "Hello World"},
                "recipient": {"id": "123"}
            },
            params={'access_token': '1234'}
        )
        
    @patch('requests.post')
    def test_client_send_error_with_error_data(self, mock_post):

        mock_post.return_value.status_code = 190
        mock_post.return_value.json.return_value = {
            "error":{
                     "message":"Invalid parameter",
                     "type":"FacebookApiException",
                     "code":100,
                     "error_data":"No matching user found.",
                     "fbtrace_id":"D2kxCybrKVw"
                     }
        }

        messenger = MessengerClient(access_token='1234')

        recipient = messages.Recipient(recipient_id='123')
        message = messages.Message(text='Hello World')
        request = messages.MessageRequest(recipient, message)
        self.assertRaises(MessengerException, messenger.send, request)
        mock_post.assert_called_with(
            'https://graph.facebook.com/v2.6/me/messages',
            json={
                "message": {"text": "Hello World"},
                "recipient": {"id": "123"}
            },
            params={'access_token': '1234'}
        )
        
    @patch('requests.post')
    def test_client_send_error_with_no_error_data(self, mock_post):

        mock_post.return_value.status_code = 190
        mock_post.return_value.json.return_value = {
            'error': {u'message': u'This Page access token belongs to a Page that has been deleted.', u'code': 190, u'type': u'OAuthException'}
        }

        messenger = MessengerClient(access_token='1234')

        recipient = messages.Recipient(recipient_id='123')
        message = messages.Message(text='Hello World')
        request = messages.MessageRequest(recipient, message)
        self.assertRaises(MessengerException, messenger.send, request)
        mock_post.assert_called_with(
            'https://graph.facebook.com/v2.6/me/messages',
            json={
                "message": {"text": "Hello World"},
                "recipient": {"id": "123"}
            },
            params={'access_token': '1234'}
        )
    
    @patch('requests.post')
    def test_client_subscribe(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            'success': True
        }
        messenger = MessengerClient(access_token='1234')
        messenger.subscribe_app()

        mock_post.assert_called_with(
            'https://graph.facebook.com/v2.6/me/subscribed_apps',
            params={'access_token': '1234'}
        )