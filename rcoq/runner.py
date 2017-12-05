import argparse
import json
import os
import subprocess
import time
import sys

from rcoq.interpreters.RInterpreter import RInterpreter
from rcoq.interpreters.CoqInterpreter import CoqInterpreter

parser = argparse.ArgumentParser(description='Run every expression in a file with named interpreter')

# #
parser.add_argument('input')
parser.add_argument('output')


def run(input_, output_, interpreter):
    lines = __read_file(input_)
    lines = [line.strip() for line in lines]
    reports = run_interpreter(lines, interpreter)

    __write_to_file(output_, reports)


def __read_file(filename):
    with open(filename) as file_:
        return file_.readlines()


def run_interpreter(expressions, interpreter):
    results = []
    for i, expression in enumerate(filter(None, expressions)):
        exec_time = time.time()
        out = interpreter.interpret(expression)
        exec_time = time.time() - exec_time

        result = {
            "output": out,
            "expression": expression,
            "execution_time": exec_time,
            "line": i + 1,
            "interpreter": interpreter.name
        }

        results.append(result)

    return results


def __write_to_file(filename, results):
    with open(filename, "w") as file_:
        json.dump(results, file_, indent=2)


if __name__ == '__main__':
    options = parser.parse_args()

    if os.environ.get('RSCRIPT'):
        interpreter = RInterpreter(os.environ.get('RSCRIPT'))
    elif os.environ.get('COQ_INTERP'):
        interpreter = CoqInterpreter(os.environ.get('COQ_INTERP'))
    else:
        sys.exit("No valid interpreter given")

    run(options.input, options.output, interpreter)
