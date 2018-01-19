from unittest import TestCase

import re

from coqr.constants.Cases import Cases
from coqr.processors.ROutputProcessor import ROutputProcessor


class TestROutputProcessor(TestCase):
    def setUp(self):
        self.processor = ROutputProcessor()

    def assert_results(self, results, expected_case):
        for result in results:
            self.assertEqual(result, expected_case)

    def test_process_2(self):
        result = self.processor.process_output("[1] 2\n")
        self.assertEqual(result, '[1] 2')

    def test_process_TRUE(self):
        result = self.processor.process_output("[1] TRUE\n")
        self.assertEqual(result, "[1] TRUE")

    def test_process_FALSE(self):
        result = self.processor.process_output("[1] FALSE\n")
        self.assertEqual(result, "[1] FALSE")

    def test_process_NA(self):
        result = self.processor.process_output("[1] NA\n")
        self.assertEqual(result, "[1] NA")

    def test_process_NaN(self):
        result = self.processor.process_output("[1] NaN\n")
        self.assertEqual(result, "[1] NaN")

    def test_process_Inf(self):
        result = self.processor.process_output("[1] Inf\n")
        self.assertEqual(result, "[1] Inf")
        result = self.processor.process_output("[1] -Inf\n")
        self.assertEqual(result, "[1] -Inf")

    def test_process_ignore_warning(self):
        result = self.processor.process_output("[1] NaN\nWarning message:\nIn sqrt(-16) : NaNs produced")
        self.assertEqual(result, "[1] NaN")

    def test_process_string(self):
        result = self.processor.process_output(
            "> Success.\n(closure)\n> Success.\n[1] \" + input + \"\n> Success.\n[1] \" + input + \"\n> ")
        self.assertEqual(result, "[1] \"  [1] \" ")

    def test_process_NULL(self):
        result = self.processor.process_output("NULL\n")
        self.assertEqual(result, Cases.NULL)

    #
    def test_process_error_object(self):
        result = self.processor.process_output("Error: object 'e' not found")
        self.assertEqual(result, Cases.ERROR)

    def test_process_error_function(self):
        result = self.processor.process_output(
            "Error in e() : could not find function \"e\"")
        self.assertEqual(result, Cases.ERROR)

    def test_vector_output(self):
        result = self.processor.process_output("[1] 1 2 3\n[4] 5 6 7\n")
        self.assertEqual(result, "[1] 1 2 3 [4] 5 6 7")

    def test_vector_double_bracket(self):
        output = "[[1]]\n[[1]]$input\n[1]  TRUE FALSE\n\n[[1]]$any\n[1] TRUE\n\n[[1]]$all\n[1] FALSE\n\n\n[[2]]\n"
        result = self.processor.process_output(output)
        self.assertEqual(result, "[[1]] [[1]]$input [1]  TRUE FALSE [[1]]$any [1] TRUE [[1]]$all [1] FALSE [[2]]")

    def test_vector_double_bracket_2(self):
        output = "[[2]]$input\n[[2]]$input[[1]]\n[1] FALSE\n\n"
        result = self.processor.process_output(output)
        self.assertEqual(result, "[[2]]$input [[2]]$input[[1]] [1] FALSE")

    def test_vector_with_decimals(self):
        output = "[1] 2.4259 3.4293 3.9896 5.2832 5.3386 4.9822\n"
        result = self.processor.process_output(output)
        self.assertEqual(result, "[1] 2.4259 3.4293 3.9896 5.2832 5.3386 4.9822")

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

    def test_vector_type(self):
        self.assertEqual(self.processor.process_output("integer(0)"), Cases.TYPE)
        self.assertEqual(self.processor.process_output("numeric(0)"), Cases.TYPE)
        self.assertEqual(self.processor.process_output("logical(0)"), Cases.TYPE)
        self.assertEqual(self.processor.process_output("character(0)"), Cases.TYPE)

    def test_cbind_output(self):
        result = self.processor.process_output("     [,1] [,2]\n[1,]    1    2\n[2,]    2    2\n[3,]    3    2\n")
        self.assertEqual(result, "[,1] [,2] [1,]    1    2 [2,]    2    2 [3,]    3    2")

    def test_primitive(self):
        result = self.processor.process_output('.Primitive("return")\n')
        self.assertEqual(result, Cases.PRIMITIVE)

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
