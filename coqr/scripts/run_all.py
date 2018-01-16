import argparse
import os
import time

from coqr import settings
from coqr.comparators.Comparator import Comparator
from coqr.constants import ReportKeys
from coqr.constants.Status import Status
from coqr.interpreters.CoqInterpreter import CoqInterpreter
from coqr.interpreters.RInterpreter import RInterpreter
from coqr.processors.AbstractOutputProcessor import AbstractOutputProcessor
from coqr.processors.CoqOutputProcessor import CoqOutputProcessor
from coqr.processors.ROutputProcessor import ROutputProcessor
from coqr.stats import stats
from coqr.utils.file import write_to_file, read_file

parser = argparse.ArgumentParser(
    description='Run given file with R and Coq interpreters, processes outputs and compares')

parser.add_argument('src')
parser.add_argument('output')
parser.add_argument('--debug', action='store_true')


def interpret_file(src, interpreter, debug=False, out=None):
    lines = read_file(src)
    lines = [line.strip() for line in lines]
    reports = interpreter.interpret_expressions(lines)

    for report in reports:
        report[ReportKeys.FILENAME] = src

    if debug:
        write_to_file(out, reports)

    return reports


def process_outputs(output, processor: AbstractOutputProcessor, debug=False, out=None):
    processed = processor.process_reports(output)

    if debug:
        write_to_file(out, processed)

    return processed


def compare_processed_outputs(processed_r, processed_coq):
    print("Comparing")
    comparator = Comparator()
    return comparator.compare_reports(processed_coq, processed_r)


def print_general_stats():
    print("")
    print("---------- GENERAL STATS ----------")
    stats_ = stats.get_general_stats(options.output)
    for k, v in stats_.most_common():
        print("%s : %d" % (str(Status(k)), v))


if __name__ == '__main__':
    options = parser.parse_args()

    directory = os.path.dirname(options.output)
    debug = options.debug

    delta = time.time()
    print("Interpreting %s file" % options.src)
    print("Running R interpreter...")
    r_results = interpret_file(options.src, RInterpreter(settings.RSCRIPT), debug, os.path.join(directory, 'r.json'))
    print("Finished in %f seconds" % (time.time() - delta))
    delta = time.time()
    print("Running Coq interpreter...")
    coq_results = interpret_file(options.src, CoqInterpreter(settings.COQ_INTERP), debug,
                                 os.path.join(directory, 'coq.json'))
    print("Finished in %f seconds" % (time.time() - delta))

    print("Processing R output")
    r_process = process_outputs(r_results, ROutputProcessor(), debug, os.path.join(directory, 'processed-r.json'))
    print("Processing Coq output")
    coq_process = process_outputs(coq_results, CoqOutputProcessor(), debug, os.path.join(directory, 'processed-coq.json'))

    comparison = compare_processed_outputs(r_process, coq_process)
    write_to_file(options.output, comparison)

    print("Done, you may find the results in %s" % options.output)

    print_general_stats()
