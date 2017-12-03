from Comparator.CoqRunner import CoqRunner
from Comparator.ROutputProcessor import ROutputProcessor

from rcoq.comparators.Comparator import Comparator
from rcoq.processors.CoqOutputProcessor import CoqOutputProcessor
from rcoq.runners.RRunner import RRunner


class CoqRTestRunner:

    def test_expression(self, expression):
        return Comparator().compare_multiple(CoqOutputProcessor().process(CoqRunner().run_expression(expression)),
                                             ROutputProcessor().process(RRunner().run_expression(expression)))
