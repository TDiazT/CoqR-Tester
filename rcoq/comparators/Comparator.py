from rcoq.comparators.Comparable import NotImplementedComparable, ErrorComparable, ImpossibleComparable, \
    OtherComparable, UnknownComparable
from rcoq.constants import ReportKeys
from rcoq.constants.Status import Status
from rcoq.constants.Cases import Cases
from rcoq.utils.file import read_json_file


class Comparator:
    output_cases = {
        Cases.NOT_IMPLEMENTED: NotImplementedComparable(),
        Cases.IMPOSSIBLE: ImpossibleComparable(),
        Cases.UNKNOWN: UnknownComparable(),
        Cases.ERROR: ErrorComparable()
    }

    def compare(self, out1, out2):
        first_out = self.output_cases.get(out1, OtherComparable(out1))
        second_out = self.output_cases.get(out2, OtherComparable(out2))

        return first_out.compare_to(second_out)

    def compare_outputs(self, coq_output: list, r_output: list):
        i = j = 0
        result = []
        untrusted = False
        while i < len(coq_output) and j < len(r_output):
            comparison = self.compare(coq_output[i], r_output[j])

            if untrusted:
                result.append(Status.untrusted(comparison))
            else:
                if comparison == Status.NOT_IMPLEMENTED or comparison == Status.FAIL or comparison == Status.IMPOSSIBLE:
                    untrusted = True

                result.append(comparison)

            i += 1
            j += 1

        return result

    def compare_files(self, coq, r):
        coq_reports = read_json_file(coq)
        r_reports = read_json_file(r)
        results = []

        for coq_report, r_report in zip(coq_reports, r_reports):
            coq_output = coq_report[ReportKeys.PROCESSED_OUT]
            r_output = r_report[ReportKeys.PROCESSED_OUT]

            result = self.compare_outputs(coq_output, r_output)
            report = {
                ReportKeys.STATUS_CODE: result,
                ReportKeys.EXPRESSION: coq_report[ReportKeys.EXPRESSION],
                ReportKeys.COQ_OUT: coq_report[ReportKeys.OUTPUT],
                ReportKeys.R_OUT: r_report[ReportKeys.OUTPUT],
                ReportKeys.PROCESSED_COQ: coq_output,
                ReportKeys.PROCESSED_R: r_output,
            }
            results.append(report)

        return results
