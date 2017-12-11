from unittest import TestCase

from rcoq.comparators.Comparator import compare
from rcoq.constants.Status import Status
from rcoq.constants.Cases import Cases


class TestComparator(TestCase):
    def test_not_implemented(self):
        cases = [Cases.ERROR, Cases.INVISIBLE, Cases.UNKNOWN, Cases.FUNCTION, '[1] TRUE', Cases.NULL]

        for case in cases:
            self.assertEqual(compare(Cases.NOT_IMPLEMENTED, case), Status.NOT_IMPLEMENTED)

    def test_impossible(self):
        cases = [Cases.ERROR, Cases.INVISIBLE, Cases.UNKNOWN, Cases.FUNCTION, '[1] TRUE', Cases.NULL]

        for case in cases:
            self.assertEqual(compare(Cases.IMPOSSIBLE, case), Status.IMPOSSIBLE)

    def test_error(self):
        cases = [Cases.INVISIBLE, Cases.FUNCTION, '[1] TRUE', Cases.NULL]

        for case in cases:
            self.assertEqual(compare(Cases.ERROR, case), Status.FAIL)

        self.assertEqual(compare(Cases.ERROR, Cases.ERROR), Status.PASS)
        self.assertEqual(compare(Cases.ERROR, Cases.UNKNOWN), Status.UNKNOWN)

    def test_unknown(self):
        cases = [Cases.ERROR, Cases.INVISIBLE, Cases.UNKNOWN, Cases.FUNCTION, '[1] TRUE', Cases.NULL]

        for case in cases:
            self.assertEqual(compare(Cases.UNKNOWN, case), Status.UNKNOWN)
            self.assertEqual(compare(case, Cases.UNKNOWN), Status.UNKNOWN)
