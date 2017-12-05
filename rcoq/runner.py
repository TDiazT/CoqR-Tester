import sys
import subprocess
import re
import json
import os
import time
import argparse

parser = argparse.ArgumentParser(description='Run every expression in a file with named interpreter')

# #
parser.add_argument('input')
parser.add_argument('output')

options = parser.parse_args()

with open(options.input) as file_:
    lines = file_.readlines()

results = []

lines = [line.strip() for line in lines]

for i, line in enumerate(filter(None, lines)):
    exec_time = time.time()
    if os.environ.get('RSCRIPT'):
        r_interp = os.environ.get('RSCRIPT')
        out = subprocess.run([r_interp, '-e', line], universal_newlines=True, stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT).stdout
        interp = 'R'
    elif os.environ.get('COQ_INTERP'):
        coq_interp = os.environ['COQ_INTERP']

        p1 = subprocess.Popen(['echo', line], stdout=subprocess.PIPE)
        p2 = subprocess.Popen(['make', 'run', '-s', '-C', coq_interp], stdin=p1.stdout, stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT, universal_newlines=True)
        p1.stdout.close()
        out = p2.communicate()[0]
        interp = "Coq"

    exec_time = time.time() - exec_time

    result = {
        "output": out,
        "expression": line,
        "execution_time": exec_time,
        "line": i + 1,
        "interpreter": interp
    }

    results.append(result)

with open(options.output, "w") as file_:
    json.dump(results, file_, indent=2)
