from abc import ABC, abstractmethod

from rcoq.constants import ReportKeys


class AbstractOutputProcessor(ABC):
    def process_reports(self, rs):
        for report in rs:
            report[ReportKeys.PROCESSED_OUT] = self.process_outputs(report[ReportKeys.OUTPUT])

        return rs

    def process_outputs(self, outputs):
        result = []
        for out in outputs:
            result.append(self.process_output(out))

        return result

    @abstractmethod
    def process_output(self, output):
        pass
