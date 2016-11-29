class QuickReplyItem(object):
    def __init__(self, content_type, title=None, payload=None, image_url=None):
        if content_type == 'text':
            if not title and not payload:
                raise ValueError('<Message> must be set')

        if len(title) > 20:
            raise ValueError('Quick reply title limit is 20 characters')

        if len(payload) > 1000:
            raise ValueError('Quick reply payload limit is 1000 characters')

        self.content_type = content_type
        self.title = title
        self.payload = payload
        self.image_url = image_url

    def to_dict(self):
        if self.content_type == 'location':
            return {
                'content_type': self.content_type,
                'image_url': self.image_url
            }
        if self.content_type == 'text':
            return {
                'content_type': self.content_type,
                'title': self.title,
                'payload': self.payload,
                'image_url': self.image_url
            }


class QuickReplies(object):
    def __init__(self, quick_replies):
        if not isinstance(quick_replies, list):
            raise ValueError(
                'quick_replies should be a list of QuickReplyItems'
            )
        self._quick_replies = quick_replies

    def to_dict(self):
        return [quick_reply.to_dict() for quick_reply in self._quick_replies]
