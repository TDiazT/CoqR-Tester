from unittest import TestCase

from rcoq.Cases import Cases
from rcoq.comparators.Comparator import compare


class TestComparator(TestCase):
    def test_not_implemented(self):
        cases = [Cases.ERROR, Cases.INVISIBLE, Cases.UNKNOWN, Cases.FUNCTION, '[1] TRUE', Cases.NULL]

        for case in cases:
            self.assertEqual(compare(Cases.NOT_IMPLEMENTED, case), Cases.NOT_IMPLEMENTED)

    def test_impossible(self):
        cases = [Cases.ERROR, Cases.INVISIBLE, Cases.UNKNOWN, Cases.FUNCTION, '[1] TRUE', Cases.NULL]

        for case in cases:
            self.assertEqual(compare(Cases.IMPOSSIBLE, case), Cases.IMPOSSIBLE)

    def test_error(self):
        cases = [Cases.INVISIBLE, Cases.FUNCTION, '[1] TRUE', Cases.NULL]

        for case in cases:
            self.assertEqual(compare(Cases.ERROR, case), Cases.FAIL)

        self.assertEqual(compare(Cases.ERROR, Cases.ERROR), Cases.PASS)
        self.assertEqual(compare(Cases.ERROR, Cases.UNKNOWN), Cases.UNKNOWN)

    def test_unknown(self):
        cases = [Cases.ERROR, Cases.INVISIBLE, Cases.UNKNOWN, Cases.FUNCTION, '[1] TRUE', Cases.NULL]

        for case in cases:
            self.assertEqual(compare(Cases.UNKNOWN, case), Cases.UNKNOWN)
            self.assertEqual(compare(case, Cases.UNKNOWN), Cases.UNKNOWN)
