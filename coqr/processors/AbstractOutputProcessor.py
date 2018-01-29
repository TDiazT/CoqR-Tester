from abc import ABC, abstractmethod
from typing import List

from coqr.constants.Cases import Cases
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
