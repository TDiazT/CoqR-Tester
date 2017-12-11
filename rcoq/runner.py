import argparse
import os
import re
import sys
import time

from rcoq.constants import ReportKeys
from rcoq.interpreters.CoqInterpreter import CoqInterpreter
from rcoq.interpreters.RInterpreter import RInterpreter
from rcoq.utils import exp_extract
from rcoq.utils.file import write_to_file, read_file

parser = argparse.ArgumentParser(description='Run every expression in a file with named interpreter')

# #
parser.add_argument('input')
parser.add_argument('output')

TOKEN = "TOKEN"


def run(input_, output_, interpreter):
    lines = read_file(input_)
    lines = [line.strip() for line in lines]
    reports = run_interpreter(lines, interpreter)

    write_to_file(output_, reports)


def __pre_process_expression(expression):
    expressions = exp_extract.extract_expressions(expression)
    results = []
    for exp in expressions:
        results.append("(%s)" % exp)

    expressions = '; "TOKEN" ;'.join(results)

    return expressions


def __post_process_output(out):
    return re.split(r'\[\d\]\s*"TOKEN"\s*', out)


def run_interpreter(expressions, interpreter):
    results = []
    for i, expression in enumerate(filter(None, expressions)):
        processed_expression = __pre_process_expression(expression)
        exec_time = time.time()
        out = interpreter.interpret(processed_expression)
        exec_time = time.time() - exec_time

        processed_out = __post_process_output(out)

        # TODO: Extract method
        result = {
            ReportKeys.OUTPUT: processed_out,
            ReportKeys.EXPRESSION: expression,
            ReportKeys.EXEC_TIME: exec_time,
            ReportKeys.LINE: i + 1,
            ReportKeys.INTERPRETER: interpreter.name
        }

        results.append(result)

    return results


if __name__ == '__main__':
    options = parser.parse_args()

    if os.environ.get('RSCRIPT'):
        interpreter = RInterpreter(os.environ.get('RSCRIPT'))
    elif os.environ.get('COQ_INTERP'):
        interpreter = CoqInterpreter(os.environ.get('COQ_INTERP'))
    else:
        sys.exit("No valid interpreter given")

    run(options.input, options.output, interpreter)
