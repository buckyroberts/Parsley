from urllib.parse import urlparse


class Domain:

    def __init__(self, url):
        self.url = url
        self.domain = self.get_domain()
        self.sub_domain = self.get_sub_domain()

    def get_domain(self):
        results = self.get_sub_domain().split('.')
        try:
            return results[-2] + '.' + results[-1]
        except IndexError:
            return False

    def get_sub_domain(self):
        return urlparse(self.url).netloc
