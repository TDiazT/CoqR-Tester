import sys
import subprocess
import re
import json
import os
import time

filename = sys.argv[2]

with open(filename) as file_:
    lines = file_.readlines()

results = []

lines = [line.strip() for line in lines]

for i, line in enumerate(filter(None, lines)):
    exec_time = time.time()
    if os.environ.get('RSCRIPT'):
        out = subprocess.run(['rscript', '-e', line], universal_newlines=True, stdout=subprocess.PIPE,
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

with open(sys.argv[3], "w") as file_:
    json.dump(results, file_, indent=2)
