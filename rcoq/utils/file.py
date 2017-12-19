import json


def read_json_file(filename):
    with open(filename) as file_:
        return json.load(file_)


def write_to_file(filename, content):
    with open(filename, 'w') as file_:
        json.dump(content, file_, indent=2)


def read_file(filename):
    with open(filename) as file_:
        return file_.readlines()