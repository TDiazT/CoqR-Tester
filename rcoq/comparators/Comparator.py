from rcoq.constants import ReportKeys
from rcoq.constants.Status import Status
from rcoq.constants.Cases import Cases
from rcoq.utils.file import read_json_file, write_to_file


def compare(out1, out2):
    if out1 == Cases.NOT_IMPLEMENTED:
        return Status.NOT_IMPLEMENTED
    elif out1 == Cases.IMPOSSIBLE:
        return Status.IMPOSSIBLE
    elif out1 == Cases.UNKNOWN or out2 == Cases.UNKNOWN:
        return Status.UNKNOWN
    elif out1 == Cases.ERROR:
        return Status.PASS if out2 == Cases.ERROR else Status.FAIL
    else:
        if out2 == Cases.INVISIBLE:
            return Status.PASS
        else:
            return Status.PASS if out1 == out2 else Status.FAIL


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
    coq_reports = read_json_file(coq)
    r_reports = read_json_file(r)
    results = []

    for pair in zip(coq_reports, r_reports):
        coq_output = pair[0][ReportKeys.PROCESSED_OUT]
        r_output = pair[1][ReportKeys.PROCESSED_OUT]

        result = compare_outputs(coq_output, r_output)
        report = {
            ReportKeys.STATUS_CODE: result,
            ReportKeys.EXPRESSION: pair[0][ReportKeys.EXPRESSION],
            ReportKeys.COQ_OUT: pair[0][ReportKeys.OUTPUT],
            ReportKeys.R_OUT: pair[1][ReportKeys.OUTPUT],
            ReportKeys.PROCESSED_COQ: coq_output,
            ReportKeys.PROCESSED_R: r_output,
        }
        results.append(report)

    # TODO: Move this somewhere else, it should return the result, not write
    write_to_file(output_, results)