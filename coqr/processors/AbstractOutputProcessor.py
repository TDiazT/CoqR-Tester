import re
from abc import ABC, abstractmethod
from distutils.util import strtobool
from typing import List, Tuple

from coqr.reports import interpretation, processing
from coqr.reports.results import InvisibleResult, UnknownResult


class AbstractOutputProcessor(ABC):
    def __init__(self) -> None:
        self.output_cases = self.define_cases_handlers()

    def process_reports(self, reports: List[interpretation.Report]) -> List[processing.Report]:
        results = []
        for report in reports:
            sub_reports = self.__process_sub_reports(report.sub_reports)
            rep = processing.Report.from_interpretation_report(report)
            rep.add_sub_reports(sub_reports)
            results.append(rep)

        return results

    def __process_sub_reports(self, sub_reports: List[interpretation.InterpretationResult]) -> List[
        processing.SubReport]:
        results = []
        for sub_report in sub_reports:
            results.append(
                processing.SubReport.from_interp_sub_report(sub_report, self.process_output(sub_report.output)))

        return results

    def process_output(self, output):

        if not output:
            return InvisibleResult()

        for regex, handler in self.output_cases:
            if regex.match(output):
                return handler(output)

        return UnknownResult()

    @abstractmethod
    def define_cases_handlers(self):
        pass

    def _result_to_boolean_vector(self, result: List[str]) -> List[bool]:
        spaceless = [list(filter(None, res.split(' '))) for res in result]

        results = []
        for lst in spaceless:
            lst.pop(0)
            for elem in lst:
                try:
                    results.append(bool(strtobool(elem)))
                except ValueError:
                    results.append(None)

        return results

    def _result_to_numeric_vector(self, result: List[str]) -> List[str]:
        spaceless = [list(filter(None, res.split(' '))) for res in result]

        results = []
        for lst in spaceless:
            lst.pop(0)
            for elem in lst:
                try:
                    results.append(float(elem))
                except ValueError:
                    results.append(None)

        return results

    def _result_to_string_vector(self, param: List[str]) -> List[str]:
        # Based on answer https://stackoverflow.com/a/2787064/3802589
        PATTERN = re.compile(r'''((?:[^\[\] "']|"[^"]*"|'[^']*')+)''')
        results = []

        for lst in param:
            split_ = PATTERN.split(lst)[1::2]
            split_.pop(0)
            results.extend(split_)

        return results

    def _extract_strings(self, output) -> List[str]:
        if not output:
            return []
        elif output[0] == '\"':
            (quote, rest) = self._extract_double_quote(output[1:])
            return ['\"' + quote] + self._extract_strings(rest)
        else:
            return self._extract_strings(output[1:])

    def _extract_double_quote(self, quoted_expression) -> Tuple[str, List]:

        if not quoted_expression:

            return '', []
        elif quoted_expression[0] == '\"':

            return '"', quoted_expression[1:]
        else:
            quote = self._extract_double_quote(quoted_expression[1:])

            return quoted_expression[0] + quote[0], quote[1]
