import re

ERROR = "Error:"

NOT = "Not"

IMPOSSIBLE = "Impossible"

SEQ_TOKEN = "SPECIAL_SUPER_TOKEN"

NULL = "NULL"

CASE_NOT_IMPLEMENTED = "CASE_NOT_IMPLEMENTED"

CASE_ERROR = "CASE_ERROR"

CASE_IMPOSSIBLE = "CASE_IMPOSSIBLE"

CASE_ASSIGNMENT = "CASE_ASSIGNMENT"


class CoqOutputProcessor:
    vec_res_regex = re.compile('\[\d+\]')

    def process(self, output):
        result = []

        splitlines = [line.split() for line in output.splitlines()]

        for line in splitlines:
            for word in line:
                if word == ERROR:
                    result.append(CASE_ERROR)
                    break
                elif word == NOT:
                    result.append(CASE_NOT_IMPLEMENTED)
                    break
                elif word == IMPOSSIBLE:
                    result.append(CASE_IMPOSSIBLE)
                    break
                elif self.vec_res_regex.match(word) is not None:
                    if self.vec_res_regex.match(word).group() == '[1]':
                        if line[1] == '"%s"' % SEQ_TOKEN:
                            break
                        else:
                            result.append(line)
                    else:
                        result[-1].append(line)
                    break
                elif word == '(%s)' % NULL:
                    result.append(NULL)
                    break
                elif word == '>':
                    continue
                else:
                    break

        return result
