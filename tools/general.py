import json
import os


def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory


def write_file(file_name, data):
    with open(file_name, 'w') as f:
        f.write(data)


def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results


def write_json(file_name, data):
    with open(file_name, 'w') as f:
        json.dump(data, f)
