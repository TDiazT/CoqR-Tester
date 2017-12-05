import re

from rcoq.Constants import CASE_INVISIBLE, CASE_ERROR, NULL, CASE_FUNCTION, CASE_UNKNOWN, CASE_TYPE


class ROutputProcessor:
    vec_res_regex = re.compile(r'\[\d+\][ \w-]+')
    error_regex = re.compile(r'Error:*')
    null_regex = re.compile(r'NULL')
    function_regex = re.compile(r'function')
    type_regex = re.compile(r'^(logical|numeric|integer|character).*')

    def process(self, output):

        if not output:
            result = CASE_INVISIBLE
        elif self.error_regex.match(output):
            result = CASE_ERROR
        elif re.search(self.vec_res_regex, output):
            matches = self.vec_res_regex.findall(output)
            result = " ".join(matches)
        elif re.search(self.type_regex, output):
            result = CASE_TYPE
        elif self.function_regex.match(output):
            result = CASE_FUNCTION
        elif self.null_regex.match(output):
            result = NULL
        else:
            result = CASE_UNKNOWN

        return result
