import argparse
import json
import re
from collections import Counter

from rcoq.Cases import Cases

parser = argparse.ArgumentParser('Processes a comparison file and prints results')

parser.add_argument('-input', default='out/compare.json')
parser.add_argument('-g', '--g', action='store_true')
parser.add_argument('-status')

token_regex = re.compile(r';\s*"TOKEN"\s*;')


def __read_file(filename):
    with open(filename) as file_:
        return json.load(file_)


def get_general_stats(filename):
    reports = __read_file(filename)

    counter = Counter()
    for report in reports:
        codes = report['status_code']
        for status_code in codes:
            counter[status_code] += 1

    return counter


def get_expressions(reports, status):
    results = []

    for report in reports:
        expressions = token_regex.split(report['expression'])
        for i, code in enumerate(report['status_code']):
            if code == status:
                result = {
                    'expression': expressions[i],
                }
                cases_ = [case.value for case in Cases]
                if report['processed_coq_output'][i] in cases_:
                    result['coq'] = str(Cases(report['processed_coq_output'][i]))
                else:
                    result['coq'] = report['processed_coq_output'][i]

                if report['processed_r_output'][i] in cases_:
                    result['r'] = str(Cases(report['processed_r_output'][i]))
                else:
                    result['r'] = report['processed_r_output'][i]

                results.append(result)

    return results


if __name__ == '__main__':
    options = parser.parse_args()

    if options.g:
        stats = get_general_stats(options.input)
        for k, v in stats.most_common():
            print("%s : %d" % (k, v))

    if options.status:
        reports = __read_file(options.input)

        results = get_expressions(reports, options.status)
        print(json.dumps(results, indent=2))
