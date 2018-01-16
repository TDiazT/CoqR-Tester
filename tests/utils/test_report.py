from unittest import TestCase

from coqr.constants import ReportKeys

from coqr.utils import reports


class TestReport(TestCase):
    def test_report_with_one_expression(self):
        exp = "a <- 1"
        filename = 'file.R'
        interpreter = 'R'
        exec_time = 123
        line = 1
        processed_out = ['[1] 1']
        report = reports.generate_report(exp, processed_out, interpreter, exec_time, filename, line)
        sub_report = [{ReportKeys.SUB_EXPRESSION: exp, ReportKeys.OUTPUT: processed_out[0]}]

        self.assertEquals(report[ReportKeys.EXPRESSION], exp)
        self.assertEquals(report[ReportKeys.FILENAME], filename)
        self.assertEquals(report[ReportKeys.INTERPRETER], interpreter)
        self.assertEquals(report[ReportKeys.EXEC_TIME], exec_time)
        self.assertEquals(report[ReportKeys.LINE], line)
        self.assertEquals(report[ReportKeys.SUB_EXPRESSIONS_REPORT],
                          sub_report)

    def test_report_with_multiple_sub_expressions(self):
        e1 = 'a <- 1'
        e2 = '2'
        e3 = 'NULL'
        exp = "%s; %s; %s" % (e1, e2, e3)
        filename = 'file.R'
        interpreter = 'R'
        exec_time = 123
        line = 1
        processed_out = ['[1] 1', '[2] 2', 'NULL']
        report = reports.generate_report(exp, processed_out, interpreter, exec_time, filename, line)
        sub_report = [
            {ReportKeys.SUB_EXPRESSION: e1, ReportKeys.OUTPUT: processed_out[0]},
            {ReportKeys.SUB_EXPRESSION: e2, ReportKeys.OUTPUT: processed_out[1]},
            {ReportKeys.SUB_EXPRESSION: e3, ReportKeys.OUTPUT: processed_out[2]}
        ]

        self.assertEquals(report[ReportKeys.EXPRESSION], exp)
        self.assertEquals(report[ReportKeys.FILENAME], filename)
        self.assertEquals(report[ReportKeys.INTERPRETER], interpreter)
        self.assertEquals(report[ReportKeys.EXEC_TIME], exec_time)
        self.assertEquals(report[ReportKeys.LINE], line)
        self.assertEquals(report[ReportKeys.SUB_EXPRESSIONS_REPORT],
                          sub_report)
