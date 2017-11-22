import re

from Comparator.Constants import ERROR, NOT, IMPOSSIBLE, SEQ_TOKEN, NULL, CASE_NOT_IMPLEMENTED, CASE_ERROR, \
    CASE_IMPOSSIBLE


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
                        result[-1].extend(line)
                    break
                elif word == '(%s)' % NULL:
                    result.append(NULL)
                    break
                elif word == '>':
                    continue
                else:
                    break

        return result
