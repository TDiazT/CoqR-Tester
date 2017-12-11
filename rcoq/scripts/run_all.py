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

parser = argparse.ArgumentParser(
    description='Run given file with R and Coq interpreters, processes outputs and compares')

parser.add_argument('rsrc')
parser.add_argument('output')
parser.add_argument('-rout', '--rout', default='r.json')
parser.add_argument('-coqout', '--coqout', default='coq.json')

if __name__ == '__main__':
    options = parser.parse_args()

    directory = os.path.dirname(options.output)
    rout = os.path.join(directory, options.rout)
    coqout = os.path.join(directory, options.coqout)

    delta = time.time()
    print("Running R interpreter...")
    runner.run(options.rsrc, rout, RInterpreter(settings.RSCRIPT))
    print("Finished in %f seconds" % (time.time() - delta))
    delta = time.time()
    print("Running Coq interpreter...")
    runner.run(options.rsrc, coqout, CoqInterpreter(settings.COQ_INTERP))
    print("Finished in %f seconds" % (time.time() - delta))

    processed_r = os.path.join(directory, "processed-" + options.rout)
    processed_coq = os.path.join(directory, "processed-" + options.coqout)

    print("Processing R output")
    cleaner.process_file(rout, processed_r, ROutputProcessor())
    print("Processing Coq output")
    cleaner.process_file(coqout, processed_coq, CoqOutputProcessor())

    print("Comparing")
    rcoq.comparators.Comparator.compare_files(processed_coq, processed_r, options.output)

    print("Done, you may find the results in %s" % options.output)

    print("")
    print("---------- GENERAL STATS ----------")
    stats = stats.get_general_stats(options.output)
    for k, v in stats.most_common():
        print("%s : %d" % (str(Status(k)), v))
