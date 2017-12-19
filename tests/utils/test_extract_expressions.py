from unittest import TestCase
from rcoq.utils import exp_extract


class TestExtract_expressions(TestCase):
    def test_extract_empty_cases(self):
        self.assertEqual(exp_extract.extract_expressions("''"), ["''"])
        self.assertEqual(exp_extract.extract_expressions('""'), ['""'])
        self.assertEqual(exp_extract.extract_expressions("{}"), ["{}"])

    def test_single_quote(self):
        txt = "''"
        self.assertEqual(exp_extract.extract_expressions(txt), [txt])
        txt = "'''"
        self.assertEqual(exp_extract.extract_expressions(txt), ["''", "'"])
        txt = "''''"
        self.assertEqual(exp_extract.extract_expressions(txt), ["''", "''"])
        txt = "'''''''"
        self.assertEqual(exp_extract.extract_expressions(txt), ["''", "''", "''", "'"])

    def test_double_quotes(self):
        txt = '""'
        self.assertEqual(exp_extract.extract_expressions(txt), [txt])
        txt = '"""'
        self.assertEqual(exp_extract.extract_expressions(txt), ['""', '"'])
        txt = '""""'
        self.assertEqual(exp_extract.extract_expressions(txt), ['""', '""'])
        txt = '"""""""'
        self.assertEqual(exp_extract.extract_expressions(txt), ['""', '""', '""', '"'])

    def test_double_quotes(self):
        txt = '{}'
        self.assertEqual(exp_extract.extract_expressions(txt), [txt])
        txt = '{{'
        self.assertEqual(exp_extract.extract_expressions(txt), ['{{'])
        txt = '{}}'
        self.assertEqual(exp_extract.extract_expressions(txt), ['{}', '}'])
        txt = '{{}}'
        self.assertEqual(exp_extract.extract_expressions(txt), ['{{}', '}'])
        txt = '{}{}'
        self.assertEqual(exp_extract.extract_expressions(txt), ['{}', '{}'])
        txt = '{}{}{}{'
        self.assertEqual(exp_extract.extract_expressions(txt), ['{}', '{}', '{}', '{'])

    def test_extract_other_chars(self):
        txt = "<-\\ $afdgQWEASDF_>+`^*/?(123567)ºœ€æ®¥å∫ƒ∑©√ß¥  ø™~"
        self.assertEqual(exp_extract.extract_expressions(txt), [txt])

    def test_cases_inside_single_quote(self):
        txt = "'""'"
        self.assertEqual(exp_extract.extract_expressions(txt), [txt])
        txt = "'{}'"
        self.assertEqual(exp_extract.extract_expressions(txt), [txt])
        txt = "'\"{}\"'"
        self.assertEqual(exp_extract.extract_expressions(txt), [txt])
        txt = "'{\"\"}'"
        self.assertEqual(exp_extract.extract_expressions(txt), [txt])
        txt = "'{\"}\"'"
        self.assertEqual(exp_extract.extract_expressions(txt), [txt])
        txt = "'\"{\"}'"
        self.assertEqual(exp_extract.extract_expressions(txt), [txt])

    def test_cases_inside_double_quote(self):
        txt = '"\'\'"'
        self.assertEqual(exp_extract.extract_expressions(txt), [txt])
        txt = '"{}"'
        self.assertEqual(exp_extract.extract_expressions(txt), [txt])
        txt = '"\'{}\'"'
        self.assertEqual(exp_extract.extract_expressions(txt), [txt])
        txt = '"{\'\'}"'
        self.assertEqual(exp_extract.extract_expressions(txt), [txt])
        txt = '"{\'}\'"'
        self.assertEqual(exp_extract.extract_expressions(txt), [txt])
        txt = '"\'{\'}"'
        self.assertEqual(exp_extract.extract_expressions(txt), [txt])

    def test_cases_inside_curly_brackets(self):
        txt = "{\"\"}"
        self.assertEqual(exp_extract.extract_expressions(txt), [txt])
        txt = "{\'\'}"
        self.assertEqual(exp_extract.extract_expressions(txt), [txt])
        txt = "{\'\"\"\'}"
        self.assertEqual(exp_extract.extract_expressions(txt), [txt])
        txt = "{\"''\"}"
        self.assertEqual(exp_extract.extract_expressions(txt), [txt])
        txt = "{\"'\"'}"
        self.assertEqual(exp_extract.extract_expressions(txt), [txt])
        txt = "{'\"'\"}"
        self.assertEqual(exp_extract.extract_expressions(txt), [txt])

    def test_semicolons_separating_words(self):
        t1 = 'asfd'
        t2 = 'qweq'
        t3 = 'qwoek'
        txt = "%s;%s;%s" % (t1, t2, t3)
        self.assertEqual(exp_extract.extract_expressions(txt), [t1, t2, t3])

    def test_semicolon_separating_cases(self):
        t1 = "'adsfasd'"
        t2 = '"qweqw"'
        t3 = '{124}'
        txt = "%s;%s;%s" % (t1, t2, t3)
        self.assertEqual(exp_extract.extract_expressions(txt), [t1, t2, t3])

    def test_semicolon_ignored_inside_cases(self):
        txt = "';'"
        self.assertEqual(exp_extract.extract_expressions(txt), [txt])

        txt = '";"'
        self.assertEqual(exp_extract.extract_expressions(txt), [txt])

        txt = "{;}"
        self.assertEqual(exp_extract.extract_expressions(txt), [txt])

        txt = "'afsdf;qwer;1235'"
        self.assertEqual(exp_extract.extract_expressions(txt), [txt])

        txt = '"afsdf;qwer;1235"'
        self.assertEqual(exp_extract.extract_expressions(txt), [txt])

        txt = "{afsdf;qwer;1235}"
        self.assertEqual(exp_extract.extract_expressions(txt), [txt])

    def test_separating_r_expressions(self):

        t1 = 'x < - function(a, b)'
        t2 = '{a ^ b}'
        t3 = 'dummy < - sum'
        t4 = 'f < - function() {x < - "dummy"; dummy < - 200; sapply(1, x, 2)}'
        t5 = 'f()'
        txt = "%s;%s;%s;%s;%s" % (t1, t2, t3, t4, t5)
        self.assertEqual(exp_extract.extract_expressions(txt), [t1, t2, t3, t4, t5])
