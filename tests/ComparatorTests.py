import unittest
from Comparator import compare_outputs_for, CASE_NOT_IMPLEMENTED, SEQ_TOKEN


class ComparatorTest(unittest.TestCase):
    def test_output_from_2(self):
        result = compare_outputs_for("2")
        self.assertEqual(result, ["OK"])

    def test_output_from_TRUE(self):
        result = compare_outputs_for("TRUE")
        self.assertEqual(result, ["OK"])

    def test_output_from_FALSE(self):
        result = compare_outputs_for("FALSE")
        self.assertEqual(result, ["OK"])

    def test_output_from_NA(self):
        result = compare_outputs_for("NA")
        self.assertEqual(result, ["OK"])

    def test_output_from_NaN(self):
        result = compare_outputs_for("NaN")
        self.assertEqual(result, ["OK"])

    def test_output_from_NULL(self):
        result = compare_outputs_for("NULL")
        self.assertEqual(result, ["OK"])

    def test_object_not_found_error(self):
        result = compare_outputs_for("e")
        self.assertEqual(result, ["OK"])

    def test_not_implemented(self):
        result = compare_outputs_for("1:10")
        self.assertEqual(result, [CASE_NOT_IMPLEMENTED])

    def test_no_output(self):
        result = compare_outputs_for("a <- 1")
        self.assertEqual(result, ["OK"])

    def test_double_assignment(self):
        result = compare_outputs_for("a <- 1; '%s' ; b <- 3" % SEQ_TOKEN)
        self.assertEqual(result, ["OK"])
