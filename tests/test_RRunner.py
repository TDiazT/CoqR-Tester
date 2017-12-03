from unittest import TestCase

from rcoq.runners.RRunner import RRunner


class TestRRunner(TestCase):
    def setUp(self):
        self.runner = RRunner()

    def test_expression_number(self):
        result = self.runner.run_expression("2")
        self.assertEqual(result, "[1] 2\n")

    def test_expression_TRUE(self):
        result = self.runner.run_expression("TRUE")
        self.assertEqual(result, "[1] TRUE\n")

    def test_expression_NULL(self):
        result = self.runner.run_expression("NULL")
        self.assertEqual(result, "NULL\n")

    def test_run_file(self):
        result = self.runner.run_file("tests/fixtures/test.R")
        self.assertEqual(result, "[1] TRUE\n")