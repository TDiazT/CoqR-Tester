from unittest import TestCase

from coqr.interpreters.RInterpreter import RInterpreter


class TestRRunner(TestCase):
    def setUp(self):
        self.runner = RInterpreter('rscript')

    def test_expression_number(self):
        result = self.runner.interpret("2")
        self.assertEqual(result, "[1] 2\n")

    def test_expression_TRUE(self):
        result = self.runner.interpret("TRUE")
        self.assertEqual(result, "[1] TRUE\n")

    def test_expression_NULL(self):
        result = self.runner.interpret("NULL")
        self.assertEqual(result, "NULL\n")