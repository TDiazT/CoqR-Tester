from aenum import unique, IntEnum


@unique
class Status(IntEnum):
    _init_ = 'value string'

    NOT_IMPLEMENTED = 1, "Not implemented"
    IMPOSSIBLE = 3, "Impossible"
    PASS = 5, "Pass"
    FAIL = 6, "Fail"
    UNKNOWN = 8, "Unknown"
    POTENTIAL_PASS = 9, "Potential Pass"
    POTENTIAL_FAIL = 10, "Potential Fail"

    def __str__(self):
        return self.string

    @classmethod
    def _missing_value_(cls, value):
        for member in cls:
            if member.string == value:
                return member

    @classmethod
    def untrusted(cls, status):
        if status == cls.PASS:
            return cls.POTENTIAL_PASS
        elif status == cls.FAIL:
            return cls.POTENTIAL_FAIL
        else:
            return status
