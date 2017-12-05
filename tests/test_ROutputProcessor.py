from unittest import TestCase

from rcoq.Cases import Cases
from rcoq.processors.ROutputProcessor import ROutputProcessor


class TestROutputProcessor(TestCase):
    def setUp(self):
        self.processor = ROutputProcessor()

    def test_process_2(self):
        result = self.processor.process("[1] 2\n")
        self.assertEqual(result, '[1] 2')

    def test_process_TRUE(self):
        result = self.processor.process("[1] TRUE\n")
        self.assertEqual(result, "[1] TRUE")

    def test_process_FALSE(self):
        result = self.processor.process("[1] FALSE\n")
        self.assertEqual(result, "[1] FALSE")

    def test_process_NA(self):
        result = self.processor.process("[1] NA\n")
        self.assertEqual(result, "[1] NA")

    def test_process_NaN(self):
        result = self.processor.process("[1] NaN\n")
        self.assertEqual(result, "[1] NaN")

    def test_process_Inf(self):
        result = self.processor.process("[1] Inf\n")
        self.assertEqual(result, "[1] Inf")
        result = self.processor.process("[1] -Inf\n")
        self.assertEqual(result, "[1] -Inf")

    def test_process_ignore_warning(self):
        result = self.processor.process("[1] NaN\nWarning message:\nIn sqrt(-16) : NaNs produced")
        self.assertEqual(result, "[1] NaN")

    def test_process_NULL(self):
        result = self.processor.process("NULL\n")
        self.assertEqual(result, Cases.NULL)

    #
    def test_process_error_object(self):
        result = self.processor.process("Error: object 'e' not found")
        self.assertEqual(result, Cases.ERROR)

    def test_process_error_function(self):
        result = self.processor.process(
            "Error in e() : could not find function \"e\"")
        self.assertEqual(result, Cases.ERROR)

    def test_vector_output(self):
        result = self.processor.process("[1] 1 2 3\n[4] 5 6 7\n")
        self.assertEqual(result, "[1] 1 2 3 [4] 5 6 7")

    def test_assignment_with_empty_array(self):
        result = self.processor.process("")
        self.assertEqual(result, Cases.INVISIBLE)

    def test_function(self):
        result = self.processor.process("function (x) x")
        self.assertEqual(result, Cases.FUNCTION)

    def test_unknown(self):
        result = self.processor.process("anything")
        self.assertEqual(result, Cases.UNKNOWN)
        result = self.processor.process("adfasd")
        self.assertEqual(result, Cases.UNKNOWN)

    def test_vector_type(self):
        self.assertEqual(self.processor.process("integer(0)"), Cases.TYPE)
        self.assertEqual(self.processor.process("numeric(0)"), Cases.TYPE)
        self.assertEqual(self.processor.process("logical(0)"), Cases.TYPE)
        self.assertEqual(self.processor.process("character(0)"), Cases.TYPE)

    def test_cbind_output(self):
        result = self.processor.process("     [,1] [,2]\n[1,]    1    2\n[2,]    2    2\n[3,]    3    2\n")
        self.assertEqual(result, "[,1] [,2] [1,]    1    2 [2,]    2    2 [3,]    3    2")
