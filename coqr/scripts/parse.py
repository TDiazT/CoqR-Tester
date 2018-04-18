import sys

from coqr.parsing.parse import parse_file


def main(argv):
    [print(exp) for exp in parse_file(argv[1])]


if __name__ == '__main__':
    main(sys.argv)
