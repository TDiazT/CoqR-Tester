import argparse
import json
from collections import Counter

from coqr.constants import ReportKeys
from coqr.constants.Cases import Cases
from coqr.constants.Status import Status
from coqr.utils.file import read_json_file

parser = argparse.ArgumentParser('Processes a comparison file and prints results')

parser.add_argument('input')
parser.add_argument('-g', '--g', action='store_true')
parser.add_argument('-status')

CONTEXT = 'context'
EXPRESSION = 'expression'
FILENAME = 'filename'
LINE = 'line'
COQ = 'Coq'
R = 'R'


def __read_file(filename):
    with open(filename) as file_:
        return json.load(file_)


def get_general_stats(filename):
    file_data = read_json_file(filename)

    reports = file_data["expression_reports"]

    counter = Counter()
    for report in reports:
        code = report[ReportKeys.STATUS_CODE]
        counter[code] += 1

    return counter


def get_expressions(reports, status):
    results = []

    filtered_reports = filter(lambda r: r[ReportKeys.STATUS_CODE] == status, reports)
    for report in filtered_reports:

        result = {
            EXPRESSION: report[ReportKeys.EXPRESSION],
            FILENAME: report[ReportKeys.FILENAME],
            LINE: report[ReportKeys.LINE]
        }
        cases_ = [case.value for case in Cases]
        if report[ReportKeys.PROCESSED_COQ] in cases_:
            result[COQ] = str(Cases(report[ReportKeys.PROCESSED_COQ]))
        else:
            # Cases like [1] 1 2 3, etc
            result[COQ] = report[ReportKeys.PROCESSED_COQ]

        if report[ReportKeys.PROCESSED_R] == Cases.UNKNOWN:
            result[R] = report[ReportKeys.R_OUT]
        else:
            if report[ReportKeys.PROCESSED_R] in cases_:
                result[R] = str(Cases(report[ReportKeys.PROCESSED_R]))
            else:
                result[R] = report[ReportKeys.PROCESSED_R]

        results.append(result)

    return results


if __name__ == '__main__':
    options = parser.parse_args()

    if options.g:
        stats = get_general_stats(options.input)
        for k, v in stats.most_common():
            print("%s : %d" % (str(Status(k)), v))

    if options.status:
        file_data = read_json_file(options.input)
        reports = file_data["expression_reports"]
        results = get_expressions(reports, Status(options.status))
        print(json.dumps(results, indent=2))
