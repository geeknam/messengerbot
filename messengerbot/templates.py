

class GenericTemplate(object):

    template_type = 'generic'

    def __init__(self, elements):
        if not isinstance(elements, list):
            raise ValueError(
                'elements should be a list of Element'
            )
        self._elements = elements

    @property
    def elements(self):
        if len(self._elements) > 10:
            raise ValueError('Too many elements in the template')
        return self._elements

    def to_dict(self):
        return {
            'template_type': self.template_type,
            'elements': [
                element.to_dict() for element in self.elements
            ]
        }


class ButtonTemplate(object):

    template_type = 'button'

    def __init__(self, text, buttons):
        self.text = text

        if not isinstance(buttons, list):
            raise ValueError(
                'buttons should be a list of Button'
            )
        self.buttons = buttons

    def to_dict(self):
        return {
            'template_type': self.template_type,
            'text': self.text,
            'buttons': [
                button.to_dict() for button in self.buttons
            ]
        }
