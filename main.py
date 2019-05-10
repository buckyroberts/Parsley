import threading
from queue import Queue

from args_parser import parse_args
from http_parser.master_parser import MasterParser
from tools.general import create_dir, file_to_set

args = parse_args()
INPUT_FILE = args.input
OUTPUT_DIR = args.output
NUMBER_OF_THREADS = args.threads

queue = Queue()
create_dir(OUTPUT_DIR)
crawl_count = 0


def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


def work():
    global crawl_count
    while True:
        url = queue.get()
        crawl_count += 1
        MasterParser.parse(url, OUTPUT_DIR, str(crawl_count))
        queue.task_done()


def create_jobs():
    for url in file_to_set(INPUT_FILE):
        queue.put(url)
    queue.join()

create_workers()
create_jobs()
