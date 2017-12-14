import re

from rcoq.constants.Cases import Cases
from rcoq.processors.AbstractOutputProcessor import AbstractOutputProcessor


class ROutputProcessor(AbstractOutputProcessor):
    vector_regex = re.compile(r'\[\d+\][ \w\-\"]+')
    error_regex = re.compile(r'Error:*')
    null_regex = re.compile(r'NULL')
    function_regex = re.compile(r'function')
    type_regex = re.compile(r'^(logical|numeric|integer|character).*')
    col_row_regex = re.compile(r'(\[,\d+\]|\[\d+,\][ \w\-\"]+)')
    primitive_regex = re.compile(r'\.Primitive\(.*\)')

    def __init__(self):
        self.output_cases = [
            (self.error_regex, lambda x: Cases.ERROR),
            (self.null_regex, lambda x: Cases.NULL),
            (self.function_regex, lambda x: Cases.FUNCTION),
            (self.vector_regex, lambda x: " ".join(self.vector_regex.findall(x))),
            (self.col_row_regex, lambda x: " ".join(self.col_row_regex.findall(x))),
            (self.primitive_regex, lambda x: Cases.PRIMITIVE),
            (self.type_regex, lambda x: Cases.TYPE)
        ]

    def process_output(self, output):

        if not output:
            return Cases.INVISIBLE

        for regex, handler in self.output_cases:
            if regex.search(output):
                return handler(output)

        return Cases.UNKNOWN
