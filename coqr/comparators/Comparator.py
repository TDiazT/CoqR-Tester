from typing import List, Tuple

from coqr.constants.Status import Status
from coqr.reports import comparison
from coqr.reports import processing
from coqr.reports.results import ProcessedResult
from coqr.utils.file import read_json_to_processed_report


def comparison_failed(comparison):
    return comparison == Status.NOT_IMPLEMENTED or comparison == Status.FAIL or comparison == Status.IMPOSSIBLE


class Comparator:
    def compare(self, out1: ProcessedResult, out2: ProcessedResult) -> Status:
        """
        Compares two processed outputs and returns a Status Code indicating the result of the comparison
        :param out1: First processed output
        :param out2: Second processed output
        :return: Status code indicating the result of the comparison
        """
        return out1.compare_to(out2)

    def compare_sub_reports(self, coq_sub_reports: List[processing.SubReport],
                            r_sub_reports: List[processing.SubReport]) -> List[
        Tuple[processing.SubReport, processing.SubReport, Status]]:
        """
        Compares the processed outputs from sub reports and returns a list with the result of comparing each.
        If there is a mismatch in length between the amount of sub reports given,
        then the comparison stops when reaching the length of the shortest list of sub reports.

        :param coq_sub_reports: List of SubReports
        :param r_sub_reports: List of SubReports
        :return: List of tuples of the form (SubReport, SubReport, Status) indicating the result of comparing the
        processed output between two sub reports
        """

        i = 0
        results = []
        fail_occurred = False
        while i < len(coq_sub_reports) and i < len(r_sub_reports):

            coq_sub_report = coq_sub_reports[i]
            r_sub_report = r_sub_reports[i]
            comparison = self.compare(coq_sub_report.processed_output, r_sub_report.processed_output)
            if fail_occurred:
                comparison = Status.untrusted(comparison)
            else:
                if comparison_failed(comparison):
                    fail_occurred = True

            results.append((coq_sub_report, r_sub_report, comparison))
            i += 1

        return results

    def compare_results(self, developed_language_results: List[processing.Report],
                        target_language_results: List[processing.Report]) -> List[comparison.Report]:
        results = []

        for report_1, report_2 in zip(developed_language_results, target_language_results):
            comparisons = self.compare_sub_reports(report_1.sub_reports, report_2.sub_reports)
            result = []
            for (sub_report_1, sub_report_2, status) in comparisons:
                final_report = comparison.Report(sub_report_1.expression, status, sub_report_1.output,
                                                 sub_report_2.output, sub_report_1.processed_output,
                                                 sub_report_2.processed_output, report_1.filename,
                                                 sub_report_1.exec_time, sub_report_2.exec_time, report_1.line,
                                                 report_1.expression)

                result.append(final_report)

            results.extend(result)

        return results

    def compare_files(self, developed_language_file: str, target_language_file: str):
        developed_language_results = read_json_to_processed_report(developed_language_file)
        target_language_results = read_json_to_processed_report(target_language_file)

        return self.compare_results(developed_language_results, target_language_results)
