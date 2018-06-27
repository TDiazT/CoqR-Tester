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
    list_regex = re.compile(r'^ *\[\[\d+\]\].*$', re.MULTILINE)
    empty_list = re.compile(r'^list\(\)$', re.MULTILINE)
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
            (self.list_regex, lambda x: ListResult(self._result_to_list(x))),
            (self.empty_list, lambda x: ListResult({}))

        ]

    def _result_to_list(self, result: str) -> dict:
        bracket_regex = re.compile(r'\[\[\d+\]\]')

        lines = result.split("\n")
        # lines = list(filter(None, lines_aux))

        res = {}
        aux = res
        index = 1
        last = "[[1]]"
        current_result_str = ""
        attr = False
        count = 0
        last_full_match = ""
        for line in lines:
            if self.list_regex.match(line):
                match = bracket_regex.findall(line)
                last_full_match = match
                size = len(match)
                count = 0

                if size > index:
                    last_ = match[index - 1]
                    aux[last_] = {}
                    aux = aux[last_]
                    index = size

                elif size < index:
                    if current_result_str:
                        aux[last] = self.process_output(current_result_str)

                    aux = res
                    for i in range(0, size - 1):
                        aux = aux[match[i]]

                    index = size
                    current_result_str = ""
                else:
                    if current_result_str:
                        aux[last] = self.process_output(current_result_str)
                    current_result_str = ""

                last = match[-1]

            elif line == 'attr(,"names")':
                if current_result_str:
                    aux[last] = self.process_output(current_result_str)
                attr = True
                continue
            elif attr:
                if self.string_regex.match(line):
                    names = self._result_to_string_vector(self.string_regex.findall(line))
                    aux = res
                    for i in range(0, index - count):
                        aux = aux[last_full_match[i]]

                    keys = aux.keys()
                    key_size = len(keys)
                    for i in range(0, key_size):
                        new_key = names[i][1:-1]
                        if new_key:
                            aux["$%s" % new_key] = aux["[[%i]]" % (i + 1)]
                            del aux["[[%i]]" % (i + 1)]
                attr = False
                current_result_str = ""
                continue
            elif not line:
                count = count + 1
            else:
                count = 0
                current_result_str = current_result_str + "\n" + line if current_result_str else line

        if current_result_str:
            aux[last] = self.process_output(current_result_str)

        return res
