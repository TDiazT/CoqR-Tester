import argparse
import json
from collections import Counter

from rcoq.constants import ReportKeys
from rcoq.constants.Status import Status
from rcoq.constants.Cases import Cases
from rcoq.utils import exp_extract

parser = argparse.ArgumentParser('Processes a comparison file and prints results')

parser.add_argument('input')
parser.add_argument('-g', '--g', action='store_true')
parser.add_argument('-status')

CONTEXT = 'context'
EXPRESSION = 'expression'
COQ = 'Coq'
R = 'R'


def __read_file(filename):
    with open(filename) as file_:
        return json.load(file_)


def get_general_stats(filename):
    reports = __read_file(filename)

    counter = Counter()
    for report in reports:
        codes = report[ReportKeys.STATUS_CODE]
        for status_code in codes:
            counter[status_code] += 1

    return counter


def get_expressions(reports, status):
    results = []

    for report in reports:
        expressions = exp_extract.extract_expressions(report[ReportKeys.EXPRESSION])
        for i, code in enumerate(report[ReportKeys.STATUS_CODE]):
            if code == status:

                result = {
                    CONTEXT: report[ReportKeys.EXPRESSION],
                    EXPRESSION: expressions[i],
                }
                cases_ = [case.value for case in Status]
                if report[ReportKeys.PROCESSED_COQ][i] in cases_:
                    result[COQ] = str(Status(report[ReportKeys.PROCESSED_COQ][i]))
                else:
                    result[COQ] = report[ReportKeys.PROCESSED_COQ][i]

                if report[ReportKeys.PROCESSED_R][i] == Status.UNKNOWN:
                    result[R] = report[ReportKeys.R_OUT]
                else:
                    if report[ReportKeys.PROCESSED_R][i] in cases_:
                        result[R] = str(Status(report[ReportKeys.PROCESSED_R][i]))
                    else:
                        result[R] = report[ReportKeys.PROCESSED_R][i]

                results.append(result)

    return results


if __name__ == '__main__':
    options = parser.parse_args()

    if options.g:
        stats = get_general_stats(options.input)
        for k, v in stats.most_common():
            print("%s : %d" % (str(Cases(k)), v))

    if options.status:
        reports = __read_file(options.input)

        results = get_expressions(reports, Cases(options.status))
        print(json.dumps(results, indent=2))
