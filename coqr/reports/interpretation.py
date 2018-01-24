from typing import List, Tuple


class SubReport:
    def __init__(self, expression: str, output: str, exec_time: float = -1) -> None:
        super().__init__()
        self.expression = expression
        self.output = output
        self.exec_time = exec_time


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

    def add_sub_report(self, sub_report: SubReport) -> None:
        self.sub_reports.append(sub_report)


def generate_sub_reports(results: List[Tuple[str, str, int]]) -> List[SubReport]:
    reports = []
    for tuple_ in results:
        reports.append(SubReport(tuple_[0], tuple_[1], tuple_[2]))

    return reports
