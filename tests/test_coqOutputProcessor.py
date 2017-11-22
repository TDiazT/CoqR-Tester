from unittest import TestCase

from Comparator.CoqOutputProcessor import CoqOutputProcessor, CASE_ERROR, NULL


class TestCoqOutputProcessor(TestCase):
    def setUp(self):
        self.processor = CoqOutputProcessor()

    def test_process_2(self):
        result = self.processor.process("[1] 2\n")
        self.assertEqual(result, [['[1]', '2']])

    def test_process_TRUE(self):
        result = self.processor.process("[1] TRUE\n")
        self.assertEqual(result, [['[1]', 'TRUE']])

    def test_process_FALSE(self):
        result = self.processor.process("[1] FALSE\n")
        self.assertEqual(result, [['[1]', 'FALSE']])

    def test_process_NA(self):
        result = self.processor.process("[1] NA\n")
        self.assertEqual(result, [['[1]', 'NA']])

    def test_process_NaN(self):
        result = self.processor.process("[1] NaN\n")
        self.assertEqual(result, [['[1]', 'NaN']])

    def test_process_NULL(self):
        result = self.processor.process("(NULL)\n")
        self.assertEqual(result, [NULL])

    def test_process_error_object(self):
        result = self.processor.process("> Error: [eval] Object not found.\nAn error lead to an undefined result.\n")
        self.assertEqual(result, [CASE_ERROR])

    def test_process_error_function(self):
        result = self.processor.process(
            "> Error: [findFun3] Could not find function “e”.\nAn error lead to an undefined result.\n")
        self.assertEqual(result, [CASE_ERROR])
