from rcoq.Cases import Cases


def compare(out1, out2):
    if out1 == Cases.NOT_IMPLEMENTED:
        return Cases.NOT_IMPLEMENTED
    elif out1 == Cases.IMPOSSIBLE:
        return Cases.IMPOSSIBLE
    elif out1 == Cases.UNKNOWN or out2 == Cases.UNKNOWN:
        return Cases.UNKNOWN
    elif out1 == Cases.ERROR:
        return Cases.SUCCESSFUL if out2 == Cases.ERROR else Cases.UNSUCCESSFUL
    else:
        if out2 == Cases.INVISIBLE:
            return Cases.SUCCESSFUL
        else:
            return Cases.SUCCESSFUL if out1 == out2 else Cases.UNSUCCESSFUL

