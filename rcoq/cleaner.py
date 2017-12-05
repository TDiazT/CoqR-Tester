import argparse
import json
import sys
import re

from rcoq.processors.CoqOutputProcessor import CoqOutputProcessor
from rcoq.processors.ROutputProcessor import ROutputProcessor

parser = argparse.ArgumentParser(description='Processes output and returns a new standard one')

# #
parser.add_argument('interp')
parser.add_argument('input')
parser.add_argument('output')

options = parser.parse_args()

if options.interp == 'R':
    processor = ROutputProcessor()
elif options.interp == 'Coq':
    processor = CoqOutputProcessor()
else:
    sys.exit('"%s" is not a valid interpreter (either "R" or "Coq")' % options.interp)

input_ = options.input
output_ = options.output

token_regex = re.compile(r'\[\d\]\s"TOKEN"\s')


with open(input_) as file_:
    reports = json.load(file_)

for report in reports:
    stripped = token_regex.split(report['output'])

    result = []

    for out in stripped:
        result.append(processor.process(out))

    report['processed_output'] = result

with open(output_, 'w') as file_:
    json.dump(reports, file_, indent=2)
