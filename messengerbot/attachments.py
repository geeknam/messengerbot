
class Attachment(object):

    def to_dict(self):
        return {
            'type': self.attachment_type,
            'payload': self.payload
        }


class ImageAttachment(Attachment):

    attachment_type = 'image'

    def __init__(self, url):
        self._url = url

    @property
    def payload(self):
        return {
            'url': self._url
        }


class TemplateAttachment(Attachment):

    attachment_type = 'template'

    def __init__(self, template):
        self.template = template

    @property
    def payload(self):
        return self.template.to_dict()
