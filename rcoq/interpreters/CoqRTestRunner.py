from Comparator.CoqRunner import CoqRunner
from Comparator.ROutputProcessor import ROutputProcessor

from rcoq.comparators.Comparator import Comparator
from rcoq.processors.CoqOutputProcessor import CoqOutputProcessor
from rcoq.interpreters.RInterpreter import RInterpreter


class CoqRTestRunner:

    def test_expression(self, expression):
        return Comparator().compare_multiple(CoqOutputProcessor().process(CoqRunner().run_expression(expression)),
                                             ROutputProcessor().process(RInterpreter().run_expression(expression)))
