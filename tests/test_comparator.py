from unittest import TestCase

from rcoq.Cases import Cases
from rcoq.comparators.Comparator import compare


class TestComparator(TestCase):
    def test_not_implemented(self):
        cases = [str(Cases.ERROR), str(Cases.INVISIBLE), str(Cases.UNKNOWN), str(Cases.FUNCTION), '[1] TRUE', str(Cases.NULL)]

        for case in cases:
            self.assertEqual(compare(str(Cases.NOT_IMPLEMENTED), case), str(Cases.NOT_IMPLEMENTED))

    def test_impossible(self):
        cases = [str(Cases.ERROR), str(Cases.INVISIBLE), str(Cases.UNKNOWN), str(Cases.FUNCTION), '[1] TRUE', str(Cases.NULL)]

        for case in cases:
            self.assertEqual(compare(str(Cases.IMPOSSIBLE), case), str(Cases.IMPOSSIBLE))

    def test_error(self):
        cases = [str(Cases.INVISIBLE), str(Cases.FUNCTION), '[1] TRUE', str(Cases.NULL)]

        for case in cases:
            self.assertEqual(compare(str(Cases.ERROR), case), str(Cases.UNSUCCESSFUL))

        self.assertEqual(compare(str(Cases.ERROR), str(Cases.ERROR)), str(Cases.SUCCESSFUL))
        self.assertEqual(compare(str(Cases.ERROR), str(Cases.UNKNOWN)), str(Cases.UNKNOWN))

    def test_unknown(self):
        cases = [str(Cases.ERROR), str(Cases.INVISIBLE), str(Cases.UNKNOWN), str(Cases.FUNCTION), '[1] TRUE', str(Cases.NULL)]

        for case in cases:
            self.assertEqual(compare(str(Cases.UNKNOWN), case), str(Cases.UNKNOWN))
            self.assertEqual(compare(case, str(Cases.UNKNOWN)), str(Cases.UNKNOWN))
