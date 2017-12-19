import argparse
import os
import sys

from rcoq.interpreters.CoqInterpreter import CoqInterpreter
from rcoq.interpreters.RInterpreter import RInterpreter
from rcoq.utils.file import write_to_file, read_file

parser = argparse.ArgumentParser(description='Run every expression in a file with named interpreter')

parser.add_argument('input')
parser.add_argument('output')


def run(input_, output_, interpreter):
    lines = read_file(input_)
    lines = [line.strip() for line in lines]
    reports = interpreter.interpret_expressions(lines)

    write_to_file(output_, reports)


if __name__ == '__main__':
    options = parser.parse_args()

    if os.environ.get('RSCRIPT'):
        interpreter = RInterpreter(os.environ.get('RSCRIPT'))
    elif os.environ.get('COQ_INTERP'):
        interpreter = CoqInterpreter(os.environ.get('COQ_INTERP'))
    else:
        sys.exit("No valid interpreter given")

    run(options.input, options.output, interpreter)
