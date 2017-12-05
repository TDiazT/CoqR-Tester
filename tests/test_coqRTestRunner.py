from unittest import TestCase

from rcoq.Constants import SUCCESSFUL
from rcoq.interpreters.CoqRTestRunner import CoqRTestRunner


class TestCoqRTestRunner(TestCase):
    def setUp(self):
        self.runner = CoqRTestRunner()

    def test_TRUE(self):
        result = self.runner.test_expression("TRUE")
        self.assertEqual(result, [SUCCESSFUL])

    def test_FALSE(self):
        result = self.runner.test_expression("FALSE")
        self.assertEqual(result, [SUCCESSFUL])

    def test_NA(self):
        result = self.runner.test_expression("NA")
        self.assertEqual(result, [SUCCESSFUL])

    def test_NaN(self):
        result = self.runner.test_expression("NaN")
        self.assertEqual(result, [SUCCESSFUL])

    def test_NULL(self):
        result = self.runner.test_expression("NULL")
        self.assertEqual(result, [SUCCESSFUL])
