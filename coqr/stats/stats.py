import argparse
import json
from collections import Counter

from coqr.constants.Status import Status
from coqr.utils.file import read_json_file, read_json_to_report

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
    file_data = read_json_to_report(filename)

    reports = file_data.expression_reports

    counter = Counter()
    for report in reports:
        code = report.status_code
        counter[code] += 1

    return counter


def get_expressions(reports, status):
    results = []

    filtered_reports = filter(lambda r: r.status_code == status, reports)
    for report in filtered_reports:

        result = {EXPRESSION: report.expression, FILENAME: report.filename, LINE: report.line, COQ: report.dev_output,
                  R: report.target_output}

        results.append(result)

    return results


if __name__ == '__main__':
    options = parser.parse_args()

    if options.g:
        stats = get_general_stats(options.input)
        for k, v in stats.most_common():
            print("%s : %d" % (str(Status(k)), v))

    if options.status:
        file_data = read_json_to_report(options.input)

        reports = file_data.expression_reports
        results = get_expressions(reports, Status(options.status))
        print(json.dumps(results, indent=2))
