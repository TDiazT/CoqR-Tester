import time
from typing import Dict, List

from coqr.interpreters import AbstractInterpreter
from coqr.parsing import parse
from coqr.utils import reports
from coqr.utils.file import read_file


class FileInterpreter:
    def __init__(self, interpreter: AbstractInterpreter) -> None:
        super().__init__()
        self.interpreter = interpreter

    def interpret_multiline(self, filename):
        parsed = parse.parse_file(filename)
        split_ = list(zip(*parsed))
        lines = split_[0]
        expressions = split_[1]

        exec_time = time.time()
        outputs = self.interpreter.interpret_expressions(expressions)
        exec_time = time.time() - exec_time

        results = []
        for expression, output, line in zip(expressions, outputs, lines):
            results.append(
                reports.generate_report(expression, output, self.interpreter.name, line=line, exec_time=exec_time,
                                        filename=filename))

        return results

    def interpret_line_by_line(self, filename: str) -> List[Dict]:
        lines = read_file(filename)
        results = []
        # None filters blank lines
        for i, line in enumerate(filter(None, lines)):
            expressions = parse.parse_expression(line)
            exec_time = time.time()
            outputs = self.interpreter.interpret_expressions(expressions)
            exec_time = time.time() - exec_time

            for expression, output in zip(expressions, outputs):
                results.append(
                    reports.generate_report(expression, output, self.interpreter.name, line=i + 1, exec_time=exec_time,
                                            filename=filename))

        return results
