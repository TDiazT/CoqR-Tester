import argparse
import json

from rcoq.comparators.Comparator import compare_files

parser = argparse.ArgumentParser(description='Takes two files and compares processed outputs between them')

# #
parser.add_argument('coq')
parser.add_argument('r')
parser.add_argument('output')


def __read_file(filename):
    with open(filename) as file_:
        return json.load(file_)


def __write_to_file(filename, comparisons):
    with open(filename, 'w') as file_:
        json.dump(comparisons, file_, indent=2)


if __name__ == '__main__':
    options = parser.parse_args()

    compare_files(options.coq, options.r, options.output)
