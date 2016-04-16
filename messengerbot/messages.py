import json


class Message(object):

    def __init__(self, text=None, attachment=None):
        if not text and not attachment:
            raise ValueError()
        self.text = text
        self.attachment = attachment

    def to_dict(self):
        data = {}
        if self.text:
            data['text'] = self.text
        if self.attachment:
            data['attachment'] = self.attachment.to_dict()
        return data


class Recipient(object):

    def __init__(self, recipient_id=None, phone_number=None):
        if not recipient_id and not phone_number:
            raise ValueError('<Recipient> id or phone_number must be set')
        self.recipient_id = recipient_id
        self.phone_number = phone_number

    def to_dict(self):
        if self.recipient_id:
            return {'id': self.recipient_id}
        return {'phone_number': self.phone_number}


class MessageRequest(object):

    NOTIFICATION_TYPE_OPTIONS = (
        'REGULAR', 'SILENT_PUSH', 'NO_PUSH'
    )

    def __init__(self, recipient, message, notification_type=None):
        self.recipient = recipient
        self.message = message
        self._notification_type = notification_type

    @property
    def notification_type(self):
        if self._notification_type:
            if self._notification_type not in self.NOTIFICATION_TYPE_OPTIONS:
                raise ValueError()
        return self._notification_type

    def to_dict(self):
        data = {
            'recipient': self.recipient.to_dict(),
            'message': self.message.to_dict()
        }
        if self.notification_type:
            data['notification_type'] = self.notification_type
        return data

    def serialise(self):
        return json.dumps(self.to_dict())
