import argparse
import os
import sys

from coqr.constants import ReportKeys
from coqr.interpreters.AbstractInterpreter import AbstractInterpreter
from coqr.interpreters.CoqInterpreter import CoqInterpreter
from coqr.interpreters.RInterpreter import RInterpreter
from coqr.utils.file import write_to_file, read_file

parser = argparse.ArgumentParser(description='Run every expression in a file with named interpreter')

parser.add_argument('input')
parser.add_argument('output')


def run(input_, interpreter: AbstractInterpreter, debug=False):
    lines = read_file(input_)
    lines = [line.strip() for line in lines]
    reports = interpreter.interpret_expressions(lines)
    for report in reports:
        report[ReportKeys.FILENAME] = input_

    if debug:
        write_to_file(interpreter.name + '.json', reports)

    return reports


if __name__ == '__main__':
    options = parser.parse_args()

    if os.environ.get('RSCRIPT'):
        interpreter = RInterpreter(os.environ.get('RSCRIPT'))
    elif os.environ.get('COQ_INTERP'):
        interpreter = CoqInterpreter(os.environ.get('COQ_INTERP'))
    else:
        sys.exit("No valid interpreter given")

    run(options.input, options.output, interpreter)
