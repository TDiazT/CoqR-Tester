import glob
import os
import re
import sys

reg = re.compile(r'" *{ *(.*) *} *"')


cwd = os.getcwd()
os.chdir(sys.argv[1])

for filename in glob.glob("*.java"):
    with open(filename) as file_:
        lines = file_.readlines()

    results = []
    for line in lines:
        matches = reg.findall(line)
        clean = [re.sub(r'\\', '', result) for result in matches]

        if clean:
            results.append(clean)

    results = [line for result in results for line in result]

    r_file = os.path.splitext(filename)[0] + '.R'

    dest = os.path.join(cwd, sys.argv[2], r_file)

    with open(dest, 'w') as file_:
        for line in results:
            line += '\n'
            file_.write(line)
