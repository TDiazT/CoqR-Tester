import re

from coqr.processors.AbstractOutputProcessor import AbstractOutputProcessor
from coqr.reports.results import ErrorResult, NotImplementedResult, ImpossibleResult, NullResult, FunctionResult, \
    BooleanVector, StringVector, NumericVector, ListResult


class CoqOutputProcessor(AbstractOutputProcessor):
    error_regex = re.compile(r'^Error:?.*$', re.MULTILINE)
    function_regex = re.compile(r'^\(closure\).*$', re.MULTILINE)
    special_builtin_regex = re.compile(r'^\((builtin|special):.*\)$', re.MULTILINE)
    null_regex = re.compile(r'^ *NULL *$', re.MULTILINE)
    boolean_regex = re.compile(r'^ *\[\d+\](?: +TRUE| +FALSE| +NA)+ *$', re.MULTILINE)
    string_regex = re.compile(r'^ *\[\d+\](?: +\".*\")+ *$', re.MULTILINE)
    number_regex = re.compile(r'^ *\[\d+\](?: +(?:[+-]?(?:(?:[0-9]*[.])?[0-9]+(?:[eE][-+]?[0-9]+)*|Inf)|NA|NaN))+ *$',
                              re.MULTILINE)
    list_regex = re.compile(
        r'^(\[\[\d+\]\](?:\[\[\d+\]\])*|\[\d+\] *(?: +(?:[+-]?(?:(?:[0-9]*[.])?[0-9]+(?:[eE][-+]?[0-9]+)*|Inf)|NA|NaN))+ *)$',
        re.MULTILINE)
    not_implemented = re.compile(r'^Not implemented:.*$', re.MULTILINE)
    impossible = re.compile(r'^Impossible.*$', re.MULTILINE)

    def __init__(self):
        super().__init__()

    def define_cases_handlers(self):
        return [
            (self.error_regex, lambda x: ErrorResult()),
            (self.not_implemented, lambda x: NotImplementedResult()),
            (self.impossible, lambda x: ImpossibleResult()),
            (self.null_regex, lambda x: NullResult()),
            (self.special_builtin_regex, lambda x: FunctionResult()),
            (self.function_regex, lambda x: FunctionResult()),
            (self.boolean_regex,
             lambda x: BooleanVector(self._result_to_boolean_vector(self.boolean_regex.findall(x)))),
            (self.string_regex, lambda x: StringVector(self._result_to_string_vector(self.string_regex.findall(x)))),
            (self.number_regex, lambda x: NumericVector(self._result_to_numeric_vector(self.number_regex.findall(x)))),
            (self.list_regex, lambda x: ListResult(self._result_to_list(self.list_regex.findall(x))))

        ]
