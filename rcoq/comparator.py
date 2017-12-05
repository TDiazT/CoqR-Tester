import sys
import json
import argparse

from rcoq.comparators.Comparator import compare

parser = argparse.ArgumentParser(description='Takes two files and compares processed outputs between them')

# #
parser.add_argument('coq')
parser.add_argument('r')
parser.add_argument('output')

options = parser.parse_args()


def __read_file(filename):
    with open(filename) as file_:
        return json.load(file_)


def __write_to_file(filename, comparisons):
    with open(filename, 'w') as file_:
        json.dump(comparisons, file_, indent=2)


def compare_outputs(coq_output, r_output):
    i = j = 0
    result = []
    while i < len(coq_output) and j < len(r_output):
        comparison = compare(coq_output[i], r_output[j])
        result.append(comparison)
        i += 1
        j += 1

    return result


def compare_files(coq, r, output_):
    coq_reports = __read_file(coq)
    r_reports = __read_file(r)
    results = []

    for pair in zip(coq_reports, r_reports):
        coq_output = pair[0]['processed_output']
        r_output = pair[1]['processed_output']

        result = compare_outputs(coq_output, r_output)
        report = {
            "status_code": result,
            "expression": pair[0]['expression'],
            "coq_output": pair[0]['output'],
            "r_output": pair[1]['output'],
            "processed_coq_output": coq_output,
            "processed_r_output": r_output,
        }
        results.append(report)

    __write_to_file(output_, results)


if __name__ == '__main__':
    options = parser.parse_args()

    compare_files(options.coq, options.r, options.output)
