from unittest import TestCase

from rcoq.Constants import NULL, CASE_ERROR, SEQ_TOKEN
from rcoq.processors.CoqOutputProcessor import CoqOutputProcessor


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

    def test_vector_output(self):
        result = self.processor.process("[1] 1 2 3\n[4] 5 6 7\n")
        self.assertEqual(result, [['[1]', '1', '2', '3', '[4]', '5', '6', '7']])

    def test_single_token(self):
        result = self.processor.process("[1] \"%s\"" % SEQ_TOKEN)
        self.assertEqual(result, [SEQ_TOKEN])

    def test_multiple_tokens(self):
        result = self.processor.process("[1] \"%s\"\n[1] \"%s\"\n[1] \"%s\"" % (SEQ_TOKEN, SEQ_TOKEN, SEQ_TOKEN))
        self.assertEqual(result, [SEQ_TOKEN, SEQ_TOKEN, SEQ_TOKEN])

    def test_multiple_outputs(self):
        output = "[1] \"%s\"\n(%s)\n%s\n%s\n%s\n[1] \"%s\"\n[1] \"%s\"\n%s" % (SEQ_TOKEN, NULL, "[1] 1 2 3",
                                                                               "Error: [findFun3] Could not find function “e”.",
                                                                               "An error lead to an undefined result.",
                                                                               SEQ_TOKEN,
                                                                               SEQ_TOKEN,
                                                                               "[1] TRUE")
        result = self.processor.process(output)
        self.assertEqual(result,
                         [SEQ_TOKEN, NULL, ['[1]', '1', '2', '3'], CASE_ERROR, SEQ_TOKEN, SEQ_TOKEN, ['[1]', 'TRUE']])
