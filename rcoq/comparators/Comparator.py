from rcoq.comparators.Comparable import NotImplementedComparable, ErrorComparable, ImpossibleComparable, \
    OtherComparable, UnknownComparable, PrimitiveComparable
from rcoq.constants import ReportKeys
from rcoq.constants.Cases import Cases
from rcoq.constants.Status import Status
from rcoq.utils import reports
from rcoq.utils.file import read_json_file


class Comparator:
    output_cases = {
        Cases.NOT_IMPLEMENTED: NotImplementedComparable(),
        Cases.IMPOSSIBLE: ImpossibleComparable(),
        Cases.UNKNOWN: UnknownComparable(),
        Cases.ERROR: ErrorComparable(),
        Cases.PRIMITIVE: PrimitiveComparable()
    }

    def compare(self, out1, out2):
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

    def compare_files(self, coq, r):
        coq_reports = read_json_file(coq)
        r_reports = read_json_file(r)
        results = []

        for coq_report, r_report in zip(coq_reports, r_reports):
            coq_sub_report = coq_report[ReportKeys.SUB_EXPRESSIONS_REPORT]
            r_sub_report = r_report[ReportKeys.SUB_EXPRESSIONS_REPORT]

            result = self.compare_sub_reports(coq_sub_report, r_sub_report)
            report = {
                ReportKeys.EXPRESSION: coq_report[ReportKeys.EXPRESSION],
                ReportKeys.FILENAME: coq_report[ReportKeys.FILENAME],
                ReportKeys.INTERPRETER: coq_report[ReportKeys.INTERPRETER],
                ReportKeys.R_EXEC_TIME: r_report[ReportKeys.EXEC_TIME],
                ReportKeys.COQ_EXEC_TIME:coq_report[ReportKeys.EXEC_TIME],
                ReportKeys.LINE: coq_report[ReportKeys.LINE],
                ReportKeys.SUB_EXPRESSIONS_REPORT: result
            }
            results.append(report)

        return results
