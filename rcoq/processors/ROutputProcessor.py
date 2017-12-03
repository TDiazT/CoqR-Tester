import re

from rcoq.Constants import CASE_INVISIBLE, CASE_ERROR, SEQ_TOKEN, NULL, CASE_FUNCTION


class ROutputProcessor:
    vec_res_regex = re.compile('\[\d+\]')
    error_regex = re.compile('Error:*')
    flag = False

    def process(self, output):
        result = []
        splitlines = [row.split() for row in output.splitlines()]
        if not splitlines:
            result.append(CASE_INVISIBLE)
            return result

        for line in splitlines:
            for word in line:
                if self.error_regex.match(word):
                    result.append(CASE_ERROR)
                    self.flag = False
                    break
                elif self.vec_res_regex.match(word):
                    if self.vec_res_regex.match(word).group() == '[1]':
                        if line[1] == '"%s"' % SEQ_TOKEN:
                            result.append(SEQ_TOKEN)
                        else:
                            result.append(line)
                    else:
                        result[-1].extend(line)
                    break
                elif word == 'function':
                    result.append(CASE_FUNCTION)
                    break
                elif word == NULL:
                    result.append(NULL)
                    break
                else:
                    break

        return result
