from rcoq.Constants import CASE_NOT_IMPLEMENTED, CASE_ERROR, CASE_IMPOSSIBLE, SUCCESSFUL, CASE_INVISIBLE, \
    UNSUCCESSFUL, CASE_UNKNOWN


def compare(out1, out2):
    if out1 == CASE_NOT_IMPLEMENTED:
        return CASE_NOT_IMPLEMENTED
    elif out1 == CASE_IMPOSSIBLE:
        return CASE_IMPOSSIBLE
    elif out1 == CASE_UNKNOWN or out2 == CASE_UNKNOWN:
        return CASE_UNKNOWN
    elif out1 == CASE_ERROR:
        return SUCCESSFUL if out2 == CASE_ERROR else UNSUCCESSFUL
    else:
        if out2 == CASE_INVISIBLE:
            return SUCCESSFUL
        else:
            return SUCCESSFUL if out1 == out2 else UNSUCCESSFUL

