import argparse
import os
from rcoq import settings, runner, cleaner, comparator
from rcoq.interpreters.CoqInterpreter import CoqInterpreter

from rcoq.interpreters.RInterpreter import RInterpreter
from rcoq.processors.CoqOutputProcessor import CoqOutputProcessor
from rcoq.processors.ROutputProcessor import ROutputProcessor

parser = argparse.ArgumentParser(
    description='Run given file with R and Coq interpreters, processes outputs and compares')

parser.add_argument('rsrc')
parser.add_argument('output')
parser.add_argument('-rout', '--rout', default='r.json')
parser.add_argument('-coqout', '--coqout', default='coq.json')

if __name__ == '__main__':
    options = parser.parse_args()

    print("Running R interpreter")
    runner.run(options.rsrc, options.rout, RInterpreter(settings.RSCRIPT))

    print("Running Coq interpreter")
    runner.run(options.rsrc, options.coqout, CoqInterpreter(settings.COQ_INTERP))

    directory = os.path.dirname(options.output)
    processed_r = os.path.join(directory, "processed-" + options.rout)
    processed_coq = os.path.join(directory, "processed-" + options.coqout)

    print("Processing R output")
    cleaner.process_file(options.rout, processed_r, ROutputProcessor())
    print("Processing Coq output")
    cleaner.process_file(options.rout, processed_coq, CoqOutputProcessor())

    print("Comparing")
    comparator.compare_files(processed_coq, processed_r, options.output)

    print("Done, you may find the results in %s" % options.output)
