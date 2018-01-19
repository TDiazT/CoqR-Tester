from typing import Dict

from coqr.constants import ReportKeys


def generate_report(expression: str, output: str, interpreter, exec_time=-1, filename="", line=-1) -> Dict:
    return {
        ReportKeys.EXPRESSION: expression,
        ReportKeys.FILENAME: filename,
        ReportKeys.INTERPRETER: interpreter,
        ReportKeys.EXEC_TIME: exec_time,
        ReportKeys.LINE: line,
        ReportKeys.OUTPUT: output
    }


def __generate_sub_report(expression, output):
    result = []
    for i, out in enumerate(output):
        sub_report = {
            ReportKeys.SUB_EXPRESSION: expression[i],
            ReportKeys.OUTPUT: out
        }

        result.append(sub_report)

    return result


def make_comparison_sub_report(sub_expression, status, raw_r, raw_coq, processed_r, processed_coq):
    return {
        ReportKeys.SUB_EXPRESSION: sub_expression,
        ReportKeys.STATUS_CODE: status,
        ReportKeys.R_OUT: raw_r,
        ReportKeys.COQ_OUT: raw_coq,
        ReportKeys.PROCESSED_R: processed_r,
        ReportKeys.PROCESSED_COQ: processed_coq
    }
