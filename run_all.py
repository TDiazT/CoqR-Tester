#!/usr/bin/env python3

import argparse
import os
import re
import subprocess

import time

import sys
from requests import HTTPError

import stats
import settings
import logging

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
from messages import *

COQ_DEFAULT_FILE = 'coq.json'

R_DEFAULT_FILE = 'r.json'

parser = argparse.ArgumentParser(
    description='Run given file with R and Coq interpreters, processes outputs and compares')

parser.add_argument('src', help="File to be interpreted")
parser.add_argument('-o', '--output', help="Creates a JSON file with the results in the given path.")
parser.add_argument('-d', '--debug', action='store_true',
                    help="Allows printing debug information in the console output. If the -o option is used, it "
                         "will attempt to create debug files in the same directory given.")
parser.add_argument('-s', '--server', action='store_true', help="Send results to a server. It requires URL and TOKEN "
                                                                "env variables to be defined.")
parser.add_argument('-r', '--recursive', action='store_true',
                    help="Allows interpretation of a directory to be recursive.")
parser.add_argument('-t', '--title', default='', help="Adds a title to the test.")
parser.add_argument('-m', '--message', default='', help="Adds a custom message (description) to the test.")

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)


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
    logger.info(COMPARING_MSG)
    comparator = Comparator()
    return comparator.compare_results(processed_coq, processed_r)


def print_general_stats(reports):
    logger.info("")
    logger.info(GENERAL_STATS_HEADER)
    stats_ = stats.get_general_stats(reports)
    for k, v in stats_.most_common():
        logger.info("%s : %d" % (str(Status(k)), v))


def get_coqr_version():
    COQ_INTERP = os.environ.get("COQ_INTERP")
    if COQ_INTERP:
        git_process = subprocess.Popen(["git", "--git-dir", os.path.join(COQ_INTERP, '.git'),
                                        "rev-parse", "HEAD"], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                       universal_newlines=True)
        (res, err) = git_process.communicate()
        return re.sub(r'\n', '', res)
    else:
        sys.exit("Please define the 'COQ_INTERP' variable.")


def get_cmd_used():
    cmd = sys.argv
    cmd[0] = "./{0:s}".format(os.path.basename(cmd[0]))
    return " ".join(cmd)


if __name__ == '__main__':
    options = parser.parse_args()

    logger.info(interpreting(options.src))
    logger.info(RUNNING_R_INTERPRETER_MSG)
    RSCRIPT = os.environ.get("RSCRIPT")
    if RSCRIPT:
        r_interpreter = RInterpreter(RSCRIPT)
    else:
        sys.exit("Please define the 'RSCRIPT' variable.")
    COQ_INTERP = os.environ.get("COQ_INTERP")
    if COQ_INTERP:
        COQR_INITIAL_STATE = os.environ.get("COQR_INITIAL_STATE")
        if COQR_INITIAL_STATE:
            coqr = CoqInterpreter(COQ_INTERP, COQR_INITIAL_STATE)
        else:
            sys.exit("Please define the 'COQR_INITIAL_STATE' env variable.")
    else:
        sys.exit("Please define the 'COQ_INTERP' variable.")

    delta = time.time()
    if os.path.isfile(options.src):
        r_results = interpret_file(options.src, FileInterpreter(r_interpreter, debug=options.debug))
    else:
        r_results = interpret_directory(options.src, FileInterpreter(r_interpreter, debug=options.debug),
                                        recursive=options.recursive)
    logger.info(finished_in(time.time() - delta))

    logger.info(RUNNING_COQ_INTERPRETER_MSG)

    delta = time.time()
    if os.path.isfile(options.src):
        coq_results = interpret_file(options.src, FileInterpreter(coqr, debug=options.debug))
    else:
        coq_results = interpret_directory(options.src, FileInterpreter(coqr, debug=options.debug),
                                          recursive=options.recursive)

    logger.info(finished_in(time.time() - delta))

    if options.debug:
        if options.output:
            directory = os.path.dirname(options.output)
            write_to_file(os.path.join(directory, R_DEFAULT_FILE), r_results)
            write_to_file(os.path.join(directory, COQ_DEFAULT_FILE), coq_results)
        else:
            logger.info("Debug set but no output directory specified")

    logger.info(processing_output("R"))
    r_process = process_outputs(r_results, ROutputProcessor())
    logger.info(processing_output("Coq"))
    coq_process = process_outputs(coq_results, CoqOutputProcessor())

    if options.debug:
        if options.output:
            directory = os.path.dirname(options.output)
            write_to_file(os.path.join(directory, 'processed-r.json'), r_process)
            write_to_file(os.path.join(directory, 'processed-coq.json'), coq_process)
        else:
            logger.info("Debug set but no output directory specified")

    comparison = compare_processed_outputs(r_process, coq_process)
    (sysname, nodename, release, version, machine) = os.uname()
    cmd = get_cmd_used()
    description = "".join([cmd, '\n\n', options.message])

    final_report = {
        "r_interpreter_version": "3.4.2",
        "coq_interpreter_version": get_coqr_version(),
        "system": sysname,
        "os_node_name": nodename,
        "os_release": release,
        "os_version": version,
        "hardware": machine,
        "title": options.title,
        "description": description,
        "expression_reports": comparison
    }

    if options.output:
        write_to_file(options.output, final_report)

    if options.server:
        URL = os.environ.get("URL")
        TOKEN = os.environ.get("TOKEN")
        if URL:
            logger.info(SENDING_RESULTS)
            try:
                send_reports(final_report, URL, TOKEN)
                logger.info(SENT_SUCCESSFULLY)
            except HTTPError:
                logger.error(ERROR_SENDING)
        else:
            sys.exit("Please define the 'URL' environmental variable")

    if options.output:
        logger.info(processed_finished_with_output(options.output))
    else:
        logger.info(PROCESS_FINISHED_MSG)

    print_general_stats(comparison)
