from abc import ABC, abstractmethod

from coqr.constants import ReportKeys
from coqr.constants.Cases import Cases


class AbstractOutputProcessor(ABC):
    def __init__(self) -> None:
        self.output_cases = self.define_cases_handlers()

    def process_reports(self, rs):
        for report in rs:
            report[ReportKeys.PROCESSED_OUT] = self.process_outputs(report[ReportKeys.OUTPUT])

        return rs

    def process_outputs(self, outputs):
        result = []
        for out in outputs:
            result.append(self.process_output(out))

        return result

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
