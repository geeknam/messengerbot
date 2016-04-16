from unittest import TestCase
from messengerbot import messages, attachments, templates, elements


class MessagesTestCase(TestCase):

    def setUp(self):
        self.recipient = messages.Recipient(recipient_id='123')

    def test_text_message(self):
        message = messages.Message(text='Hello World')
        request = messages.MessageRequest(self.recipient, message)

        self.assertEquals(
            request.serialise(),
            '{"message": {"text": "Hello World"}, "recipient": {"id": "123"}}'
        )

    def test_message_notification_type(self):
        message = messages.Message(text='Hello World')
        request = messages.MessageRequest(self.recipient, message, 'INVALID')
        self.assertRaises(ValueError, request.serialise)

        request = messages.MessageRequest(self.recipient, message, 'REGULAR')
        self.assertIsInstance(request.serialise(), str)

    def test_image_url(self):
        attachment = attachments.ImageAttachment(
            url='https://petersapparel.com/img/shirt.png'
        )
        message = messages.Message(attachment=attachment)
        request = messages.MessageRequest(self.recipient, message)
        self.assertEquals(
            request.serialise(),
            '{"message": {"attachment": {"type": "image", "payload": {"url": "https://petersapparel.com/img/shirt.png"}}}, "recipient": {"id": "123"}}'
        )

    def test_button_template(self):
        web_button = elements.WebUrlButton(
            title='Show website',
            url='https://petersapparel.parseapp.com'
        )
        postback_button = elements.PostbackButton(
            title='Start chatting',
            payload='USER_DEFINED_PAYLOAD'
        )
        template = templates.ButtonTemplate(
            text='What do you want to do next?',
            buttons=[
                web_button, postback_button
            ]
        )
        attachment = attachments.TemplateAttachment(template=template)

        message = messages.Message(attachment=attachment)
        request = messages.MessageRequest(self.recipient, message)

        self.assertEquals(
            request.serialise(),
            '{"message": {"attachment": {"type": "template", "payload": {"template_type": "button", "text": "What do you want to do next?", "buttons": [{"url": "https://petersapparel.parseapp.com", "type": "web_url", "title": "Show website"}, {"type": "postback", "payload": "USER_DEFINED_PAYLOAD", "title": "Start chatting"}]}}}, "recipient": {"id": "123"}}'
        )

    def test_generic_template(self):
        element = elements.Element(
            title='Classic White T-Shirt',
            image_url='http://petersapparel.parseapp.com/img/item100-thumb.png',
            subtitle='Soft white cotton t-shirt is back in style',
            buttons=[
                elements.WebUrlButton(
                    title='View Item',
                    url='https://petersapparel.parseapp.com/view_item?item_id=100',
                )
            ]
        )

        template = templates.GenericTemplate([element])
        attachment = attachments.TemplateAttachment(template)
        message = messages.Message(attachment=attachment)
        request = messages.MessageRequest(self.recipient, message)
        # Assert we can serialise
        self.assertIsInstance(request.serialise(), str)
