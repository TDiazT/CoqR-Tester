import sys
import re
import os
import json

reg = re.compile(r'" *{ *([\w:\(\)-.=, \\"\/\%^!|&<;{}\[\]`]*) *} *"')

print()

with open(sys.argv[1]) as file_:
    lines = file_.readlines()

results = []
for line in lines:
    matches = reg.findall(line)
    clean = [re.sub(r'\\', '', result) for result in matches]

    if clean:
        results.append(clean)

results = [line for result in results for line in result]

r_file = os.path.splitext(sys.argv[1])[0] + '.R'

with open(os.path.join(sys.argv[2], r_file), 'w') as file_:
    for line in results:
        line += '\n'
        file_.write(line)
