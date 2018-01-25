from unittest import TestCase

from coqr.constants.Cases import Cases
from coqr.processors.CoqOutputProcessor import CoqOutputProcessor
from tests.processors.test_processor import TestCommonProcessor


class TestCoqOutputProcessor(TestCase, TestCommonProcessor):
    def setUp(self):
        self.processor = CoqOutputProcessor()

    def assert_results(self, results, expected_case):
        for result in results:
            self.assertEqual(result, expected_case)

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

    def test_not_implemented(self):
        output = "> Not implemented: [do_c]\nAn error lead to an undefined state. Continuing using the old one.\n" \
                 "An error lead to an undefined result.\n> "
        result = self.processor.process_output(output)
        self.assertEqual(result, Cases.NOT_IMPLEMENTED)

    def test_parse_error_over_not_implemented(self):
        output = "> Error: Parser error at offset 2133.\n> Error: [findFun3] Could not find function \u201cf\u201d.\n" \
                 "An error lead to an undefined result.\n> Error: Parser error at offset 2166.\n" \
                 "> > > (closure)\n> Error: [findFun3] Could not find function \u201cdeparse\u201d.\n" \
                 "An error lead to an undefined result.\n" \
                 "> Not implemented: [do_for]\nAn error lead to an undefined state. Continuing using the old one.\n" \
                 "An error lead to an undefined result."
        result = self.processor.process_output(output)
        self.assertEquals(result, Cases.ERROR)

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
