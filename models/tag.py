

class Tag:

    def __init__(self, name):
        self.name = name
        self.content = None
        self.attributes = {}

    def add_content(self, text):
        self.content = ' '.join(text.split())

    def add_attribute(self, key, value):
        if str(type(value)) == "<class 'str'>":
            if len(value) < 1:
                return
        self.attributes[key] = value

    def get_data(self):
        if len(self.attributes) == 0:
            self.attributes = None
        return {
            'name': self.name,
            'content': self.content,
            'attributes': self.attributes
        }
