from unittest import TestCase

from coqr.constants.Cases import Cases
from coqr.processors.ROutputProcessor import ROutputProcessor
from tests.processors.test_processor import TestCommonProcessor


class TestROutputProcessor(TestCase, TestCommonProcessor):
    def setUp(self):
        self.processor = ROutputProcessor()

    def assert_results(self, results, expected_case):
        for result in results:
            self.assertEqual(result, expected_case)

    def test_process_NULL(self):
        result = self.processor.process_output("NULL\n")
        self.assertEqual(result, Cases.NULL)

    def test_process_ignore_warning(self):
        self.assert_output("[1] NaN\nWarning message:\nIn sqrt(-16) : NaNs produced", "[1] NaN")

    def test_booleans(self):
        self.assert_output('[1] TRUE\n', '[1] TRUE')
        self.assert_output('[1] FALSE\n', '[1] FALSE')
        self.assert_output('[1] TRUE\n[2] TRUE', '[1] TRUE\n[2] TRUE')
        self.assert_output('[1] TRUE\n[1] FALSE', '[1] TRUE\n[1] FALSE')
        self.assert_output('[1] TRUE    ', '[1] TRUE    ')

    def test_process_string(self):
        self.assert_output("[1] \" + input + \"\n[1] \" + input + \"\n> ",
                           "[1] \" + input + \"\n[1] \" + input + \"")

    def test_process_multiple_nan(self):
        self.assert_output("[1] NaN\n [1] NaN\n [4] NaN\n", "[1] NaN\n [1] NaN\n [4] NaN")
        self.assert_output("[1] NaN NaN NaN\n[1] NaN\n [4] NaN\n", "[1] NaN NaN NaN\n[1] NaN\n [4] NaN")

    def test_numeric_output(self):
        self.assert_output("[1] NA NaN 1 1.2 0.3 2e-12 -Inf\n[12] NA NA\n",
                           "[1] NA NaN 1 1.2 0.3 2e-12 -Inf\n[12] NA NA")

    def test_simple_number(self):
        self.assert_output("[1]  TRUE FALSE\n", "[1]  TRUE FALSE")

    def test_string_function_not_mistaken_by_real_function(self):
        self.assert_output('[1] "function"\n', '[1] "function"')

    def test_null_in_function(self):
        self.assert_output("function(n, trans.mat, init.dist=NULL, states=colnames(trans.mat)) { }", Cases.FUNCTION)

    def test_process_error_object(self):
        result = self.processor.process_output("Error: object 'e' not found")
        self.assertEqual(result, Cases.ERROR)

    def test_process_error_function(self):
        result = self.processor.process_output(
            "Error in e() : could not find function \"e\"")
        self.assertEqual(result, Cases.ERROR)

    def test_assignment_with_empty_array(self):
        result = self.processor.process_output("")
        self.assertEqual(result, Cases.INVISIBLE)

    def test_function(self):
        result = self.processor.process_output("function (x) x")
        self.assertEqual(result, Cases.FUNCTION)

    def test_unknown(self):
        result = self.processor.process_output("anything")
        self.assertEqual(result, Cases.UNKNOWN)
        result = self.processor.process_output("adfasd")
        self.assertEqual(result, Cases.UNKNOWN)

    def test_vector_type_to_unknown(self):
        self.assertEqual(self.processor.process_output("integer(0)"), Cases.UNKNOWN)
        self.assertEqual(self.processor.process_output("numeric(0)"), Cases.UNKNOWN)
        self.assertEqual(self.processor.process_output("logical(0)"), Cases.UNKNOWN)
        self.assertEqual(self.processor.process_output("character(0)"), Cases.UNKNOWN)

    def test_cbind_output(self):
        self.assert_output("     [,1] [,2]\n[1,]    1    2\n[2,]    2    2\n[3,]    3    2\n", Cases.UNKNOWN)

    def test_primitive(self):
        result = self.processor.process_output('.Primitive("return")\n')
        self.assertEqual(result, Cases.FUNCTION)

        # def test_error_outputs(self):
        #     errors = ["Error in e() : could not find function \"e\"", "Error: object 'e' not found",
        #               "Error in .Primitive(cos) : string argument required"]
        #     results = self.processor.__process_sub_reports(errors)
        #
        #     self.assert_results(results, Cases.ERROR)
        #
        # def test_null_outputs(self):
        #     nulls = ['NULL', 'NULL', 'NULL', 'NULL']
        #     results = self.processor.__process_sub_reports(nulls)
        #
        #     self.assert_results(results, Cases.NULL)
        #
        # def test_function_outputs(self):
        #     functions = ['function (x) x', 'function (x, y) { x + y }', 'function() y', 'function    (     )       1']
        #     results = self.processor.__process_sub_reports(functions)
        #
        #     self.assert_results(results, Cases.FUNCTION)
