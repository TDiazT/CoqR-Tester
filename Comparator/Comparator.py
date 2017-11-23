from Comparator.Constants import CASE_NOT_IMPLEMENTED, CASE_ERROR, CASE_IMPOSSIBLE, SUCCESSFUL, CASE_INVISIBLE, \
    NOT_EQUAL, SEQ_TOKEN


class Comparator:
    def compare_multiple(self, coq_outputs, r_outputs):
        i = j = 0
        token_flag = False
        results = []

        while i < len(coq_outputs) and j < len(r_outputs):
            if coq_outputs[i] == CASE_NOT_IMPLEMENTED:
                results.append(CASE_NOT_IMPLEMENTED)
            elif coq_outputs[i] == CASE_IMPOSSIBLE:
                results.append(CASE_IMPOSSIBLE)
            elif coq_outputs[i] == CASE_ERROR:
                if r_outputs[j] == CASE_ERROR:
                    results.append(SUCCESSFUL)
                else:
                    results.append(NOT_EQUAL)
            elif coq_outputs[i] == SEQ_TOKEN:
                if r_outputs[j] == SEQ_TOKEN:
                    token_flag = True
                else:
                    results.append(NOT_EQUAL)
            else:
                if r_outputs[j] == SEQ_TOKEN:
                    if token_flag:
                        results.append(SUCCESSFUL)
                        i += 1
                    else:
                        results.append(NOT_EQUAL)
                else:
                    results.append(SUCCESSFUL if coq_outputs[i] == r_outputs[j] else NOT_EQUAL)

            i += 1
            j += 1

        return results

    @staticmethod
    def __compare(outputs):
        if outputs[0] == CASE_NOT_IMPLEMENTED:
            return CASE_NOT_IMPLEMENTED
        elif outputs[0] == CASE_IMPOSSIBLE:
            return CASE_IMPOSSIBLE
        elif outputs[0] == CASE_ERROR:
            if outputs[1] == CASE_ERROR:
                return SUCCESSFUL
            else:
                return CASE_ERROR
        else:
            if outputs[1] == CASE_INVISIBLE:
                return SUCCESSFUL
            else:
                return SUCCESSFUL if outputs[0] == outputs[1] else NOT_EQUAL
