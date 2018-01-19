import re

from coqr.constants.Cases import Cases
from coqr.processors.AbstractOutputProcessor import AbstractOutputProcessor


class ROutputProcessor(AbstractOutputProcessor):
    vector_regex = re.compile(r'(\[\[*\d+\]*\][ $\w\-\"]*(\[\[\d+\]\])?)')
    error_regex = re.compile(r'Error:*')
    null_regex = re.compile(r'NULL')
    function_regex = re.compile(r'function')
    type_regex = re.compile(r'^(logical|numeric|integer|character).*')
    col_row_regex = re.compile(r'(\[,\d+\]|\[\d+,\][ \w\-\"]+)')
    primitive_regex = re.compile(r'\.Primitive\(.*\)')

    def __init__(self):
        super().__init__()

    def define_cases_handlers(self):
        return [
            (self.error_regex, lambda x: Cases.ERROR),
            (self.null_regex, lambda x: Cases.NULL),
            (self.function_regex, lambda x: Cases.FUNCTION),
            (self.vector_regex, lambda x: " ".join([x[0] for x in self.vector_regex.findall(x)])),
            (self.col_row_regex, lambda x: " ".join(self.col_row_regex.findall(x))),
            (self.primitive_regex, lambda x: Cases.PRIMITIVE),
            (self.type_regex, lambda x: Cases.TYPE)
        ]
