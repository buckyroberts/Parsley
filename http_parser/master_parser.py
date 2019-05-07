from urllib.request import Request, urlopen
from http_parser.response_parser import ResponseParser
from http_parser.page_parser import PageParser
from tools.general import *


class MasterParser:

    @staticmethod
    def parse(url, output_dir, output_file):
        '''
        Call the ResponseParser method for parsing and retrieving the headers from the urlopen object retrieved from the URL.
        It then calls the PageParser method for the actual parsing.
        The project can as of now only decode UTF-8 encoding.
        Results are stored in JSON with attributes as url, status, headers and tags.

        :param url: The URL of webpage to be parsed to JSON
        :type url: string

        :param output_dir: Root directory where the JSON is to be stored
        :type output_dir: string

        :param output_file: The name the JSON file is to be given
        :type output_file: string
        '''
        print('Crawling ' + url)
        resp = urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'}))
        resp_bytes = resp.read()
        resp_parser = ResponseParser(resp)
        try:
            page_parser = PageParser(resp_bytes.decode('utf-8'))
        except UnicodeDecodeError:
            return
        json_results = {
            'url': url,
            'status': resp.getcode(),
            'headers': resp_parser.headers,
            'tags': page_parser.all_tags
        }
        write_json(output_dir + '/' + output_file + '.json', json_results)
