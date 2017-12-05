import argparse
import json
import os
import subprocess
import time
import sys

from rcoq.runners.RRunner import RRunner
from rcoq.runners.CoqRunner import CoqRunner

parser = argparse.ArgumentParser(description='Run every expression in a file with named interpreter')

# #
parser.add_argument('input')
parser.add_argument('output')


def run(input_, output_, runner):
    lines = __read_file(input_)
    lines = [line.strip() for line in lines]
    reports = run_interpreter(lines, runner)

    __write_to_file(output_, reports)


def __read_file(filename):
    with open(filename) as file_:
        return file_.readlines()


def run_interpreter(expressions, runner):
    results = []
    for i, expression in enumerate(filter(None, expressions)):
        exec_time = time.time()
        out = runner.run(expression)
        exec_time = time.time() - exec_time

        result = {
            "output": out,
            "expression": expression,
            "execution_time": exec_time,
            "line": i + 1,
            "interpreter": runner.interpreter
        }

        results.append(result)

    return results


def __write_to_file(filename, results):
    with open(filename, "w") as file_:
        json.dump(results, file_, indent=2)


if __name__ == '__main__':
    options = parser.parse_args()

    if os.environ.get('RSCRIPT'):
        runner = RRunner(os.environ.get('RSCRIPT'))
    elif os.environ.get('COQ_INTERP'):
        runner = CoqRunner(os.environ.get('COQ_INTERP'))
    else:
        sys.exit("No valid interpreter given")

    run(options.input, options.output, runner)
