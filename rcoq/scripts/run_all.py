import argparse
import os
import time

import rcoq.comparators.Comparator
from rcoq import settings
from rcoq.constants.Status import Status
from rcoq.interpreters.CoqInterpreter import CoqInterpreter
from rcoq.interpreters.RInterpreter import RInterpreter
from rcoq.processors.CoqOutputProcessor import CoqOutputProcessor
from rcoq.processors.ROutputProcessor import ROutputProcessor
from rcoq.scripts import runner, cleaner
from rcoq.stats import stats
from rcoq.utils.file import write_to_file

parser = argparse.ArgumentParser(
    description='Run given file with R and Coq interpreters, processes outputs and compares')

parser.add_argument('rsrc')
parser.add_argument('output')
parser.add_argument('-rout', '--rout', default='r.json')
parser.add_argument('-coqout', '--coqout', default='coq.json')


def interpret_file(src, rout, coqout):
    delta = time.time()
    print("Running R interpreter...")
    runner.run(src, rout, RInterpreter(settings.RSCRIPT))
    print("Finished in %f seconds" % (time.time() - delta))
    delta = time.time()
    print("Running Coq interpreter...")
    runner.run(src, coqout, CoqInterpreter(settings.COQ_INTERP))
    print("Finished in %f seconds" % (time.time() - delta))


def process_outputs(rout, processed_r, coqout, processed_coq):
    print("Processing R output")
    cleaner.process_file(rout, processed_r, ROutputProcessor())
    print("Processing Coq output")
    cleaner.process_file(coqout, processed_coq, CoqOutputProcessor())


def compare_processed_outputs(processed_r, processed_coq):
    print("Comparing")
    return rcoq.comparators.Comparator.compare_files(processed_coq, processed_r)


def print_general_stats():
    print("")
    print("---------- GENERAL STATS ----------")
    stats_ = stats.get_general_stats(options.output)
    for k, v in stats_.most_common():
        print("%s : %d" % (str(Status(k)), v))


if __name__ == '__main__':
    options = parser.parse_args()

    directory = os.path.dirname(options.output)
    rout = os.path.join(directory, options.rout)
    coqout = os.path.join(directory, options.coqout)

    interpret_file(options.rsrc, rout, coqout)

    processed_r = os.path.join(directory, "processed-" + options.rout)
    processed_coq = os.path.join(directory, "processed-" + options.coqout)
    process_outputs(rout, processed_r, coqout, processed_coq)

    comparison = compare_processed_outputs(processed_r, processed_coq)
    write_to_file(options.output, comparison)

    print("Done, you may find the results in %s" % options.output)

    print_general_stats()
