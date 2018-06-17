import re

from coqr.processors.AbstractOutputProcessor import AbstractOutputProcessor
from coqr.reports.results import ErrorResult, FunctionResult, NullResult, BooleanVector, StringVector, \
    NumericVector


class ROutputProcessor(AbstractOutputProcessor):
    error_regex = re.compile(r'^Error:?.*$', re.MULTILINE)
    function_regex = re.compile(r'^function.*$', re.MULTILINE)
    primitive_regex = re.compile(r'^\.Primitive.*$', re.MULTILINE)
    null_regex = re.compile(r'^ *NULL *$', re.MULTILINE)
    boolean_regex = re.compile(r'^ *\[\d+\](?: +TRUE| +FALSE| +NA)+ *$', re.MULTILINE)
    string_regex = re.compile(r'^ *\[\d+\] *(?: +\".*\")+ *$', re.MULTILINE)
    number_regex = re.compile(r'^ *\[\d+\] *(?: +(?:[+-]?(?:(?:[0-9]*[.])?[0-9]+(?:[eE][-+]?[0-9]+)*|Inf)|NA|NaN))+ *$',
                              re.MULTILINE)

    def __init__(self):
        super().__init__()

    def define_cases_handlers(self):
        return [
            (self.error_regex, lambda x: ErrorResult()),
            (self.function_regex, lambda x: FunctionResult()),
            (self.primitive_regex, lambda x: FunctionResult()),
            (self.null_regex, lambda x: NullResult()),
            (self.boolean_regex, lambda x: BooleanVector(self._result_to_boolean_vector(self.boolean_regex.findall(x)))),
            (self.string_regex, lambda x: StringVector(self._result_to_string_vector(self.string_regex.findall(x)))),
            (self.number_regex, lambda x: NumericVector(self._result_to_numeric_vector(self.number_regex.findall(x)))),
        ]

