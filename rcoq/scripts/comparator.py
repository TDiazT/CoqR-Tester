import argparse

from rcoq.comparators.Comparator import compare_files
from rcoq.utils.file import write_to_file

parser = argparse.ArgumentParser(description='Takes two files and compares processed outputs between them')

# #
parser.add_argument('coq')
parser.add_argument('r')
parser.add_argument('output')

if __name__ == '__main__':
    options = parser.parse_args()

    comparison = compare_files(options.coq, options.r)
    write_to_file(options.output, comparison)
