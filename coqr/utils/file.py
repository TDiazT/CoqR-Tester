import json
from typing import List


def read_json_file(filename):
    with open(filename) as file_:
        return json.load(file_)


def obj_dict(obj):
    return obj.__dict__


def write_to_file(filename, content):
    with open(filename, 'w') as file_:
        json.dump(content, file_, indent=2, default=obj_dict)


def read_file(filename: str) -> List[str]:
    """
    Reads a file and returns a list with its lines
    :param filename: File to read
    :return: List of lines
    """
    with open(filename) as file_:
        return file_.readlines()
