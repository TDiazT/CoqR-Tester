from unittest import TestCase

from Comparator.Comparator import Comparator
from Comparator.Constants import SUCCESSFUL, CASE_NOT_IMPLEMENTED, CASE_ERROR, CASE_INVISIBLE, SEQ_TOKEN


class TestComparator(TestCase):
    def setUp(self):
        self.comparator = Comparator()

    def test_case_not_implemented(self):
        self.assertEqual(self.comparator.compare_multiple([CASE_NOT_IMPLEMENTED], [CASE_ERROR]), [CASE_NOT_IMPLEMENTED])
        self.assertEqual(self.comparator.compare_multiple([CASE_NOT_IMPLEMENTED], [CASE_INVISIBLE]),
                         [CASE_NOT_IMPLEMENTED])
        self.assertEqual(self.comparator.compare_multiple([CASE_NOT_IMPLEMENTED], [['[1]', "TRUE"]]),
                         [CASE_NOT_IMPLEMENTED])
        self.assertEqual(self.comparator.compare_multiple([CASE_NOT_IMPLEMENTED], [['[1]', '1', '[2]', '4']]),
                         [CASE_NOT_IMPLEMENTED])

    def test_simple_token(self):
        self.assertEqual(self.comparator.compare_multiple([SEQ_TOKEN], [SEQ_TOKEN]), [])

    def test_assignment_with_tokens(self):
        coq = [SEQ_TOKEN, ['[1]', '1'], SEQ_TOKEN]
        r = [SEQ_TOKEN, SEQ_TOKEN]
        self.assertEqual(self.comparator.compare_multiple(coq, r), [SUCCESSFUL])
