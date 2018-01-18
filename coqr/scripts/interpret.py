import argparse
import os
import sys

from coqr.constants import ReportKeys
from coqr.interpreters.AbstractInterpreter import AbstractInterpreter
from coqr.interpreters.CoqInterpreter import CoqInterpreter
from coqr.interpreters.RInterpreter import RInterpreter
from coqr.utils.file import write_to_file, read_file
from coqr.parsing import parse

parser = argparse.ArgumentParser(description='Run every expression in a file with named interpreter')

parser.add_argument('input')
parser.add_argument('-m', action='store_false')


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
        sys.exit("No valid interpreter set in environment. Define either 'RSCRIPT' or 'COQ_INTERP' variables.")

    if options.m:
        expressions = parse.parse_file(options.input)
        results = interpreter.interpret_multiple(expressions)
        print(results)
    else:
        results = run(options.input, interpreter)
        print(results)
        # print(expressions)
        # print(len(expressions))
    # reports = run(options.input, interpreter)
    # print(reports)
