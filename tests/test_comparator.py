from unittest import TestCase

from rcoq.Constants import SUCCESSFUL, CASE_NOT_IMPLEMENTED, CASE_ERROR, CASE_INVISIBLE, SEQ_TOKEN, \
    CASE_IMPOSSIBLE, UNSUCCESSFUL, CASE_UNKNOWN, NULL, CASE_FUNCTION
from rcoq.comparators.Comparator import compare


class TestComparator(TestCase):
    def test_not_implemented(self):
        cases = [CASE_ERROR, CASE_INVISIBLE, CASE_UNKNOWN, CASE_FUNCTION, '[1] TRUE', NULL]

        for case in cases:
            self.assertEqual(compare(CASE_NOT_IMPLEMENTED, case), CASE_NOT_IMPLEMENTED)

    def test_impossible(self):
        cases = [CASE_ERROR, CASE_INVISIBLE, CASE_UNKNOWN, CASE_FUNCTION, '[1] TRUE', NULL]

        for case in cases:
            self.assertEqual(compare(CASE_IMPOSSIBLE, case), CASE_IMPOSSIBLE)

    def test_error(self):
        cases = [CASE_INVISIBLE, CASE_FUNCTION, '[1] TRUE', NULL]

        for case in cases:
            self.assertEqual(compare(CASE_ERROR, case), UNSUCCESSFUL)

        self.assertEqual(compare(CASE_ERROR, CASE_ERROR), SUCCESSFUL)
        self.assertEqual(compare(CASE_ERROR, CASE_UNKNOWN), CASE_UNKNOWN)

    def test_unknown(self):
        cases = [CASE_ERROR, CASE_INVISIBLE, CASE_UNKNOWN, CASE_FUNCTION, '[1] TRUE', NULL]

        for case in cases:
            self.assertEqual(compare(CASE_UNKNOWN, case), CASE_UNKNOWN)
            self.assertEqual(compare(case, CASE_UNKNOWN), CASE_UNKNOWN)
