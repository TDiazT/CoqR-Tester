from unittest import TestCase

from coqr.comparators.Comparator import Comparator


class TestComparator(TestCase):
    def setUp(self):
        self.comparator = Comparator()

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
