from unittest import TestCase

from coqr.constants.Cases import Cases
from coqr.processors.CoqOutputProcessor import CoqOutputProcessor


class TestCoqOutputProcessor(TestCase):
    def setUp(self):
        self.processor = CoqOutputProcessor()

    def assert_results(self, results, expected_case):
        for result in results:
            self.assertEqual(result, expected_case)

    def test_process_2(self):
        result = self.processor.process_output("Success.\n[1] 2\n")
        self.assertEqual(result, '[1] 2')

    def test_process_TRUE(self):
        result = self.processor.process_output("Success.\n[1] TRUE\n")
        self.assertEqual(result, '[1] TRUE')

    def test_process_FALSE(self):
        result = self.processor.process_output("Success.\n[1] FALSE\n")
        self.assertEqual(result, '[1] FALSE')

    def test_process_NA(self):
        result = self.processor.process_output("Success.\n[1] NA\n")
        self.assertEqual(result, '[1] NA')

    def test_process_NaN(self):
        result = self.processor.process_output("Success.\n[1] NaN\n")
        self.assertEqual(result, '[1] NaN')

    def test_process_Inf(self):
        result = self.processor.process_output("[1] Inf\n")
        self.assertEqual(result, "[1] Inf")
        result = self.processor.process_output("[1] -Inf\n")
        self.assertEqual(result, "[1] -Inf")

    def test_process_string(self):
        result = self.processor.process_output(
            "> Success.\n(closure)\n> Success.\n[1] \" + input + \"\n> Success.\n[1] \" + input + \"\n> ")
        self.assertEqual(result, "[1] \"  [1] \" ")

    def test_process_NULL(self):
        result = self.processor.process_output("Success.\nNULL\n")
        self.assertEqual(result, Cases.NULL)

    def test_process_error_object(self):
        result = self.processor.process_output("> Error: [eval] Object not found.\nAn error lead to an undefined result.\n")
        self.assertEqual(result, Cases.ERROR)

    def test_process_error_function(self):
        result = self.processor.process_output(
            "> Error: [findFun3] Could not find function “e”.\nAn error lead to an undefined result.\n")
        self.assertEqual(result, Cases.ERROR)

    def test_vector_output(self):
        result = self.processor.process_output("Success.\n[1] 1 2 3\n[4] 5 6 7\n")
        self.assertEqual(result, '[1] 1 2 3 [4] 5 6 7')

    def test_vector_double_bracket(self):
        output = "[[1]]\n[[1]]$input\n[1]  TRUE FALSE\n\n[[1]]$any\n[1] TRUE\n\n[[1]]$all\n[1] FALSE\n\n\n[[2]]\n"
        result = self.processor.process_output(output)
        self.assertEqual(result, "[[1]] [[1]]$input [1]  TRUE FALSE [[1]]$any [1] TRUE [[1]]$all [1] FALSE [[2]]")

    def test_vector_double_bracket_2(self):
        output = "[[2]]$input\n[[2]]$input[[1]]\n[1] FALSE\n\n"
        result = self.processor.process_output(output)
        self.assertEqual(result, "[[2]]$input [[2]]$input[[1]] [1] FALSE")

    def test_assignment_with_empty_array(self):
        result = self.processor.process_output("")
        self.assertEqual(result, Cases.INVISIBLE)

    def test_function(self):
        result = self.processor.process_output("Success.\n(closure)\n")
        self.assertEqual(result, Cases.FUNCTION)

    def test_unknown(self):
        result = self.processor.process_output("anything")
        self.assertEqual(result, Cases.UNKNOWN)
        result = self.processor.process_output("adfasd")
        self.assertEqual(result, Cases.UNKNOWN)
        result = self.processor.process_output("[,1]")
        self.assertEqual(result, Cases.UNKNOWN)

    # def test_error_outputs(self):
    #     errors = ["Error in e() : could not find function \"e\"", "Error: object 'e' not found",
    #               "Error in .Primitive(cos) : string argument required"]
    #     results = self.processor.__process_rub_reports(errors)
    #
    #     self.assert_results(results, Cases.ERROR)
    #
    # def test_null_outputs(self):
    #     nulls = ['NULL', 'NULL', 'NULL', 'NULL']
    #     results = self.processor.__process_rub_reports(nulls)
    #
    #     self.assert_results(results, Cases.NULL)
    #
    # def test_function_outputs(self):
    #     functions = ['(closure)', '(closure)', '(closure)', '(closure)']
    #     results = self.processor.__process_rub_reports(functions)
    #
    #     self.assert_results(results, Cases.FUNCTION)
