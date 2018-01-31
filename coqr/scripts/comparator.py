import argparse
import json

from coqr.comparators.Comparator import Comparator
from coqr.utils.encoder import JSONSerializer
from coqr.utils.file import write_to_file

parser = argparse.ArgumentParser(description='Takes two files and compares processed outputs between them')

# #
parser.add_argument('coq')
parser.add_argument('r')
parser.add_argument('-output')

if __name__ == '__main__':
    options = parser.parse_args()

    comparator = Comparator()
    comparison = comparator.compare_files(options.coq, options.r)

    print("Comparing results from %s and %s" % (options.coq, options.r))
    if options.output:
        write_to_file(options.output, comparison)
    else:
        print(json.dumps(comparison, indent=2, cls=JSONSerializer))
