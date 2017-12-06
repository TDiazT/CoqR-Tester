import re

from rcoq.Cases import Cases


class CoqOutputProcessor:
    vec_res_regex = re.compile(r'\[\d+\][ \w\-\"]+')
    error_regex = re.compile(r'Error:*')
    null_regex = re.compile(r'NULL')
    function_regex = re.compile(r'(closure)')
    not_implemented = re.compile(r'Not implemented')
    impossible = re.compile(r'Impossible')
    special_builtin_regex = re.compile(r'\((builtin|special):.*\)')

    def process(self, output):
        if not output:
            result = Cases.INVISIBLE
        elif self.not_implemented.search(output):
            result = Cases.NOT_IMPLEMENTED
        elif self.impossible.search(output):
            result = Cases.IMPOSSIBLE
        elif self.error_regex.search(output):
            result = Cases.ERROR
        elif re.search(self.vec_res_regex, output):
            matches = self.vec_res_regex.findall(output)
            result = " ".join(matches)
        elif self.function_regex.search(output):
            result = Cases.FUNCTION
        elif re.search(self.special_builtin_regex, output):
            result = Cases.PRIMITIVE
        elif self.null_regex.search(output):
            result = Cases.NULL
        else:
            result = Cases.UNKNOWN

        return result

