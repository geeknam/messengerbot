import abc


class Attachment:

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
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

    def to_dict(self):
        _super_obj = super(ImageAttachment, self)
        return _super_obj.to_dict()


class TemplateAttachment(Attachment):

    attachment_type = 'template'

    def __init__(self, template):
        self.template = template

    @property
    def payload(self):
        return self.template.to_dict()

    def to_dict(self):
        _super_obj = super(TemplateAttachment, self)
        return _super_obj.to_dict()
