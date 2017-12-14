from unittest import TestCase

from rcoq.comparators.Comparator import Comparator
from rcoq.constants.Status import Status
from rcoq.constants.Cases import Cases


class TestComparator(TestCase):

    def setUp(self):
        self.comparator = Comparator()

    def test_not_implemented(self):
        for case in Cases:
            self.assertEqual(self.comparator.compare(Cases.NOT_IMPLEMENTED, case), Status.NOT_IMPLEMENTED)

    def test_impossible(self):
        cases = [Cases.IMPOSSIBLE, Cases.ERROR, Cases.INVISIBLE, Cases.UNKNOWN, Cases.FUNCTION, '[1] TRUE', Cases.NULL]

        for case in cases:
            self.assertEqual(self.comparator.compare(Cases.IMPOSSIBLE, case), Status.IMPOSSIBLE)

    def test_error(self):
        cases = [Cases.INVISIBLE, Cases.FUNCTION, '[1] TRUE', Cases.NULL, Cases.PRIMITIVE, Cases.TYPE]

        for case in cases:
            self.assertEqual(self.comparator.compare(Cases.ERROR, case), Status.FAIL)

        self.assertEqual(self.comparator.compare(Cases.ERROR, Cases.ERROR), Status.PASS)
        self.assertEqual(self.comparator.compare(Cases.ERROR, Cases.UNKNOWN), Status.UNKNOWN)

    def test_unknown(self):
        cases = [Cases.ERROR, Cases.INVISIBLE, Cases.UNKNOWN, Cases.FUNCTION, '[1] TRUE', Cases.NULL, Cases.PRIMITIVE, Cases.TYPE]

        for case in cases:
            self.assertEqual(self.comparator.compare(Cases.UNKNOWN, case), Status.UNKNOWN)
            self.assertEqual(self.comparator.compare(case, Cases.UNKNOWN), Status.UNKNOWN)
