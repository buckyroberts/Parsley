

class ResponseParser:

    def __init__(self, response):
        self.response = response
        self.headers = self.parse()

    def parse(self):
        results = {}
        header_info = str(self.response.info()).split('\n')
        for item in header_info:
            row = item.split(':', 1)
            try:
                key = ' '.join(row[0].split())
                value = ' '.join(row[1].split())
                results[key] = value
            except IndexError:
                pass
        return results
