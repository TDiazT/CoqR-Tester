from typing import List


class Report:
    def __init__(self, expression: str, filename: str, interpreter: str, line: int = -1,
                 sub_reports: List[SubReport] = None, exec_time=-1) -> None:
        super().__init__()
        if sub_reports is None:
            sub_reports = []
        self.expression = expression
        self.interpreter = interpreter
        self.line = line
        self.filename = filename
        self.sub_reports = sub_reports
        self.exec_time = exec_time

    def add_sub_report(self, sub_report: SubReport) -> None:
        self.sub_reports.append(sub_report)


class SubReport:
    def __init__(self, expression, output) -> None:
        super().__init__()
        self.expression = expression
        self.output = output
