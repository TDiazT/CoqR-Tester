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


def compare_lists(s, t):
    t = list(t)  # make a mutable copy
    try:
        for elem in s:
            t.remove(elem)
    except ValueError:
        return False
    return not t


with open(options.coq) as coq_file:
    with open(options.r) as r_file:
        coq_results = json.load(coq_file)
        r_results = json.load(r_file)

results = []

for pair in zip(coq_results, r_results):
    coq_output = pair[0]['processed_output']
    r_output = pair[1]['processed_output']

    i = j = 0
    result = []
    while i < len(coq_output) and j < len(r_output):
        comparison = compare(coq_output[i], r_output[j])
        result.append(comparison)
        i += 1
        j += 1

    report = {
        "status_code": result,
        "expression": pair[0]['expression'],
        "coq_output": pair[0]['output'],
        "r_output": pair[1]['output'],
        "processed_coq_output": coq_output,
        "processed_r_output": r_output,
    }
    results.append(report)


with open(options.output, "w") as file_:
    json.dump(results, file_, indent=2)
