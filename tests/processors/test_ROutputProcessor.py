from math import inf, isnan, nan
from unittest import TestCase

from coqr.processors.ROutputProcessor import ROutputProcessor
from coqr.reports.results import NullResult, VectorResult, FunctionResult, ErrorResult, \
    InvisibleResult, UnknownResult, ListResult
from tests.processors.test_processor import TestCommonProcessor


class TestROutputProcessor(TestCase, TestCommonProcessor):
    def setUp(self):
        self.processor = ROutputProcessor()

    def assert_vector(self, output, expected: list):
        result = self.processor.process_output(output)
        self.assertIsInstance(result, VectorResult)
        self.assertEqual(result.result, expected)

    def assert_list(self, output, expected):
        result = self.processor.process_output(output)
        self.assertIsInstance(result, ListResult)
        self.assertEqual(result.result, expected)

    def assert_is_instance(self, output, instance):
        result = self.processor.process_output(output)
        self.assertIsInstance(result, instance)

    def assert_results(self, results, expected_case):
        for result in results:
            self.assertEqual(result, expected_case)

    def test_process_NULL(self):
        result = self.processor.process_output("NULL\n")
        self.assertIsInstance(result, NullResult)

    def test_process_ignore_warning(self):
        output = self.processor.process_output("[1] NaN\nWarning message:\nIn sqrt(-16) : NaNs produced")
        self.assertTrue(len(output.result) == 1)
        self.assertTrue(isnan(output.result[0]))

    def test_booleans(self):
        self.assert_vector('[1] TRUE\n', [True])
        self.assert_vector('[1] FALSE\n', [False])
        self.assert_vector('[1] TRUE\n[2] TRUE', [True, True])
        self.assert_vector('[1] TRUE\n[1] FALSE', [True, False])
        self.assert_vector('[1] TRUE    ', [True])

    def test_boolean_with_NA(self):
        self.assert_vector("[1] NA    TRUE  NA    FALSE\n", [None, True, None, False])

    def test_simple_number(self):
        self.assert_vector("[1] 1", [1.0])

    def test_vector_with_spaces(self):
        self.assert_vector('[1] TRUE\n', [True])
        self.assert_vector('[1]     FALSE    TRUE  \n', [False, True])
        self.assert_vector('[1]     "test"    "test2"  \n', ['"test"', '"test2"'])
        self.assert_vector('[1]     1   2 3\n', [1.0, 2.0, 3.0])
        self.assert_vector('    [1] 1      3', [1.0, 3.0])
        self.assert_vector("[1] TRUE  FALSE FALSE FALSE\n", [True, False, False, False])
        self.assert_vector("[1] TRUE  TRUE  TRUE  FALSE\n", [True, True, True, False])

    def test_vector_with_newlines(self):
        self.assert_vector('[1] 1 2 3 4\n[4] 5 6 7 8', [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0])
        self.assert_vector('[1] TRUE\n[2] FALSE\n[3] TRUE\n[4] FALSE', [True, False, True, False])

    def test_process_string(self):
        self.assert_vector("[1] \" + input + \"\n[1] \" + input + \"\n> ", ["\" + input + \"", "\" + input + \""])

    def test_process_NA(self):
        self.assert_vector("[1] NA", [None])

    def test_process_NaN(self):
        output = self.processor.process_output("[1] NaN")
        self.assertTrue(len(output.result) == 1)
        self.assertTrue(isnan(output.result[0]))

    def test_process_Inf(self):
        self.assert_vector("[1] Inf", [inf])
        self.assert_vector("[1] -Inf", [-inf])

    def test_vector_output(self):
        self.assert_vector("[1] 1 2 3\n[4] 5 6 7\n", [1.0, 2.0, 3.0, 5.0, 6.0, 7.0])

    def test_vector_with_decimals(self):
        self.assert_vector("[1] 2.4259 3.4293 3.9896 5.2832 5.3386 4.9822\n",
                           [2.4259, 3.4293, 3.9896, 5.2832, 5.3386, 4.9822])

    def test_process_multiple_nan(self):
        output = self.processor.process_output("[1] NaN\n [1] NaN\n [4] NaN\n")
        self.assertTrue(len(output.result) == 3)
        for out in output.result:
            self.assertTrue(isnan(out))

        output = self.processor.process_output("[1] NaN NaN NaN\n[1] NaN\n [4] NaN\n")
        self.assertTrue(len(output.result) == 5)
        for out in output.result:
            self.assertTrue(isnan(out))

    def test_numeric_output(self):
        self.assert_vector("[1] NA  1 1.2 0.3 2e-12 -Inf\n[12] NA NA\n",
                           [None, 1.0, 1.2, 0.3, 2e-12, -inf, None, None])

    def test_string_function_not_mistaken_by_real_function(self):
        self.assert_vector('[1] "function"\n', ['"function"'])

    def test_null_in_function(self):
        self.assert_is_instance("function(n, trans.mat, init.dist=NULL, states=colnames(trans.mat)) { }",
                                FunctionResult)

    def test_process_error_object(self):
        self.assert_is_instance("Error: object 'e' not found", ErrorResult)

    def test_process_error_function(self):
        self.assert_is_instance("Error in e() : could not find function \"e\"", ErrorResult)

    def test_assignment_with_empty_array(self):
        self.assert_is_instance("", InvisibleResult)

    def test_function(self):
        self.assert_is_instance("function (x) x", FunctionResult)

    def test_unknown(self):
        self.assert_is_instance("anything", UnknownResult)
        self.assert_is_instance("adfasd", UnknownResult)

    def test_vector_type_to_unknown(self):
        self.assert_is_instance("integer(0)", UnknownResult)
        self.assert_is_instance("numeric(0)", UnknownResult)
        self.assert_is_instance("logical(0)", UnknownResult)
        self.assert_is_instance("character(0)", UnknownResult)

    def test_cbind_output(self):
        self.assert_is_instance("     [,1] [,2]\n[1,]    1    2\n[2,]    2    2\n[3,]    3    2\n", UnknownResult)

    def test_primitive(self):
        self.assert_is_instance('.Primitive("return")\n', FunctionResult)

    def test_error_zero_length_var(self):
        self.assert_is_instance("Error: attempt to use zero-length variable name\nExecution halted\n", ErrorResult)

    def test_error_no_function_to_return_from(self):
        self.assert_is_instance("Error: no function to return from, jumping to top level\nExecution halted\n",
                                ErrorResult)

    def test_error_in_function(self):
        self.assert_is_instance(
            "Error in (function() break)() : \n  no loop for break/next, jumping to top level\nExecution halted\n",
            ErrorResult)

    def test_error_no_loop(self):
        self.assert_is_instance("Error: no loop for break/next, jumping to top level\nExecution halted\n", ErrorResult)

    def test_function_with_newlines(self):
        self.assert_is_instance("function () \nbreak\n", FunctionResult)

    def test_simple_list(self):
        self.assert_list("[[1]]\n[1] 1", [1])
        self.assert_list("[[1]]\n[1] 1\n[[2]]\n[1] 2\n", [1, 2])
        self.assert_list("[[1]]\n[1] NA\n[[2]]\n[1] Inf\n", [None, inf])
        self.assert_list("[[1]]\n[1] 1\n[[2]]\n[1] -Inf\n[[3]]\n[1] 2.4", [1, -inf, 2.4])

    def test_nested_lists(self):
        self.assert_list("[[1]]\n[1] 1\n[[2]]\n[[2]][[1]]\n[1] 2\n", [1, [2]])
        self.assert_list("[[1]]\n[[1]][[1]]\n[1] 1", [[1]])
        self.assert_list("[[1]]\n[[1]][[1]]\n[1] 1\n[[2]]\n[1] 2\n", [[1], 2])
        self.assert_list("[[1]]\n[[1]][[1]]\n[1] 1\n[[1]][[2]]\n[1] 2\n", [[1, 2]])
        self.assert_list(
            "[[1]]\n[[1]][[1]]\n[[1]][[1]][[1]]\n[[1]][[1]][[1]][[1]]\n[1] 4\n[[1]][[1]][[1]][[2]]\n[1] 5\n[[2]]\n[1] 4",
            [[[[4,5]]], 4])

    def test_fastr_lists(self):
        self.assert_list("[[1]]\n[1] 1\n[[2]]\n[1] 2\n[[3]]\n[[3]][[1]]\n[1] 100", [1, 2, [100]])
