from unittest import TestCase

from Comparator.Comparator import Comparator
from Comparator.Constants import SUCCESSFUL, CASE_NOT_IMPLEMENTED, CASE_ERROR


class TestComparator(TestCase):
    def setUp(self):
        self.comparator = Comparator()

    def test_case_not_implemented(self):
        result = self.comparator.compare_multiple([CASE_NOT_IMPLEMENTED], [CASE_ERROR])
        self.assertEqual(result, [CASE_NOT_IMPLEMENTED])
