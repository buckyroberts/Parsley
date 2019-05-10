import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Gets a list of URLs and converts the HTML to JSON.')

    parser.add_argument('--input', default='sample-links.txt', help='Input file')
    parser.add_argument('--output', default='data', help='Output directory')
    parser.add_argument('--threads', type=int, default=8, help='Number of threads')

    args = parser.parse_args()
    return args
