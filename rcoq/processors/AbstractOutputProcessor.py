from abc import ABC, abstractmethod

from rcoq.constants import ReportKeys
from rcoq.constants.Cases import Cases


class AbstractOutputProcessor(ABC):
    def __init__(self) -> None:
        self.output_cases = self.define_cases_handlers()

    def process_reports(self, rs):
        for report in rs:
            self.__process_sub_reports(report[ReportKeys.SUB_EXPRESSIONS_REPORT])

        return rs

    def __process_sub_reports(self, sub_reports):
        for sub_report in sub_reports:
            sub_report[ReportKeys.PROCESSED_OUT] = self.process_output(sub_report[ReportKeys.OUTPUT])

    def process_output(self, output):

        if not output:
            return Cases.INVISIBLE

        for regex, handler in self.output_cases:
            if regex.search(output):
                return handler(output)

        return Cases.UNKNOWN

    @abstractmethod
    def define_cases_handlers(self):
        pass
