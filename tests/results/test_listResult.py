from unittest import TestCase

from coqr.constants.Status import Status
from coqr.reports.results import NullResult, ErrorResult, NotImplementedResult, ImpossibleResult, UnknownResult, \
    FunctionResult, VectorResult, InvisibleResult, ListResult, StringVector, BooleanVector


class TestListResult(TestCase):
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
        self.assertEqual(result, Status.UNKNOWN)

    def test_compare_to_function(self):
        result = self.result.compare_to(FunctionResult())
        self.assertEqual(result, Status.FAIL)

    def test_compare_to_invisible(self):
        result = self.result.compare_to(InvisibleResult())
        self.assertEqual(result, Status.FAIL)

    def assert_list_equals(self, v1: dict, v2: dict):
        list_1 = ListResult(v1)
        list_2 = ListResult(v2)

        self.assertEqual(list_1.compare_to(list_2), Status.PASS)

    def assert_list_not_equals(self, v1: dict, v2: dict):
        vector_1 = ListResult(v1)
        vector_2 = ListResult(v2)

        self.assertEqual(vector_1.compare_to(vector_2), Status.FAIL)

    def test_compare_to_simple_list(self):
        self.assert_list_equals({}, {})
        self.assert_list_equals({'[[1]]': VectorResult([1, 2, 3])}, {'[[1]]': VectorResult([1, 2, 3])})
        self.assert_list_equals({'[[1]]': NullResult()}, {'[[1]]': NullResult()})
        self.assert_list_equals({'[[1]]': StringVector(['"hey"', '"huu"'])},
                                {'[[1]]': StringVector(['"hey"', '"huu"'])})
        self.assert_list_equals({'[[1]]': BooleanVector([True, True])}, {'[[1]]': BooleanVector([True, True])})
        self.assert_list_equals({'[[1]]': FunctionResult()}, {'[[1]]': FunctionResult()})
        self.assert_list_equals({'[[1]]': InvisibleResult()}, {'[[1]]': InvisibleResult()})
        self.assert_list_equals({'[[1]]': ErrorResult()}, {'[[1]]': ErrorResult()})

    def test_compare_nested_lists(self):
        self.assert_list_equals({'[[1]]': VectorResult([1, 2, 3]), '[[2]]': {'[[1]]': VectorResult([1])}},
                                {'[[1]]': VectorResult([1, 2, 3]), '[[2]]': {'[[1]]': VectorResult([1])}})

        self.assert_list_equals(
            {'[[1]]': VectorResult([1]), '[[2]]': {'[[1]]': VectorResult([1])}, '$a': FunctionResult()},
            {'[[1]]': VectorResult([1]), '[[2]]': {'[[1]]': VectorResult([1])}, '$a': FunctionResult()})

        self.assert_list_equals(
            {'[[1]]': VectorResult([1]), '[[2]]': {'[[1]]': ErrorResult()}, '$a': FunctionResult()},
            {'[[1]]': VectorResult([1]), '[[2]]': {'[[1]]': ErrorResult()}, '$a': FunctionResult()})

    def test_unknown_in_lists(self):
        comparison = ListResult({'[[1]]': UnknownResult()}).compare_to(ListResult({'[[1]]': UnknownResult()}))
        self.assertEqual(comparison, Status.UNKNOWN)

        comparison = ListResult({'[[1]]': UnknownResult()}).compare_to(ListResult({'[[1]]': FunctionResult()}))
        self.assertEqual(comparison, Status.UNKNOWN)

        comparison = ListResult({'[[1]]': UnknownResult()}).compare_to(ListResult({'[[1]]': NullResult()}))
        self.assertEqual(comparison, Status.UNKNOWN)

        comparison = ListResult({'[[1]]': UnknownResult()}).compare_to(ListResult({'[[1]]': VectorResult([1])}))
        self.assertEqual(comparison, Status.UNKNOWN)

        comparison = ListResult({'[[1]]': UnknownResult()}).compare_to(ListResult({'[[1]]': StringVector(['"Hey"'])}))
        self.assertEqual(comparison, Status.UNKNOWN)

        comparison = ListResult({'[[1]]': UnknownResult()}).compare_to(ListResult({'[[1]]': BooleanVector([True])}))
        self.assertEqual(comparison, Status.UNKNOWN)

        comparison = ListResult({'[[1]]': UnknownResult()}).compare_to(ListResult({'[[1]]': ErrorResult()}))
        self.assertEqual(comparison, Status.UNKNOWN)

        comparison = ListResult({'[[1]]': NullResult(), '[[2]]': {'$a': UnknownResult()}}).compare_to(
            ListResult({'[[1]]': NullResult(), '[[2]]': {'$a': NullResult()}}))
        self.assertEqual(comparison, Status.UNKNOWN)

        comparison = ListResult({'[[1]]': NullResult(), '[[2]]': {'$a': FunctionResult(),
                                                                  '$bc': {'[[1]]': BooleanVector([True])}},
                                 '[[4]]': FunctionResult()}).compare_to(
            ListResult({'[[1]]': NullResult(), '[[2]]': {'$a': FunctionResult(),
                                                         '$bc': {'[[1]]': UnknownResult()}},
                        '[[4]]': FunctionResult()}))
        self.assertEqual(comparison, Status.UNKNOWN)

    def test_failed_vector_comparison(self):
        self.assert_list_not_equals({}, {'[[1]]': '1'})
        self.assert_list_not_equals({'[[1]]': '1'}, {})
        self.assert_list_not_equals({'[[1]]': VectorResult([]), '$a': NullResult()},
                                    {'[[1]]': VectorResult([]), '$b': NullResult()})

        self.assert_list_not_equals({'[[1]]': VectorResult([1, 2, 3])},
                                    {'[[1]]': VectorResult([1, 2])})

        self.assert_list_not_equals({'[[1]]': VectorResult([1, 2, 3])},
                                    {'[[1]]': BooleanVector([True])})

        self.assert_list_not_equals({'[[1]]': NullResult()},
                                    {'[[1]]': ErrorResult()})

        self.assert_list_not_equals({'[[1]]': FunctionResult()},
                                    {'[[1]]': ErrorResult()})

        self.assert_list_not_equals({'[[1]]': BooleanVector([False])},
                                    {'[[1]]': ErrorResult()})

        self.assert_list_not_equals({'[[1]]': NullResult(), '$b': {'$a': {'$cd': NullResult()}, '[[2]]': NullResult()},
                                     '[[3]]': FunctionResult()},
                                    {'[[1]]': NullResult(), '$b': {'$a': {'$cd': NullResult()}, '[[2]]': ErrorResult()},
                                     '[[3]]': FunctionResult()})
