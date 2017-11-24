from Comparator.Comparator import Comparator
from Comparator.CoqOutputProcessor import CoqOutputProcessor
from Comparator.CoqRunner import CoqRunner
from Comparator.ROutputProcessor import ROutputProcessor
from Comparator.RRunner import RRunner


class CoqRTestRunner:

    def test_expression(self, expression):
        return Comparator().compare_multiple(CoqOutputProcessor().process(CoqRunner().run_expression(expression)),
                                             ROutputProcessor().process(RRunner().run_expression(expression)))
