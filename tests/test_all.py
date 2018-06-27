from unittest import TestCase

import os

from coqr.comparators.Comparator import Comparator
from coqr.constants.Status import Status
from coqr.interpreters.CoqInterpreter import CoqInterpreter
from coqr.interpreters.RInterpreter import RInterpreter
from coqr.processors.CoqOutputProcessor import CoqOutputProcessor
from coqr.processors.ROutputProcessor import ROutputProcessor


class TestAll(TestCase):
    def setUp(self):
        RSCRIPT = os.environ.get("RSCRIPT")
        if RSCRIPT:
            self.R = RInterpreter(RSCRIPT)
        else:
            exit("Please define the 'RSCRIPT' variable.")

        COQ_INTERP = os.environ.get("COQ_INTERP")
        if COQ_INTERP:
            COQR_INITIAL_STATE = os.environ.get("COQR_INITIAL_STATE")
            if COQR_INITIAL_STATE:
                self.CoqR = CoqInterpreter(COQ_INTERP, COQR_INITIAL_STATE)
            else:
                exit("Please define the 'COQR_INITIAL_STATE' env variable.")
        else:
            exit("Please define the 'COQ_INTERP' variable.")

        self.r_processor = ROutputProcessor()
        self.coq_processor = CoqOutputProcessor()
        self.comparator = Comparator()

    def execute(self, expression) -> Status:
        r_result = self.R.interpret(expression)
        coq_result = self.CoqR.interpret(expression)

        processed_r_result = self.r_processor.process_output(r_result)
        processed_coq_result = self.coq_processor.process_output(coq_result)

        return self.comparator.compare(processed_coq_result, processed_r_result)

    def assertPass(self, expression):
        comparison = self.execute(expression)
        self.assertEqual(comparison, Status.PASS)

    def assertFail(self, expression):
        self.assertEqual(self.execute(expression), Status.FAIL)

    def assertUnknown(self, expression):
        self.assertEqual(self.execute(expression), Status.UNKNOWN)

    def test_list_pass(self):
        self.assertPass('list(1)')
        self.assertPass('list(1, 2, 3)')
        self.assertPass('list(a=1)')
        self.assertPass('list(a=1, 2, b=3)')

    def test_empty_lists(self):
        self.assertPass('list()')
        self.assertPass('list(1, list(), list(list()))')
        self.assertPass('list(1, list(), list(list(), 2, 4), list())')

    def test_nested_list_pass(self):
        self.assertPass('list(a=1, list(list(list(2, bc=3))), 4, c=5)')
        self.assertPass('list(1L, 1L, FALSE, NULL)')

    # def test_list_unknown(self):
