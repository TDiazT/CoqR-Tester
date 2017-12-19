from abc import ABC, abstractmethod
import time
import re

from rcoq.constants import ReportKeys
from rcoq.utils import exp_extract
from rcoq.utils import reports


class AbstractInterpreter(ABC):
    SEQUENCE_TOKEN = '; "TOKEN" ;'
    token_regex = re.compile(r'\[\d\]\s*"TOKEN"\s*')

    def __init__(self, interp) -> None:
        self.name = ''
        self.interpreter = interp

    def interpret_expressions(self, expressions: list):
        results = []
        # None filters blank lines
        for i, expression in enumerate(filter(None, expressions)):
            processed_expression = self.__pre_process_expression(expression)
            exec_time = time.time()
            out = self.interpret(processed_expression)
            exec_time = time.time() - exec_time

            processed_out = self.__post_process_output(out)

            result = reports.generate_report(expression, processed_out, self.name, exec_time=exec_time, line=i + 1)

            results.append(result)

        return results

    @abstractmethod
    def interpret(self, expression):
        pass

    def __pre_process_expression(self, expression):
        expressions = exp_extract.extract_expressions(expression)
        parenthesized_expressions = ["(%s)" % exp for exp in expressions]

        return self.SEQUENCE_TOKEN.join(parenthesized_expressions)

    def __post_process_output(self, out):
        return re.split(self.token_regex, out)

