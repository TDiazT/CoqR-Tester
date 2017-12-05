import re

from rcoq.Constants import ERROR, NOT, IMPOSSIBLE, SEQ_TOKEN, NULL, CASE_NOT_IMPLEMENTED, CASE_ERROR, \
    CASE_IMPOSSIBLE, CASE_INVISIBLE, CASE_FUNCTION, CASE_UNKNOWN


class CoqOutputProcessor:
    vec_res_regex = re.compile(r'\[\d+\][ \w-]+')
    error_regex = re.compile(r'Error:*')
    null_regex = re.compile(r'NULL')
    function_regex = re.compile(r'(closure)')
    not_implemented = re.compile(r'Not implemented')
    impossible = re.compile(r'Impossible')

    def process(self, output):
        if not output:
            result = CASE_INVISIBLE
        elif self.not_implemented.search(output):
            result = CASE_NOT_IMPLEMENTED
        elif self.impossible.search(output):
            result = CASE_IMPOSSIBLE
        elif self.error_regex.search(output):
            result = CASE_ERROR
        elif re.search(self.vec_res_regex, output):
            matches = self.vec_res_regex.findall(output)
            result = " ".join(matches)
        elif self.function_regex.search(output):
            result = CASE_FUNCTION
        elif self.null_regex.search(output):
            result = NULL
        else:
            result = CASE_UNKNOWN

        return result

