from unittest import TestCase

from coqr.constants.Status import Status
from coqr.reports.results import NullResult, ErrorResult, NotImplementedResult, ImpossibleResult, UnknownResult, \
    FunctionResult, VectorResult, InvisibleResult


class TestUnknownResult(TestCase):
    def setUp(self):
        self.result = UnknownResult()

    def test_compare_to_null(self):
        result = self.result.compare_to(NullResult())
        self.assertEqual(result, Status.UNKNOWN)

    def test_compare_to_error(self):
        result = self.result.compare_to(ErrorResult())
        self.assertEqual(result, Status.UNKNOWN)

    def test_compare_to_not_implemented(self):
        result = self.result.compare_to(NotImplementedResult())
        self.assertEqual(result, Status.NOT_IMPLEMENTED)

    def test_compare_to_impossible(self):
        result = self.result.compare_to(ImpossibleResult())
        self.assertEqual(result, Status.IMPOSSIBLE)

    def test_compare_to_unknown(self):
        result = self.result.compare_to(UnknownResult())
        self.assertEqual(result, Status.UNKNOWN)

    def test_compare_to_function(self):
        result = self.result.compare_to(FunctionResult())
        self.assertEqual(result, Status.UNKNOWN)

    def test_compare_to_vector(self):
        result = self.result.compare_to(VectorResult([]))
        self.assertEqual(result, Status.UNKNOWN)

    def test_compare_to_invisible(self):
        result = self.result.compare_to(InvisibleResult())
        self.assertEqual(result, Status.UNKNOWN)
