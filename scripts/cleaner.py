import json
import sys
import re

input_ = sys.argv[1]

cases = {
    'SUCCESS': re.compile(r'\[\d+\][ \w]+'),
    'ERROR': re.compile(r'Error:*'),
    'NOT_IMPLEMENTED': re.compile(r'Not implemented:'),
    'IMPOSSIBLE': re.compile(r'Impossible'),
    'NULL': re.compile(r'\(*NULL\)*'),
    'FUNCTION': re.compile(r'\(closure\)|function \(\w*\)'),
    'INVISIBLE': re.compile(r'^(?![\s\S])')
}

with open(input_) as file_:
    outputs = json.load(file_)

    for output in outputs:
        result = []
        for case in cases:
            matches = cases[case].findall(output['output'])

            if matches:
                if case == 'SUCCESS':
                    result.append(matches)
                else:
                    result.append(case)

        if not result:
            result.append("UNKNOWN")

        output['clean_output'] = result

with open(sys.argv[2], "w") as file_:
    json.dump(outputs, file_, indent=2)
