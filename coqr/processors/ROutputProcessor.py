import re

from coqr.constants.Cases import Cases
from coqr.processors.AbstractOutputProcessor import AbstractOutputProcessor


class ROutputProcessor(AbstractOutputProcessor):
    error_regex = re.compile(r'^Error:?.*$')
    function_regex = re.compile(r'^function.*$')
    primitive_regex = re.compile(r'^\.Primitive.*$', re.MULTILINE)
    null_regex = re.compile(r'^ *NULL *$', re.MULTILINE)
    boolean_regex = re.compile(r'^ *\[\d+\](?: TRUE| FALSE)+ *$', re.MULTILINE)
    string_regex = re.compile(r'^ *\[\d+\](?: \".*\")+ *$', re.MULTILINE)
    number_regex = re.compile(r'^ *\[\d+\](?: (?:[+-]?(?:(?:[0-9]*[.])?[0-9]+(?:[eE][-+]?[0-9]+)*|Inf)|NA|NaN))+ *$', re.MULTILINE)

    def __init__(self):
        super().__init__()

    def define_cases_handlers(self):
        return [
            (self.error_regex, lambda x: Cases.ERROR),
            (self.function_regex, lambda x: Cases.FUNCTION),
            (self.primitive_regex, lambda x: Cases.FUNCTION),
            (self.null_regex, lambda x: Cases.NULL),
            (self.boolean_regex, lambda x: "\n".join(self.boolean_regex.findall(x))),
            (self.string_regex, lambda x: "\n".join(self.string_regex.findall(x))),
            (self.number_regex, lambda x: "\n".join(self.number_regex.findall(x))),
        ]
