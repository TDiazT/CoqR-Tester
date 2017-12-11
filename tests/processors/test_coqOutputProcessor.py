from unittest import TestCase

from rcoq.constants.Cases import Cases
from rcoq.processors.CoqOutputProcessor import CoqOutputProcessor


class TestCoqOutputProcessor(TestCase):
    def setUp(self):
        self.processor = CoqOutputProcessor()

    def test_process_2(self):
        result = self.processor.process("Success.\n[1] 2\n")
        self.assertEqual(result, '[1] 2')

    def test_process_TRUE(self):
        result = self.processor.process("Success.\n[1] TRUE\n")
        self.assertEqual(result, '[1] TRUE')

    def test_process_FALSE(self):
        result = self.processor.process("Success.\n[1] FALSE\n")
        self.assertEqual(result, '[1] FALSE')

    def test_process_NA(self):
        result = self.processor.process("Success.\n[1] NA\n")
        self.assertEqual(result, '[1] NA')

    def test_process_NaN(self):
        result = self.processor.process("Success.\n[1] NaN\n")
        self.assertEqual(result, '[1] NaN')

    def test_process_Inf(self):
        result = self.processor.process("[1] Inf\n")
        self.assertEqual(result, "[1] Inf")
        result = self.processor.process("[1] -Inf\n")
        self.assertEqual(result, "[1] -Inf")

    def test_process_string(self):
        result = self.processor.process(
            "> Success.\n(closure)\n> Success.\n[1] \" + input + \"\n> Success.\n[1] \" + input + \"\n> ")
        self.assertEqual(result, "[1] \"  [1] \" ")

    def test_process_NULL(self):
        result = self.processor.process("Success.\nNULL\n")
        self.assertEqual(result, Cases.NULL)

    def test_process_error_object(self):
        result = self.processor.process("> Error: [eval] Object not found.\nAn error lead to an undefined result.\n")
        self.assertEqual(result, Cases.ERROR)

    def test_process_error_function(self):
        result = self.processor.process(
            "> Error: [findFun3] Could not find function “e”.\nAn error lead to an undefined result.\n")
        self.assertEqual(result, Cases.ERROR)

    def test_vector_output(self):
        result = self.processor.process("Success.\n[1] 1 2 3\n[4] 5 6 7\n")
        self.assertEqual(result, '[1] 1 2 3 [4] 5 6 7')

    def test_assignment_with_empty_array(self):
        result = self.processor.process("")
        self.assertEqual(result, Cases.INVISIBLE)

    def test_function(self):
        result = self.processor.process("Success.\n(closure)\n")
        self.assertEqual(result, Cases.FUNCTION)

    def test_unknown(self):
        result = self.processor.process("anything")
        self.assertEqual(result, Cases.UNKNOWN)
        result = self.processor.process("adfasd")
        self.assertEqual(result, Cases.UNKNOWN)
        result = self.processor.process("[,1]")
        self.assertEqual(result, Cases.UNKNOWN)
