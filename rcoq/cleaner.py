import argparse
import sys

from rcoq.constants import ReportKeys
from rcoq.processors.CoqOutputProcessor import CoqOutputProcessor
from rcoq.processors.ROutputProcessor import ROutputProcessor
from rcoq.utils.file import read_json_file, write_to_file

parser = argparse.ArgumentParser(description='Processes output and returns a new standard one')

# #
parser.add_argument('interp')
parser.add_argument('input')
parser.add_argument('output')


def process_file(input_, output_, processor):
    previous_reports = read_json_file(input_)
    new_reports = process_reports(previous_reports, processor)

    write_to_file(output_, new_reports)


def process_reports(rs, processor):
    for report in rs:
        result = []

        for out in report[ReportKeys.OUTPUT]:
            result.append(processor.process(out))

        report[ReportKeys.PROCESSED_OUT] = result

    return rs


if __name__ == '__main__':
    options = parser.parse_args()

    if options.interp == 'R':
        processor = ROutputProcessor()
    elif options.interp == 'Coq':
        processor = CoqOutputProcessor()
    else:
        sys.exit('"%s" is not a valid interpreter (either "R" or "Coq")' % options.interp)

    process_file(options.input, options.output, processor)
