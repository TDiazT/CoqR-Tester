from rcoq.Cases import Cases


def compare(out1, out2):
    if out1 == Cases.NOT_IMPLEMENTED:
        return str(Cases.NOT_IMPLEMENTED)
    elif out1 == Cases.IMPOSSIBLE:
        return str(Cases.IMPOSSIBLE)
    elif out1 == Cases.UNKNOWN or out2 == Cases.UNKNOWN:
        return str(Cases.UNKNOWN)
    elif out1 == Cases.ERROR:
        return str(Cases.SUCCESSFUL) if out2 == Cases.ERROR else str(Cases.UNSUCCESSFUL)
    else:
        if out2 == Cases.INVISIBLE:
            return str(Cases.SUCCESSFUL)
        else:
            return str(Cases.SUCCESSFUL) if out1 == out2 else str(Cases.UNSUCCESSFUL)

