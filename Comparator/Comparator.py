from Comparator.Constants import CASE_NOT_IMPLEMENTED, CASE_ERROR, CASE_IMPOSSIBLE, SUCCESSFUL, CASE_INVISIBLE, \
    NOT_EQUAL


class Comparator:
    def compare_multiple(self, coq_outputs, r_outputs):
        assert(len(coq_outputs) == len(r_outputs))

        return list(map(self.__compare, zip(coq_outputs, r_outputs)))

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
