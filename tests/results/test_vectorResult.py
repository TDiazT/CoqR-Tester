from typing import List
from unittest import TestCase

from coqr.constants.Status import Status
from coqr.reports.results import NullResult, ErrorResult, NotImplementedResult, ImpossibleResult, UnknownResult, \
    FunctionResult, VectorResult, InvisibleResult


class TestVectorResult(TestCase):
    def setUp(self):
        self.result = VectorResult([])

    def test_compare_to_null(self):
        result = self.result.compare_to(NullResult())
        self.assertEqual(result, Status.FAIL)

    def test_compare_to_error(self):
        result = self.result.compare_to(ErrorResult())
        self.assertEqual(result, Status.FAIL)

    def test_compare_to_not_implemented(self):
        result = self.result.compare_to(NotImplementedResult())
        self.assertEqual(result, Status.NOT_IMPLEMENTED)

    def test_compare_to_impossible(self):
        result = self.result.compare_to(ImpossibleResult())
        self.assertEqual(result, Status.IMPOSSIBLE)

    def test_compare_to_unknown(self):
        result = self.result.compare_to(UnknownResult())
        self.assertEqual(result, Status.FAIL)

    def test_compare_to_function(self):
        result = self.result.compare_to(FunctionResult())
        self.assertEqual(result, Status.FAIL)

    def test_compare_to_invisible(self):
        result = self.result.compare_to(InvisibleResult())
        self.assertEqual(result, Status.FAIL)

    def assert_vector_equals(self, v1: List, v2: List):
        vector_1 = VectorResult(v1)
        vector_2 = VectorResult(v2)

        self.assertEqual(vector_1.compare_to(vector_2), Status.PASS)

    def assert_vector_not_equals(self, v1: List, v2: List):
        vector_1 = VectorResult(v1)
        vector_2 = VectorResult(v2)

        self.assertEqual(vector_1.compare_to(vector_2), Status.FAIL)

    def test_compare_to_vector(self):
        self.assert_vector_equals([], [])
        self.assert_vector_equals([1, 2, 3], [1, 2, 3])
        self.assert_vector_equals(['1', '2', '3'], ['1', '2', '3'])
        self.assert_vector_equals([True, True], [True, True])
        self.assert_vector_equals([False], [False])
        self.assert_vector_equals([False, True], [False, True])
        self.assert_vector_equals(['NA', 'NaN'], ['NA', 'NaN'])

    def test_failed_vector_comparison(self):
        self.assert_vector_not_equals([], ['1'])
        self.assert_vector_not_equals(['1'], [])
        self.assert_vector_not_equals([1, 2], [1, 2, 3])
        self.assert_vector_not_equals(['1', '2', '3'], ['1', '3', '2'])
        self.assert_vector_not_equals([False], [True])
        self.assert_vector_not_equals([True], [False])
        self.assert_vector_not_equals([True, True], [True, False])
        self.assert_vector_not_equals([False, True], [True, True])
        self.assert_vector_not_equals(['NA', 'NaN'], ['NA', '1'])
