import re

from rcoq.constants.Cases import Cases
from rcoq.processors.AbstractOutputProcessor import AbstractOutputProcessor


class CoqOutputProcessor(AbstractOutputProcessor):
    vector_regex = re.compile(r'\[\d+\][ \w\-\"]+')
    error_regex = re.compile(r'Error:*')
    null_regex = re.compile(r'NULL')
    function_regex = re.compile(r'(closure)')
    not_implemented = re.compile(r'Not implemented')
    impossible = re.compile(r'Impossible')
    special_builtin_regex = re.compile(r'\((builtin|special):.*\)')

    def __init__(self):
        self.output_cases = [
            (self.not_implemented, lambda x: Cases.NOT_IMPLEMENTED),
            (self.impossible, lambda x: Cases.IMPOSSIBLE),
            (self.error_regex, lambda x: Cases.ERROR),
            (self.null_regex, lambda x: Cases.NULL),
            (self.special_builtin_regex, lambda x: Cases.PRIMITIVE),
            (self.vector_regex, lambda x: " ".join(self.vector_regex.findall(x))),
            (self.function_regex, lambda x: Cases.FUNCTION),
        ]

    def process_output(self, output):
        if not output:
            return Cases.INVISIBLE

        for regex, handler in self.output_cases:
            if regex.search(output):
                return handler(output)

        return Cases.UNKNOWN


