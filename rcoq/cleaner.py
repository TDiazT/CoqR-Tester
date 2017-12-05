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

token_regex = re.compile(r'\[\d\]\s"TOKEN"\s')


def process_file(input_, output_, processor):
    previous_reports = __read_file(input_)
    new_reports = process_reports(previous_reports, processor)

    __write_to_file(output_, new_reports)


def process_reports(rs, processor):
    for report in rs:
        stripped = token_regex.split(report['output'])

        result = []

        for out in stripped:
            result.append(processor.process(out))

        report['processed_output'] = result

    return rs


def __read_file(filename):
    with open(filename) as file_:
        return json.load(file_)


def __write_to_file(filename, processed_reports):
    with open(filename, 'w') as file_:
        json.dump(processed_reports, file_, indent=2)


if __name__ == '__main__':
    options = parser.parse_args()

    if options.interp == 'R':
        processor = ROutputProcessor()
    elif options.interp == 'Coq':
        processor = CoqOutputProcessor()
    else:
        sys.exit('"%s" is not a valid interpreter (either "R" or "Coq")' % options.interp)

    process_file(options.input, options.output, processor)
