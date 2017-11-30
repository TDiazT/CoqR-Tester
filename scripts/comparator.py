import sys
import json


def compare(s, t):
    t = list(t)  # make a mutable copy
    try:
        for elem in s:
            t.remove(elem)
    except ValueError:
        return False
    return not t


with open(sys.argv[1]) as file_1:
    with open(sys.argv[2]) as file_2:
        coq_results = json.load(file_1)
        r_results = json.load(file_2)

results = []

for pair in zip(coq_results, r_results):
    coq_output = pair[0]['clean_output']
    r_output = pair[1]['clean_output']
    status = "UNDEFINED"
    if coq_output == "NOT_IMPLEMENTED":
        status = "NOT_IMPLEMENTED"
    elif coq_output == "IMPOSSIBLE":
        status = "IMPOSSIBLE"
    elif coq_output == "ERROR":
        if r_output == "ERROR":
            status = "SUCCESS"
        else:
            status = "FAILED"
    elif coq_output == "FUNCTION":
        if not r_output == "ERROR":
            status = "SUCCESS"
    else:
        status = "SUCCESS" if compare(coq_output, r_output) else "FAILED"

    result = {
        "status_code": status,
        "expression": pair[0]['expression'],
        "coq_output": pair[0]['output'],
        "r_output": pair[1]['output'],
        "clean_coq_output": pair[0]['clean_output'],
        "clean_r_output": pair[1]['clean_output'],
    }

    results.append(result)

with open(sys.argv[3], "w") as file_:
    json.dump(results, file_, indent=2)
