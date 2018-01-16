import argparse
import json
from collections import Counter

from coqr.constants import ReportKeys
from coqr.constants.Cases import Cases
from coqr.constants.Status import Status

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
        for sub_report in report[ReportKeys.SUB_EXPRESSIONS_REPORT]:
            code = sub_report[ReportKeys.STATUS_CODE]
            counter[code] += 1

    return counter


def get_expressions(reports, status):
    results = []

    for report in reports:

        filtered_sub_reports = filter(lambda r: r[ReportKeys.STATUS_CODE] == status,
                                      report[ReportKeys.SUB_EXPRESSIONS_REPORT])
        for sub_report in filtered_sub_reports:
            result = {
                CONTEXT: report[ReportKeys.EXPRESSION],
                EXPRESSION: sub_report[ReportKeys.SUB_EXPRESSION],
            }
            cases_ = [case.value for case in Cases]
            if sub_report[ReportKeys.PROCESSED_COQ] in cases_:
                result[COQ] = str(Cases(sub_report[ReportKeys.PROCESSED_COQ]))
            else:
                # Cases like [1] 1 2 3, etc
                result[COQ] = sub_report[ReportKeys.PROCESSED_COQ]

            if sub_report[ReportKeys.PROCESSED_R] == Cases.UNKNOWN:
                result[R] = sub_report[ReportKeys.R_OUT]
            else:
                if sub_report[ReportKeys.PROCESSED_R] in cases_:
                    result[R] = str(Cases(sub_report[ReportKeys.PROCESSED_R]))
                else:
                    result[R] = sub_report[ReportKeys.PROCESSED_R]

            results.append(result)

    return results


if __name__ == '__main__':
    options = parser.parse_args()

    if options.g:
        stats = get_general_stats(options.input)
        for k, v in stats.most_common():
            print("%s : %d" % (str(Status(k)), v))

    if options.status:
        reports = __read_file(options.input)

        results = get_expressions(reports, Status(options.status))
        print(json.dumps(results, indent=2))
