import argparse
import json
import os
import sys

from coqr.constants import ReportKeys
from coqr.interpreters.AbstractInterpreter import AbstractInterpreter
from coqr.interpreters.CoqInterpreter import CoqInterpreter
from coqr.interpreters.FileInterpreter import FileInterpreter
from coqr.interpreters.RInterpreter import RInterpreter
from coqr.utils import reports
from coqr.utils.file import write_to_file, read_file
from coqr.parsing import parse

parser = argparse.ArgumentParser(description='Run every expression in a file with named interpreter')

parser.add_argument('input')
parser.add_argument('-output')
parser.add_argument('--line', action='store_true')


def run(input_, interpreter: AbstractInterpreter, debug=False):
    lines = read_file(input_)
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

    file_interpreter = FileInterpreter(interpreter)
    print('Interpreting file %s ...')
    if not options.line:
        reports = file_interpreter.interpret_multiline(options.input)
        if options.output:
            print('You may find the results in %s' % options.output)
            write_to_file(options.output, reports)
        else:
            print(json.dumps(reports, indent=2))
    else:
        reports = file_interpreter.interpret_line_by_line(options.input)

        if options.output:
            print('You may find the results in %s' % options.output)
            write_to_file(options.output, reports)
        else:
            print(json.dumps(reports, indent=2))