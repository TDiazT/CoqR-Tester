import json
import sys
import re

input_ = sys.argv[1]

cases = {
    'SUCCESS': re.compile(r'\[\d+\][ \w]+'),
    'ERROR': re.compile(r'Error:*'),
    'NOT_IMPLEMENTED': re.compile(r'Not implemented:'),
    'IMPOSSIBLE': re.compile('Impossible'),
    'NULL': re.compile('\(*NULL\)*')
}

with open(input_) as file_:
    outputs = json.load(file_)

    for output in outputs:

        for case in cases:
            result = cases[case].findall(output['output'])

            if result:
                if case == 'SUCCESS':
                    output['clean_output'] = result
                else:
                    output['clean_output'] = case

with open(sys.argv[2], "w") as file_:
    json.dump(outputs, file_, indent=2)
