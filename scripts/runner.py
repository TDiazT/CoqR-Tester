import sys
import subprocess
import re
import json
import os

filename = sys.argv[2]

with open(filename) as file_:
    a = file_.readlines()

results = []

for i, line in enumerate(a):
    line = line.strip()
    if sys.argv[1] == 'R':
        out = subprocess.run(['rscript', '-e', line], universal_newlines=True, stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT).stdout
        interp = 'R'
    else:
        coq_interp = os.environ['COQ_INTERP']

        p1 = subprocess.Popen(['echo', line], stdout=subprocess.PIPE)
        p2 = subprocess.Popen(['make', 'run', '-s', '-C', coq_interp], stdin=p1.stdout, stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT, universal_newlines=True)
        p1.stdout.close()
        out = p2.communicate()[0]
        interp = "Coq"

    result = {
        "output": out,
        "expression": line,
        "line": i + 1,
        "interpreter": interp
    }

    results.append(result)

with open(sys.argv[3], "w") as file_:
    json.dump(results, file_, indent=2)
