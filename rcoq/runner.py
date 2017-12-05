import argparse
import json
import os
import subprocess
import time
import sys

parser = argparse.ArgumentParser(description='Run every expression in a file with named interpreter')

# #
parser.add_argument('input')
parser.add_argument('output')


def read_file(filename):
    with open(filename) as file_:
        return file_.readlines()


def run_interpreter(expressions):
    results = []
    for i, expression in enumerate(filter(None, expressions)):
        exec_time = time.time()
        if os.environ.get('RSCRIPT'):
            r_interp = os.environ.get('RSCRIPT')
            out = subprocess.run([r_interp, '-e', expression], universal_newlines=True, stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT).stdout
            interp = 'R'
        elif os.environ.get('COQ_INTERP'):
            coq_interp = os.environ['COQ_INTERP']

            p1 = subprocess.Popen(['echo', expression], stdout=subprocess.PIPE)
            p2 = subprocess.Popen(['make', 'run', '-s', '-C', coq_interp], stdin=p1.stdout, stdout=subprocess.PIPE,
                                  stderr=subprocess.STDOUT, universal_newlines=True)
            p1.stdout.close()
            out = p2.communicate()[0]
            interp = "Coq"
        else:
            sys.exit("No valid interpreter given")

        exec_time = time.time() - exec_time

        result = {
            "output": out,
            "expression": expression,
            "execution_time": exec_time,
            "line": i + 1,
            "interpreter": interp
        }

        results.append(result)

    return results


def write_to_file(filename, results):
    with open(filename, "w") as file_:
        json.dump(results, file_, indent=2)


if __name__ == '__main__':
    options = parser.parse_args()

    lines = read_file(options.input)
    lines = [line.strip() for line in lines]
    reports = run_interpreter(lines)

    write_to_file(options.output, reports)
