class TestCommonProcessor(object):
    def assert_output(self, output, expected):
        result = self.processor.process_output(output)
        self.assertEqual(result, expected)

    def test_process_2(self):
        result = self.processor.process_output("[1] 2")
        self.assertEqual(result, '[1] 2')

    def test_process_TRUE(self):
        self.assert_output("[1] TRUE", "[1] TRUE")

    def test_process_FALSE(self):
        result = self.processor.process_output("[1] FALSE")
        self.assertEqual(result, "[1] FALSE")

    def test_process_NA(self):
        self.assert_output("[1] NA", "[1] NA")

    def test_process_NaN(self):
        result = self.processor.process_output("[1] NaN")
        self.assertEqual(result, "[1] NaN")

    def test_process_Inf(self):
        result = self.processor.process_output("[1] Inf")
        self.assertEqual(result, "[1] Inf")
        result = self.processor.process_output("[1] -Inf")
        self.assertEqual(result, "[1] -Inf")

    def test_vector_output(self):
        result = self.processor.process_output("[1] 1 2 3\n[4] 5 6 7\n")
        self.assertEqual(result, "[1] 1 2 3\n[4] 5 6 7")

    def test_vector_with_decimals(self):
        self.assert_output("[1] 2.4259 3.4293 3.9896 5.2832 5.3386 4.9822\n",
                           "[1] 2.4259 3.4293 3.9896 5.2832 5.3386 4.9822")
