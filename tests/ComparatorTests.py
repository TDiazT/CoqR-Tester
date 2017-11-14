import unittest
from Comparator import compare_outputs_for


class ComparatorTest(unittest.TestCase):
    def test_output_from_2(self):
        result = compare_outputs_for("2")
        self.assertEqual(result, "OK")

    def test_object_not_found_error(self):
        result = compare_outputs_for("e")
        self.assertEqual(result, "OK")
