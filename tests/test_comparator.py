from unittest import TestCase

from Comparator.Comparator import Comparator
from Comparator.Constants import SUCCESSFUL, CASE_NOT_IMPLEMENTED, CASE_ERROR, CASE_ASSIGNMENT


class TestComparator(TestCase):
    def setUp(self):
        self.comparator = Comparator()

    def test_case_not_implemented(self):
        self.assertEqual(self.comparator.compare_multiple([CASE_NOT_IMPLEMENTED], [CASE_ERROR]), [CASE_NOT_IMPLEMENTED])
        self.assertEqual(self.comparator.compare_multiple([CASE_NOT_IMPLEMENTED], [CASE_ASSIGNMENT]),
                         [CASE_NOT_IMPLEMENTED])
        self.assertEqual(self.comparator.compare_multiple([CASE_NOT_IMPLEMENTED], [['[1]', "TRUE"]]),
                         [CASE_NOT_IMPLEMENTED])
        self.assertEqual(self.comparator.compare_multiple([CASE_NOT_IMPLEMENTED], [['[1]', '1', '[2]', '4']]),
                         [CASE_NOT_IMPLEMENTED])
