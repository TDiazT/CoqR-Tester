import argparse
import json
import os
import sys

import time

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


def get_interpreter():
    if os.environ.get('RSCRIPT'):
        return RInterpreter(os.environ.get('RSCRIPT'))
    elif os.environ.get('COQ_INTERP'):
        return CoqInterpreter(os.environ.get('COQ_INTERP'))
    else:
        sys.exit("No valid interpreter set in environment. Define either 'RSCRIPT' or 'COQ_INTERP' variables.")


if __name__ == '__main__':
    options = parser.parse_args()

    interpreter = get_interpreter()
    file_interpreter = FileInterpreter(interpreter)

    print('Interpreting file %s with %s interpreter' % (options.input, interpreter.name))
    current_time = time.time()
    if not options.line:
        reports = file_interpreter.interpret_multiline(options.input)
    else:
        reports = file_interpreter.interpret_line_by_line(options.input)

    print('Done! It took %f' % (time.time() - current_time))
    if options.output:
        print('You may find the results in %s' % options.output)
        write_to_file(options.output, reports)
    else:
        print(json.dumps(reports, indent=2))
