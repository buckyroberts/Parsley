from bs4 import BeautifulSoup
from models.tag import Tag


class PageParser:

    def __init__(self, html_string):
        self.soup = BeautifulSoup(html_string, 'html5lib')
        self.html = self.soup.find('html')
        self.all_tags = self.parse()

    def parse(self):
        '''
        This function returns a dictionary with the response headers of the page along with other meta-information.
        The utility of this function is that urlopen.info() returns these information as a mime tools.Message instance which isn’t as easy to use an dictionary.
        Each item from an .info() call is split and added to a dictionary as a key value pair

        :param response: The response object from a urlopen call to the URL of the webpage
        :type response: HTTPresponse object

        :returns a dictionary with response headers and other meta-information depending on the webpage.
        '''
        results = []
        for x, tag in enumerate(self.html.descendants):

            if str(type(tag)) == "<class 'bs4.element.Tag'>":

                #look for global.document.metadata
                if tag.name == 'script':
                    if tag.string:
                        position = tag.string.find('global.document.metadata=')
                        if position == -1:
                            continue
                        else:
                            a = 'global.document.metadata='
                            t = Tag('global.document.metadata')

                            s = tag.string[position + len(a):]
                            s = s[:s.find('\n')-1]

                            t.add_content(s)

                            results.append(t.get_data())


                # Find tags with no children (base tags)
                if tag.contents:
                    if sum(1 for _ in tag.descendants) == 1:
                        t = Tag(tag.name.lower())

                        # Because it might be None (<i class="fa fa-icon"></i>)
                        if tag.string:
                            t.add_content(tag.string)

                        if tag.attrs:
                            for a in tag.attrs:
                                t.add_attribute(a, tag[a])

                        results.append(t.get_data())

                # Self enclosed tags (hr, meta, img, etc...)
                else:
                    t = Tag(tag.name.lower())

                    if tag.attrs:
                        for a in tag.attrs:
                            t.add_attribute(a, tag[a])

                    results.append(t.get_data())

        return results
