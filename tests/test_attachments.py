from unittest import TestCase
from messengerbot import (templates, attachments, elements)


class AttachementTestCase(TestCase):

    def test_attachment(self):
        """
        Attachment cannot be instantiated
        """
        message = "Can't instantiate abstract class Attachment with abstract methods to_dict"
        with self.assertRaises(TypeError) as exp:
            attachments.Attachment()
        self.assertEqual(exp.exception.message, message)

    def test_image_attachment(self):
        """
        to_dict test for ImageAttachment
        """
        url = "http://www.webreality.co.uk/media/1079/i_love_open_source.jpg"
        image_attachement = attachments.ImageAttachment(url)
        _dic = image_attachement.to_dict()
        self.assertEqual(_dic['payload']['url'], url)
        self.assertEqual(_dic['type'], image_attachement.attachment_type)

    def test_template_attachment(self):
        """
        TemplateAttachment
        """
        template_text = 'What do you want to do next?',
        postback_button = elements.PostbackButton(
            title='Start chatting', payload='USER_DEFINED_PAYLOAD')
        template = templates.ButtonTemplate(
            text=template_text, buttons=[postback_button])

        template_attachment = attachments.TemplateAttachment(template=template)
        _dic = template_attachment.to_dict()
        payload = _dic['payload']
        self.assertEqual(_dic['type'],  template_attachment.attachment_type)
        self.assertEqual(payload['text'], template_text)
        self.assertEqual(payload['template_type'], 'button')
