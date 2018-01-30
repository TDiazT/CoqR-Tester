from typing import List

from coqr.reports import interpretation
from coqr.reports.results import ProcessedResult


class SubReport:
    def __init__(self, expression: str, output: str, processed_output: ProcessedResult, exec_time: float = -1) -> None:
        super().__init__()
        self.expression = expression
        self.output = output
        self.processed_output = processed_output
        self.exec_time = exec_time

    @classmethod
    def from_interp_sub_report(cls, sub_report: interpretation.InterpretationResult, processed_output: ProcessedResult):
        return cls(sub_report.expression, sub_report.output, processed_output, sub_report.exec_time)

    def to_json(self):
        return self.__dict__


class Report:
    def __init__(self, expression: str, filename: str, interpreter: str, line: int = -1,
                 sub_reports: List[SubReport] = None) -> None:
        super().__init__()
        if sub_reports is None:
            sub_reports = []
        self.expression = expression
        self.interpreter = interpreter
        self.line = line
        self.filename = filename
        self.sub_reports = sub_reports

    @classmethod
    def from_interpretation_report(cls, report: interpretation.Report):
        return cls(expression=report.expression, filename=report.filename, interpreter=report.interpreter,
                   line=report.line)

    def add_sub_reports(self, sub_reports: List[SubReport]) -> None:
        self.sub_reports.extend(sub_reports.copy())

    def to_json(self):
        return self.__dict__
