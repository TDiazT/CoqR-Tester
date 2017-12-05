import re

from rcoq.Cases import Cases
from rcoq.Constants import CASE_INVISIBLE, CASE_ERROR, NULL, CASE_FUNCTION, CASE_UNKNOWN, CASE_TYPE


class ROutputProcessor:
    vec_res_regex = re.compile(r'\[\d+\][ \w-]+')
    error_regex = re.compile(r'Error:*')
    null_regex = re.compile(r'NULL')
    function_regex = re.compile(r'function')
    type_regex = re.compile(r'^(logical|numeric|integer|character).*')

    def process(self, output):

        if not output:
            result = Cases.INVISIBLE
        elif self.error_regex.match(output):
            result = Cases.ERROR
        elif re.search(self.vec_res_regex, output):
            matches = self.vec_res_regex.findall(output)
            result = " ".join(matches)
        elif re.search(self.type_regex, output):
            result = Cases.TYPE
        elif self.function_regex.match(output):
            result = Cases.FUNCTION
        elif self.null_regex.match(output):
            result = Cases.NULL
        else:
            result = Cases.UNKNOWN

        return result
