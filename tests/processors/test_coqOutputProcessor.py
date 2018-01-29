from unittest import TestCase

from coqr.processors.CoqOutputProcessor import CoqOutputProcessor
from coqr.reports.results import VectorResult, NullResult, FunctionResult, ErrorResult, InvisibleResult, UnknownResult, \
    NotImplementedResult
from tests.processors.test_processor import TestCommonProcessor


class TestCoqOutputProcessor(TestCase, TestCommonProcessor):
    def setUp(self):
        self.processor = CoqOutputProcessor()

    def assert_vector(self, output, expected: list):
        result = self.processor.process_output(output)
        self.assertIsInstance(result, VectorResult)
        self.assertEqual(result.result, expected)

    def assert_is_instance(self, output, instance):
        result = self.processor.process_output(output)
        self.assertIsInstance(result, instance)

    def test_process_error_object(self):
        self.assert_is_instance("Error: [eval] Object not found.\nAn error lead to an undefined result.\n", ErrorResult)
        self.assert_is_instance("Error: [eval] Object not found.\nAn error lead to an undefined result.\n", ErrorResult)

    def test_function(self):
        self.assert_is_instance("(closure)\n", FunctionResult)

    def test_not_implemented(self):
        self.assert_is_instance(
            "Not implemented: [do_c]\nAn error lead to an undefined state. Continuing using the old one.\n"
            "An error lead to an undefined result.\n> ", NotImplementedResult)

    def test_parse_error_over_not_implemented(self):
        output = "Error: Parser error at offset 2133.\n> Error: [findFun3] Could not find function \u201cf\u201d.\n" \
                 "An error lead to an undefined result.\n> Error: Parser error at offset 2166.\n" \
                 "> > > (closure)\n> Error: [findFun3] Could not find function \u201cdeparse\u201d.\n" \
                 "An error lead to an undefined result.\n" \
                 "> Not implemented: [do_for]\nAn error lead to an undefined state. Continuing using the old one.\n" \
                 "An error lead to an undefined result."
        self.assert_is_instance(output, ErrorResult)

    def test_process_NULL(self):
        self.assert_is_instance("NULL", NullResult)

    def test_process_ignore_warning(self):
        self.assert_vector("[1] NaN\nWarning message:\nIn sqrt(-16) : NaNs produced", ['NaN'])

    def test_booleans(self):
        self.assert_vector('[1] TRUE\n', ['TRUE'])
        self.assert_vector('[1] FALSE\n', ['FALSE'])
        self.assert_vector('[1] TRUE\n[2] TRUE', ['TRUE', 'TRUE'])
        self.assert_vector('[1] TRUE\n[1] FALSE', ['TRUE', 'FALSE'])
        self.assert_vector('[1] TRUE    ', ['TRUE'])

    def test_simple_number(self):
        self.assert_vector("[1] 1", ['1'])

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

    def test_process_error_function(self):
        self.assert_is_instance("Error in e() : could not find function \"e\"", ErrorResult)

    def test_assignment_with_empty_array(self):
        self.assert_is_instance("", InvisibleResult)

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
