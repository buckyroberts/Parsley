

class ResponseParser:

    def __init__(self, response):
        self.response = response
        self.headers = self.parse()

    def parse(self):
        '''
        Return a list of dictionaries comprising of all the HTML tags in the webpage.
        The dictionary has the keys: attributes, content and name of the tags.
        The attributes would be of the tags such as content and name whereas as the name listed above is the name of the tag.

        param html_string: the HTML data of the requested webpage
        type html_string: string

        returns: list of dictionaries with all the tags
        '''
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
