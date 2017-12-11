from aenum import Enum, unique


@unique
class Status(Enum):
    _init_ = 'value string'

    NOT_IMPLEMENTED = 1, "Not implemented"
    IMPOSSIBLE = 3, "Impossible"
    PASS = 5, "Pass"
    FAIL = 6, "Fail"
    UNKNOWN = 8, "Unknown"

    def __str__(self):
        return self.string

    @classmethod
    def _missing_value_(cls, value):
        for member in cls:
            if member.string == value:
                return member
