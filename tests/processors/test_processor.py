class TestCommonProcessor(object):
    def assert_output(self, output, expected):
        result = self.processor.process_output(output)
        self.assertEqual(result, expected)

    def test_process_2(self):
        result = self.processor.process_output("[1] 2\n")
        self.assertEqual(result, '[1] 2')

    def test_process_TRUE(self):
        result = self.processor.process_output("[1] TRUE\n")
        self.assertEqual(result, "[1] TRUE")

    def test_process_FALSE(self):
        result = self.processor.process_output("[1] FALSE\n")
        self.assertEqual(result, "[1] FALSE")

    def test_process_NA(self):
        result = self.processor.process_output("[1] NA\n")
        self.assertEqual(result, "[1] NA")

    def test_process_NaN(self):
        result = self.processor.process_output("[1] NaN\n")
        self.assertEqual(result, "[1] NaN")

    def test_process_Inf(self):
        result = self.processor.process_output("[1] Inf\n")
        self.assertEqual(result, "[1] Inf")
        result = self.processor.process_output("[1] -Inf\n")
        self.assertEqual(result, "[1] -Inf")

    def test_vector_output(self):
        result = self.processor.process_output("[1] 1 2 3\n[4] 5 6 7\n")
        self.assertEqual(result, "[1] 1 2 3 [4] 5 6 7")

    def test_vector_double_bracket(self):
        output = "[[1]]\n[[1]]$input\n[1]  TRUE FALSE\n\n[[1]]$any\n[1] TRUE\n\n[[1]]$all\n[1] FALSE\n\n\n[[2]]\n"
        result = self.processor.process_output(output)
        self.assertEqual(result, "[[1]] [[1]]$input [1]  TRUE FALSE [[1]]$any [1] TRUE [[1]]$all [1] FALSE [[2]]")

    def test_vector_double_bracket_2(self):
        output = "[[2]]$input\n[[2]]$input[[1]]\n[1] FALSE\n\n"
        result = self.processor.process_output(output)
        self.assertEqual(result, "[[2]]$input [[2]]$input[[1]] [1] FALSE")

    def test_vector_with_decimals(self):
        output = "[1] 2.4259 3.4293 3.9896 5.2832 5.3386 4.9822\n"
        result = self.processor.process_output(output)
        self.assertEqual(result, "[1] 2.4259 3.4293 3.9896 5.2832 5.3386 4.9822")

    def test_digits(self):
        self.assert_output("$digits\n[1] 7\n\n", "$digits\n[1] 7")
