import argparse
import json
import sys

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

with open(input_) as file_:
    outputs = json.load(file_)

    for output in outputs:
        result = processor.process(output['output'])
        output['clean_output'] = result

with open(sys.argv[2], 'w') as file_:
    json.dump(outputs, file_, indent=2)
