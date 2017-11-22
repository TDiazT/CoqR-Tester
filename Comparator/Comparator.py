from Comparator.Constants import CASE_NOT_IMPLEMENTED, CASE_ERROR, CASE_IMPOSSIBLE, SUCCESSFUL, CASE_ASSIGNMENT, \
    NOT_EQUAL


class Comparator:
    def compare_multiple(self, coq_outputs, r_outputs):
        assert(len(coq_outputs) == len(r_outputs))

        return map(self.__compare, zip(coq_outputs, r_outputs))

    @staticmethod
    def __compare(coq_output, r_output):
        if coq_output == CASE_NOT_IMPLEMENTED:
            return CASE_NOT_IMPLEMENTED
        elif coq_output == CASE_IMPOSSIBLE:
            return CASE_IMPOSSIBLE
        elif coq_output == CASE_ERROR:
            if r_output == CASE_ERROR:
                return SUCCESSFUL
            else:
                return CASE_ERROR
        else:
            if r_output == CASE_ASSIGNMENT:
                return SUCCESSFUL
            else:
                return SUCCESSFUL if coq_output == r_output else NOT_EQUAL
