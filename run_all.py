#!/usr/bin/env python3

import argparse
import os
import time

from requests import HTTPError

import stats
import settings

from coqr.comparators.Comparator import Comparator
from coqr.constants.Status import Status
from coqr.interpreters.CoqInterpreter import CoqInterpreter
from coqr.interpreters.FileInterpreter import FileInterpreter
from coqr.interpreters.RInterpreter import RInterpreter
from coqr.network.calls import send_reports
from coqr.processors.AbstractOutputProcessor import AbstractOutputProcessor
from coqr.processors.CoqOutputProcessor import CoqOutputProcessor
from coqr.processors.ROutputProcessor import ROutputProcessor
from coqr.utils.file import write_to_file

COQ_DEFAULT_FILE = 'coq.json'

R_DEFAULT_FILE = 'r.json'

parser = argparse.ArgumentParser(
    description='Run given file with R and Coq interpreters, processes outputs and compares')

parser.add_argument('src')
parser.add_argument('-o', '--output')
parser.add_argument('--debug', action='store_true')
parser.add_argument('-s', '--server', action='store_true')
parser.add_argument('-r', '--recursive', action='store_true')
parser.add_argument('-a', '--alias', default='')


def interpret_file(src, interpreter, debug=False, out=None):
    reports = interpreter.interpret_file(src)

    if debug:
        write_to_file(out, reports)

    return reports


def interpret_directory(src, interpreter: FileInterpreter, recursive=False, debug=False, out=None):
    reports = interpreter.interpret_directory(src, recursive=recursive)

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
    return comparator.compare_results(processed_coq, processed_r)


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
    print("Interpreting tests in %s" % options.src)
    print("Running R interpreter...")
    if os.path.isfile(options.src):
        r_results = interpret_file(options.src, FileInterpreter(RInterpreter(os.environ.get("RSCRIPT"))),
                                   debug=options.debug,
                                   out=os.path.join(directory, R_DEFAULT_FILE))
    else:
        r_results = interpret_directory(options.src, FileInterpreter(RInterpreter(os.environ.get("RSCRIPT"))),
                                        debug=debug,
                                        out=os.path.join(directory, R_DEFAULT_FILE), recursive=options.recursive)
    print("Finished in %f seconds" % (time.time() - delta))
    delta = time.time()
    print("Running Coq interpreter...")
    if os.path.isfile(options.src):
        coq_results = interpret_file(options.src, FileInterpreter(CoqInterpreter(os.environ.get("COQ_INTERP"))),
                                     debug=options.debug, out=os.path.join(directory, COQ_DEFAULT_FILE))
    else:
        coq_results = interpret_directory(options.src, FileInterpreter(CoqInterpreter(os.environ.get("COQ_INTERP"))),
                                          debug=debug,
                                          out=os.path.join(directory, COQ_DEFAULT_FILE), recursive=options.recursive)
    print("Finished in %f seconds" % (time.time() - delta))

    print("Processing R output")
    r_process = process_outputs(r_results, ROutputProcessor(), debug, os.path.join(directory, 'processed-r.json'))
    print("Processing Coq output")
    coq_process = process_outputs(coq_results, CoqOutputProcessor(), debug,
                                  os.path.join(directory, 'processed-coq.json'))

    comparison = compare_processed_outputs(r_process, coq_process)
    (sysname, nodename, release, version, machine) = os.uname()
    final_report = {
        "r_interpreter_version": "3.4.2",
        "coq_interpreter_version": '0.1',
        "system": sysname,
        "os_node_name": nodename,
        "os_release": release,
        "os_version": version,
        "hardware": machine,
        "alias": options.alias,
        "expression_reports": comparison
    }

    if options.output:
        write_to_file(options.output, final_report)

    if options.server:
        print('Sending results to server')
        try:
            send_reports(final_report, os.environ.get("URL"), os.environ.get("TOKEN"))
            print('Sent successfully')
        except HTTPError:
            print('There was an error sending the report to server')

    print("Done, you may find the results in %s" % options.output)

    print_general_stats()
