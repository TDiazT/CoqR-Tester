import argparse

from rcoq.comparators.Comparator import compare_files

parser = argparse.ArgumentParser(description='Takes two files and compares processed outputs between them')

# #
parser.add_argument('coq')
parser.add_argument('r')
parser.add_argument('output')

if __name__ == '__main__':
    options = parser.parse_args()

    compare_files(options.coq, options.r, options.output)
