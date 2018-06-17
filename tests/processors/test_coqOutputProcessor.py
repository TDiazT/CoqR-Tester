from math import isnan, inf
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
        self.assert_vector('[1]     FALSE\n', [False])
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
