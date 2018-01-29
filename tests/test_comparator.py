from unittest import TestCase

from coqr.comparators.Comparator import Comparator
from coqr.constants.Cases import Cases
from coqr.constants.Status import Status


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
        self.assertEqual(self.comparator.compare(Cases.ERROR, Cases.UNKNOWN), Status.FAIL)
        self.assertEqual(self.comparator.compare(Cases.UNKNOWN, Cases.ERROR), Status.FAIL)

    def test_unknown(self):
        cases = [Cases.INVISIBLE, Cases.UNKNOWN, Cases.FUNCTION, '[1] TRUE', Cases.NULL, Cases.PRIMITIVE,
                 Cases.TYPE]

        for case in cases:
            self.assertEqual(self.comparator.compare(Cases.UNKNOWN, case), Status.UNKNOWN)
            self.assertEqual(self.comparator.compare(case, Cases.UNKNOWN), Status.UNKNOWN)

    def test_primitive(self):
        self.assertEqual(self.comparator.compare(Cases.PRIMITIVE, Cases.FUNCTION), Status.PASS)

    def test_boolean_output(self):
        self.assertEqual(self.comparator.compare('[1] TRUE', '[1] TRUE'), Status.PASS)
        self.assertEqual(self.comparator.compare('[1] FALSE', '[1] FALSE'), Status.PASS)
        self.assertEqual(self.comparator.compare('[1] TRUE', '[1] FALSE'), Status.FAIL)
        self.assertEqual(self.comparator.compare('[1] FALSE', '[1] TRUE'), Status.FAIL)

    def test_multiple_single_line_boolean_output(self):
        self.assertEqual(self.comparator.compare('[1] TRUE TRUE', '[1] TRUE TRUE'), Status.PASS)
        self.assertEqual(self.comparator.compare('[1] TRUE TRUE', '[1] TRUE FALSE'), Status.FAIL)
        self.assertEqual(self.comparator.compare('[1] TRUE TRUE', '[1] FALSE TRUE'), Status.FAIL)
        self.assertEqual(self.comparator.compare('[1] TRUE TRUE', '[1] FALSE FALSE'), Status.FAIL)

        self.assertEqual(self.comparator.compare('[1] FALSE FALSE', '[1] FALSE FALSE'), Status.PASS)
        self.assertEqual(self.comparator.compare('[1] FALSE FALSE', '[1] TRUE FALSE'), Status.FAIL)
        self.assertEqual(self.comparator.compare('[1] FALSE FALSE', '[1] FALSE TRUE'), Status.FAIL)
        self.assertEqual(self.comparator.compare('[1] FALSE FALSE', '[1] TRUE TRUE'), Status.FAIL)

        self.assertEqual(self.comparator.compare('[1] TRUE FALSE', '[1] TRUE TRUE'), Status.FAIL)
        self.assertEqual(self.comparator.compare('[1] TRUE FALSE', '[1] TRUE FALSE'), Status.PASS)
        self.assertEqual(self.comparator.compare('[1] TRUE FALSE', '[1] FALSE TRUE'), Status.FAIL)
        self.assertEqual(self.comparator.compare('[1] TRUE FALSE', '[1] FALSE FALSE'), Status.FAIL)

        self.assertEqual(self.comparator.compare('[1] FALSE TRUE', '[1] TRUE TRUE'), Status.FAIL)
        self.assertEqual(self.comparator.compare('[1] FALSE TRUE', '[1] TRUE FALSE'), Status.FAIL)
        self.assertEqual(self.comparator.compare('[1] FALSE TRUE', '[1] FALSE TRUE'), Status.PASS)
        self.assertEqual(self.comparator.compare('[1] FALSE TRUE', '[1] FALSE FALSE'), Status.FAIL)

    def test_boolean_without_same_format(self):
        self.assertEqual(self.comparator.compare('[1]   TRUE', '[1]    TRUE    '), Status.PASS)
        self.assertEqual(self.comparator.compare('[1] TRUE', '[1] TRUE\n'), Status.PASS)
        self.assertEqual(self.comparator.compare('[1]   TRUE', '[1]    TRUE    '), Status.PASS)
        self.assertEqual(self.comparator.compare('[1] FALSE   ', '[1] FALSE'), Status.PASS)
        self.assertEqual(self.comparator.compare('[1]   TRUE  ', '[1] FALSE'), Status.FAIL)
        self.assertEqual(self.comparator.compare('[1]   FALSE   ', '[1] TRUE\n'), Status.FAIL)

    def test_multiple_boolean_in_multiple_lines(self):
        self.assertEqual('[1] TRUE\n[2] TRUE', '[1] TRUE TRUE', Status.PASS)
        self.assertEqual('[1] TRUE\n[2] TRUE', '[1] TRUE FALSE', Status.FAIL)
        self.assertEqual('[1] TRUE\n[2] TRUE\n[3] TRUE TRUE', '[1] TRUE TRUE\n[3]   TRUE TRUE', Status.PASS)
        self.assertEqual('[1] TRUE\n[2] TRUE\n[3] TRUE TRUE', '[1] TRUE TRUE\n[3]   FALSE TRUE', Status.FAIL)


        # def test_not_implemented_followed_by_untrusted(self):
        #     coq_outputs = [{ReportKeys.OUTPUT: Cases.NOT_IMPLEMENTED}, {ReportKeys.OUTPUT: Cases.NULL},
        #                    {ReportKeys.OUTPUT: Cases.ERROR}]
        #     r_outputs = [{ReportKeys.OUTPUT: Cases.ERROR}, {ReportKeys.OUTPUT: Cases.NULL}, {ReportKeys.OUTPUT: Cases.TYPE}]
        #     results = self.comparator.compare_sub_reports(coq_outputs, r_outputs)
        #
        #     self.assertEquals(results, [Status.NOT_IMPLEMENTED, Status.UNTRUSTED_PASS, Status.UNTRUSTED_FAIL])
        #
        # def test_fail_followed_by_untrusted(self):
        #     coq_outputs = [Cases.NULL, Cases.NULL, Cases.ERROR]
        #     r_outputs = [Cases.ERROR, Cases.NULL, Cases.TYPE]
        #     results = self.comparator.compare_sub_reports(coq_outputs, r_outputs)
        #
        #     self.assertEquals(results, [Status.FAIL, Status.UNTRUSTED_PASS, Status.UNTRUSTED_FAIL])
        #
        # def test_impossible_followed_by_untrusted(self):
        #     coq_outputs = [Cases.IMPOSSIBLE, Cases.NULL, Cases.ERROR]
        #     r_outputs = [Cases.ERROR, Cases.NULL, Cases.TYPE]
        #     results = self.comparator.compare_sub_reports(coq_outputs, r_outputs)
        #
        #     self.assertEquals(results, [Status.IMPOSSIBLE, Status.UNTRUSTED_PASS, Status.UNTRUSTED_FAIL])
        #
        # def test_no_untrusted(self):
        #     coq_outputs = [Cases.ERROR, Cases.NULL, Cases.ERROR, Cases.NOT_IMPLEMENTED]
        #     r_outputs = [Cases.ERROR, Cases.NULL, Cases.TYPE, Cases.PRIMITIVE]
        #     results = self.comparator.compare_sub_reports(coq_outputs, r_outputs)
        #
        #     self.assertEquals(results, [Status.PASS, Status.PASS, Status.FAIL, Status.NOT_IMPLEMENTED])
        #
        # def test_not_implemented_in_between_followed_by_untrusted(self):
        #     coq_outputs = [Cases.ERROR, Cases.NULL, Cases.NOT_IMPLEMENTED, Cases.ERROR, Cases.FUNCTION]
        #     r_outputs = [Cases.ERROR, Cases.NULL, Cases.TYPE, Cases.ERROR, Cases.PRIMITIVE]
        #     results = self.comparator.compare_sub_reports(coq_outputs, r_outputs)
        #
        #     self.assertEquals(results, [Status.PASS, Status.PASS, Status.NOT_IMPLEMENTED, Status.UNTRUSTED_PASS,
        #                                 Status.UNTRUSTED_FAIL])
        #
        # def test_fail_in_between_followed_by_untrusted(self):
        #     coq_outputs = [Cases.ERROR, Cases.NULL, Cases.NULL, Cases.ERROR, Cases.FUNCTION]
        #     r_outputs = [Cases.ERROR, Cases.NULL, Cases.TYPE, Cases.ERROR, Cases.PRIMITIVE]
        #     results = self.comparator.compare_sub_reports(coq_outputs, r_outputs)
        #
        #     self.assertEquals(results,
        #                       [Status.PASS, Status.PASS, Status.FAIL, Status.UNTRUSTED_PASS, Status.UNTRUSTED_FAIL])
        #
        # def test_impossible_in_between_followed_by_untrusted(self):
        #     coq_outputs = [Cases.ERROR, Cases.NULL, Cases.IMPOSSIBLE, Cases.ERROR, Cases.FUNCTION]
        #     r_outputs = [Cases.ERROR, Cases.NULL, Cases.TYPE, Cases.ERROR, Cases.PRIMITIVE]
        #     results = self.comparator.compare_sub_reports(coq_outputs, r_outputs)
        #
        #     self.assertEquals(results,
        #                       [Status.PASS, Status.PASS, Status.IMPOSSIBLE, Status.UNTRUSTED_PASS, Status.UNTRUSTED_FAIL])
