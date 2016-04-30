

class Element(object):

    def __init__(self, title, item_url=None,
                 image_url=None, subtitle=None, buttons=None):

        self._title = title
        self.item_url = item_url
        self.image_url = image_url
        self._subtitle = subtitle
        self.buttons = buttons

    @property
    def title(self):
        if len(self._title) > 45:
            raise ValueError(
                'Element.title has more than 45 characters'
            )
        return self._title

    @property
    def subtitle(self):
        if self._subtitle:
            if len(self._subtitle) > 80:
                raise ValueError(
                                 'Element.subtitle has more than 80 characters'
                                 )
        return self._subtitle

    def to_dict(self):
        serialised = {
            'title': self.title,
            'item_url': self.item_url,
            'image_url': self.image_url,
            'subtitle': self.subtitle
        }
        if self.buttons:
            serialised['buttons'] = [
                button.to_dict() for button in self.buttons
            ]
        return serialised

class Button(object):

    def __init__(self, title):
        if len(title) > 20:
            raise ValueError('Button title limit is 20 characters')
        self.title = title

    def to_dict(self):
        serialised = {
            'type': self.button_type,
            'title': self.title
        }
        if self.button_type == 'web_url':
            serialised['url'] = self.url
        elif self.button_type == 'postback':
            serialised['payload'] = self.payload
        return serialised


class WebUrlButton(Button):

    button_type = 'web_url'

    def __init__(self, title, url):
        self.url = url
        super(WebUrlButton, self).__init__(title=title)


class PostbackButton(Button):

    button_type = 'postback'

    def __init__(self, title, payload):
        self.payload = payload
        super(PostbackButton, self).__init__(title=title)
