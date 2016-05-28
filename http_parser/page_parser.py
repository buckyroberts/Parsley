from bs4 import BeautifulSoup
from models.tag import Tag


class PageParser:

    def __init__(self, html_string):
        self.soup = BeautifulSoup(html_string, 'html5lib')
        self.html = self.soup.find('html')
        self.all_tags = self.parse()

    def parse(self):
        results = []
        for x, tag in enumerate(self.html.descendants):

            if str(type(tag)) == "<class 'bs4.element.Tag'>":

                if tag.name == 'script':
                    continue

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
