from unittest import TestCase

from coqr.processors.ROutputProcessor import ROutputProcessor
from coqr.reports.results import NullResult, VectorResult, FunctionResult, ErrorResult, \
    InvisibleResult, UnknownResult
from tests.processors.test_processor import TestCommonProcessor


class TestROutputProcessor(TestCase, TestCommonProcessor):
    def setUp(self):
        self.processor = ROutputProcessor()

    def assert_vector(self, output, expected: list):
        result = self.processor.process_output(output)
        self.assertIsInstance(result, VectorResult)
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
        self.assert_vector("[1] NaN\nWarning message:\nIn sqrt(-16) : NaNs produced", ['NaN'])

    def test_booleans(self):
        self.assert_vector('[1] TRUE\n', [True])
        self.assert_vector('[1] FALSE\n', [False])
        self.assert_vector('[1] TRUE\n[2] TRUE', [True, True])
        self.assert_vector('[1] TRUE\n[1] FALSE', [True, False])
        self.assert_vector('[1] TRUE    ', [True])

    def test_simple_number(self):
        self.assert_vector("[1] 1", ['1'])

    def test_vector_with_spaces(self):
        self.assert_vector('[1] TRUE\n', [True])
        self.assert_vector('[1]     FALSE    TRUE  \n', [False, True])
        self.assert_vector('[1]     "test"    "test2"  \n', ['"test"', '"test2"'])
        self.assert_vector('[1]     1   2 3\n', ['1', '2', '3'])
        self.assert_vector('    [1] 1      3', ['1', '3'])

    def test_vector_with_newlines(self):
        self.assert_vector('[1] 1 2 3 4\n[4] 5 6 7 8', ['1', '2', '3', '4', '5', '6', '7', '8'])
        self.assert_vector('[1] TRUE\n[2] FALSE\n[3] TRUE\n[4] FALSE', [True, False, True, False])

    def test_process_string(self):
        self.assert_vector("[1] \" + input + \"\n[1] \" + input + \"\n> ", ["\" + input + \"", "\" + input + \""])

    def test_process_NA(self):
        self.assert_vector("[1] NA", ['NA'])

    def test_process_NaN(self):
        self.assert_vector("[1] NaN", ['NaN'])

    def test_process_Inf(self):
        self.assert_vector("[1] Inf", ['Inf'])
        self.assert_vector("[1] -Inf", ['-Inf'])

    def test_vector_output(self):
        self.assert_vector("[1] 1 2 3\n[4] 5 6 7\n", ['1', '2', '3', '5', '6', '7'])

    def test_vector_with_decimals(self):
        self.assert_vector("[1] 2.4259 3.4293 3.9896 5.2832 5.3386 4.9822\n",
                           ['2.4259', '3.4293', '3.9896', '5.2832', '5.3386', '4.9822'])

    def test_process_multiple_nan(self):
        self.assert_vector("[1] NaN\n [1] NaN\n [4] NaN\n", ['NaN'] * 3)
        self.assert_vector("[1] NaN NaN NaN\n[1] NaN\n [4] NaN\n", ['NaN'] * 5)

    def test_numeric_output(self):
        self.assert_vector("[1] NA NaN 1 1.2 0.3 2e-12 -Inf\n[12] NA NA\n",
                           ['NA', 'NaN', '1', '1.2', '0.3', '2e-12', '-Inf', 'NA', 'NA'])

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
