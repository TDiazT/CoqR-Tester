import re
import time
from abc import ABC, abstractmethod
from typing import List

from coqr.parsing import parse
from coqr.utils import reports


class AbstractInterpreter(ABC):
    SEQUENCE_TOKEN = "; 'TOKEN' ;"
    token_regex = re.compile(r'\[\d\]\s*"TOKEN"\s*')

    def __init__(self, interp) -> None:
        self.name = ''
        self.interpreter = interp

    @abstractmethod
    def interpret_multiple(self, expressions: List[str]) -> List[str]:
        pass

    def interpret_expressions(self, expressions: list):
        results = []
        # None filters blank lines
        for i, expression in enumerate(filter(None, expressions)):
            parsed = parse.parse(expression)
            exec_time = time.time()
            out = self.interpret_multiple(parsed)
            exec_time = time.time() - exec_time

            result = reports.generate_report(parsed, out, self.name, exec_time=exec_time, line=i + 1)

            results.append(result)

        return results

    @abstractmethod
    def interpret(self, expression) -> str:
        pass

    def __pre_process_expression(self, expression):
        expressions = parse.parse(expression)
        print(expression)
        print(expressions)
        parenthesized_expressions = ["(%s)" % exp for exp in expressions]

        return self.SEQUENCE_TOKEN.join(parenthesized_expressions)

    def __post_process_output(self, out):
        return re.split(self.token_regex, out)
