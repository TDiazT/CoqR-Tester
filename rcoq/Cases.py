from aenum import unique, IntEnum


# https://stackoverflow.com/a/43863085/3802589
@unique
class Cases(IntEnum):
    _init_ = 'value string'

    NOT_IMPLEMENTED = 1, "Not implemented"
    ERROR = 2, "Error"
    IMPOSSIBLE = 3, "Impossible"
    INVISIBLE = 4, "Invisible"
    PASS = 5, "Pass"
    FAIL = 6, "Fail"
    FUNCTION = 7, "Function"
    UNKNOWN = 8, "Unknown"
    NULL = 9, "Null"
    TYPE = 10, "Type"
    PRIMITIVE = 11, "Primitive"

    def __str__(self):
        return self.string

    @classmethod
    def _missing_value_(cls, value):
        for member in cls:
            if member.string == value:
                return member
