class TestCommonProcessor(object):
    def assert_output(self, output, expected):
        result = self.processor.process_output(output)
        self.assertEqual(result, expected)
