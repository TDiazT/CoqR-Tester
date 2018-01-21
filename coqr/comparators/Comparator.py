from typing import List, Dict

from coqr.comparators.Comparable import NotImplementedComparable, ErrorComparable, ImpossibleComparable, \
    OtherComparable, UnknownComparable, PrimitiveComparable
from coqr.constants import ReportKeys
from coqr.constants.Status import Status
from coqr.constants.Cases import Cases
from coqr.utils import reports
from coqr.utils.file import read_json_file


class Comparator:
    output_cases = {
        Cases.NOT_IMPLEMENTED: NotImplementedComparable(),
        Cases.IMPOSSIBLE: ImpossibleComparable(),
        Cases.UNKNOWN: UnknownComparable(),
        Cases.ERROR: ErrorComparable(),
        Cases.PRIMITIVE: PrimitiveComparable()
    }

    def compare(self, out1, out2) -> Status:
        first_out = self.output_cases.get(out1, OtherComparable(out1))
        second_out = self.output_cases.get(out2, OtherComparable(out2))

        return first_out.compare_to(second_out)

    def compare_sub_reports(self, coq_sub_reports: list, r_sub_reports: list):
        i = j = 0
        result = []
        untrusted = False
        while i < len(coq_sub_reports) and j < len(r_sub_reports):

            coq_sub_report = coq_sub_reports[i]
            out_1 = coq_sub_report[ReportKeys.PROCESSED_OUT]
            r_sub_report = r_sub_reports[j]
            out_2 = r_sub_report[ReportKeys.PROCESSED_OUT]
            comparison = self.compare(out_1, out_2)
            if untrusted:
                comparison = Status.untrusted(comparison)
            else:
                if comparison == Status.NOT_IMPLEMENTED or comparison == Status.FAIL or comparison == Status.IMPOSSIBLE:
                    untrusted = True

            comparison_sub_report = reports.make_comparison_sub_report(coq_sub_report[ReportKeys.SUB_EXPRESSION],
                                                                       comparison, r_sub_report[ReportKeys.OUTPUT],
                                                                       coq_sub_report[ReportKeys.OUTPUT],
                                                                       r_sub_report[ReportKeys.PROCESSED_OUT],
                                                                       coq_sub_report[ReportKeys.PROCESSED_OUT])
            result.append(comparison_sub_report)
            i += 1
            j += 1

        return result

    def compare_results(self, developed_language_results: List[Dict], target_language_results: List[Dict]):
        results = []

        for report_1, report_2 in zip(developed_language_results, target_language_results):

            out_1 = report_1[ReportKeys.PROCESSED_OUT]
            out_2 = report_2[ReportKeys.PROCESSED_OUT]
            comparison = self.compare(out_1, out_2)

            report = {
                ReportKeys.EXPRESSION: report_1[ReportKeys.EXPRESSION],
                ReportKeys.CONTEXT: report_2.get(ReportKeys.CONTEXT, ''),
                ReportKeys.FILENAME: report_1[ReportKeys.FILENAME],
                ReportKeys.R_EXEC_TIME: report_2[ReportKeys.EXEC_TIME],
                ReportKeys.COQ_EXEC_TIME:report_1[ReportKeys.EXEC_TIME],
                ReportKeys.LINE: report_1[ReportKeys.LINE],
                ReportKeys.STATUS_CODE: comparison,
                ReportKeys.R_OUT: report_2[ReportKeys.OUTPUT],
                ReportKeys.COQ_OUT: report_1[ReportKeys.OUTPUT],
                ReportKeys.PROCESSED_R: report_2[ReportKeys.PROCESSED_OUT],
                ReportKeys.PROCESSED_COQ: report_1[ReportKeys.PROCESSED_OUT]
            }


            results.append(report)

        return results

    def compare_files(self, developed_language_file: str, target_language_file: str):
        developed_language_results = read_json_file(developed_language_file)
        target_language_results = read_json_file(target_language_file)

        return self.compare_results(developed_language_results, target_language_results)
