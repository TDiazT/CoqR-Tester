import re
from distutils.util import strtobool
from typing import List, Tuple

from coqr.processors.AbstractOutputProcessor import AbstractOutputProcessor
from coqr.reports.results import ErrorResult, FunctionResult, NullResult, VectorResult, BooleanVector, StringVector, \
    NumericVector


class ROutputProcessor(AbstractOutputProcessor):
    error_regex = re.compile(r'^Error:?.*$', re.MULTILINE)
    function_regex = re.compile(r'^function.*$', re.MULTILINE)
    primitive_regex = re.compile(r'^\.Primitive.*$', re.MULTILINE)
    null_regex = re.compile(r'^ *NULL *$', re.MULTILINE)
    boolean_regex = re.compile(r'^ *\[\d+\] *(?: +TRUE| FALSE)+ *$', re.MULTILINE)
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
            (self.boolean_regex, lambda x: BooleanVector(self.__result_to_boolean_vector(self.boolean_regex.findall(x)))),
            (self.string_regex, lambda x: StringVector(self.__result_to_string_vector(self.string_regex.findall(x)))),
            (self.number_regex, lambda x: NumericVector(self.__result_to_numeric_vector(self.number_regex.findall(x)))),
        ]

    def __result_to_boolean_vector(self, result: List[str]) -> List[bool]:
        spaceless = [list(filter(None, res.split(' '))) for res in result]

        results = []
        for lst in spaceless:
            lst.pop(0)
            results.extend(list(map(lambda x: bool(strtobool(x)), lst)))

        return results

    def __result_to_numeric_vector(self, result: List[str]) -> List[str]:
        spaceless = [list(filter(None, res.split(' '))) for res in result]

        results = []
        for lst in spaceless:
            lst.pop(0)
            for elem in lst:
                try:
                    results.append(float(elem))
                except ValueError:
                    results.append(None)

        return results

    def __result_to_string_vector(self, param: List[str]) -> List[str]:
        results = []
        for res in param:
            extracted = self.__extract_strings(res)
            results.extend(extracted)

        return results

    def __extract_strings(self, output) -> List[str]:
        if not output:
            return []
        elif output[0] == '\"':
            (quote, rest) = self.__extract_double_quote(output[1:])
            return ['\"' + quote] + self.__extract_strings(rest)
        else:
            return self.__extract_strings(output[1:])

    def __extract_double_quote(self, quoted_expression) -> Tuple[str, List]:

        if not quoted_expression:

            return '', []
        elif quoted_expression[0] == '\"':

            return '"', quoted_expression[1:]
        else:
            quote = self.__extract_double_quote(quoted_expression[1:])

            return quoted_expression[0] + quote[0], quote[1]
