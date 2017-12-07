from rcoq.Cases import Cases
from rcoq.utils.file import read_file, write_to_file


def compare(out1, out2):
    if out1 == Cases.NOT_IMPLEMENTED:
        return Cases.NOT_IMPLEMENTED
    elif out1 == Cases.IMPOSSIBLE:
        return Cases.IMPOSSIBLE
    elif out1 == Cases.UNKNOWN or out2 == Cases.UNKNOWN:
        return Cases.UNKNOWN
    elif out1 == Cases.ERROR:
        return Cases.PASS if out2 == Cases.ERROR else Cases.FAIL
    else:
        if out2 == Cases.INVISIBLE:
            return Cases.PASS
        else:
            return Cases.PASS if out1 == out2 else Cases.FAIL


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
    coq_reports = read_file(coq)
    r_reports = read_file(r)
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

    write_to_file(output_, results)