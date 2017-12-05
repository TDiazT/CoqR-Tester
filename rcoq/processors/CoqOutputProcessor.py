import re

from rcoq.Cases import Cases


class CoqOutputProcessor:
    vec_res_regex = re.compile(r'\[\d+\][ \w-]+')
    error_regex = re.compile(r'Error:*')
    null_regex = re.compile(r'NULL')
    function_regex = re.compile(r'(closure)')
    not_implemented = re.compile(r'Not implemented')
    impossible = re.compile(r'Impossible')

    def process(self, output):
        if not output:
            result = str(Cases.INVISIBLE)
        elif self.not_implemented.search(output):
            result = str(Cases.NOT_IMPLEMENTED)
        elif self.impossible.search(output):
            result = str(Cases.IMPOSSIBLE)
        elif self.error_regex.search(output):
            result = str(Cases.ERROR)
        elif re.search(self.vec_res_regex, output):
            matches = self.vec_res_regex.findall(output)
            result = " ".join(matches)
        elif self.function_regex.search(output):
            result = str(Cases.FUNCTION)
        elif self.null_regex.search(output):
            result = str(Cases.NULL)
        else:
            result = str(Cases.UNKNOWN)

        return result

