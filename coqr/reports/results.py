from abc import ABC, abstractmethod
from typing import List

from coqr.constants.Status import Status


# noinspection PyMethodMayBeStatic
class ProcessedResult(ABC):
    processed_output = ''

    @abstractmethod
    def compare_to(self, other) -> Status:
        return Status.FAIL

    def compare_to_not_implemented(self, other) -> Status:
        return Status.NOT_IMPLEMENTED

    def compare_to_error(self, other) -> Status:
        return Status.FAIL

    def compare_to_impossible(self, other) -> Status:
        return Status.IMPOSSIBLE

    def compare_to_null(self, other) -> Status:
        return Status.FAIL

    def compare_to_function(self, other) -> Status:
        return Status.FAIL

    def compare_to_unknown(self, other) -> Status:
        return Status.FAIL

    def compare_to_vector(self, other) -> Status:
        return Status.FAIL

    def compare_to_invisible(self, other) -> Status:
        return Status.FAIL

    def to_json(self):
        return self.processed_output


class NullResult(ProcessedResult):
    def __init__(self) -> None:
        super().__init__()
        self.processed_output = 'NULL'

    def compare_to(self, other: ProcessedResult):
        return other.compare_to_null(self)

    def compare_to_null(self, other):
        return Status.PASS


class ImpossibleResult(ProcessedResult):
    def __init__(self) -> None:
        super().__init__()
        self.processed_output = 'Impossible'

    def compare_to(self, other: ProcessedResult):
        return other.compare_to_impossible(self)

    def compare_to_not_implemented(self, other):
        return Status.IMPOSSIBLE

    def compare_to_error(self, other):
        return Status.IMPOSSIBLE

    def compare_to_null(self, other):
        return Status.IMPOSSIBLE

    def compare_to_function(self, other):
        return Status.IMPOSSIBLE

    def compare_to_unknown(self, other):
        return Status.IMPOSSIBLE

    def compare_to_vector(self, other):
        return Status.IMPOSSIBLE

    def compare_to_invisible(self, other):
        return Status.IMPOSSIBLE


class NotImplementedResult(ProcessedResult):
    def __init__(self) -> None:
        super().__init__()
        self.processed_output = 'Not Implemented'

    def compare_to(self, other: ProcessedResult):
        return other.compare_to_not_implemented(self)

    def compare_to_error(self, other):
        return Status.NOT_IMPLEMENTED

    def compare_to_null(self, other):
        return Status.NOT_IMPLEMENTED

    def compare_to_function(self, other):
        return Status.NOT_IMPLEMENTED

    def compare_to_unknown(self, other):
        return Status.NOT_IMPLEMENTED

    def compare_to_vector(self, other):
        return Status.NOT_IMPLEMENTED

    def compare_to_invisible(self, other):
        return Status.NOT_IMPLEMENTED


class ErrorResult(ProcessedResult):
    def __init__(self) -> None:
        super().__init__()
        self.processed_output = 'ERROR'

    def compare_to(self, other: ProcessedResult):
        return other.compare_to_error(self)

    def compare_to_error(self, other):
        return Status.PASS


class FunctionResult(ProcessedResult):
    def __init__(self) -> None:
        super().__init__()
        self.processed_output = 'FUNCTION'

    def compare_to(self, other: ProcessedResult):
        return other.compare_to_function(self)

    def compare_to_function(self, other):
        return Status.PASS


class UnknownResult(ProcessedResult):
    def __init__(self) -> None:
        super().__init__()
        self.processed_output = 'UNKNOWN'

    def compare_to(self, other: ProcessedResult):
        return other.compare_to_unknown(self)

    def compare_to_unknown(self, other):
        return Status.UNKNOWN


class VectorResult(ProcessedResult):
    def __init__(self, vector: List[str]) -> None:
        super().__init__()
        self.result = vector
        self.processed_output = 'VECTOR'

    def compare_to(self, other: ProcessedResult):
        return other.compare_to_vector(self)

    def compare_to_vector(self, other):
        return Status.PASS if self.result == other.result else Status.FAIL

    def to_json(self):
        return str(self.result)


class InvisibleResult(ProcessedResult):
    def __init__(self) -> None:
        super().__init__()
        self.processed_output = 'INVISIBLE'

    def compare_to(self, other: ProcessedResult):
        return other.compare_to_invisible(self)

    def compare_to_invisible(self, other):
        return Status.PASS
