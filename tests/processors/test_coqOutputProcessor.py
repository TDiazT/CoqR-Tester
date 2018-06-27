from math import isnan, inf
from unittest import TestCase

from coqr.processors.CoqOutputProcessor import CoqOutputProcessor
from coqr.reports.results import VectorResult, NullResult, FunctionResult, ErrorResult, InvisibleResult, UnknownResult, \
    NotImplementedResult, ListResult, NumericVector, BooleanVector, StringVector
from tests.processors.test_processor import TestCommonProcessor


class TestCoqOutputProcessor(TestCase, TestCommonProcessor):
    def setUp(self):
        self.processor = CoqOutputProcessor()

    def assert_vector(self, output, expected: list):
        result = self.processor.process_output(output)
        self.assertIsInstance(result, VectorResult)
        self.assertEqual(result.result, expected)

    def assert_is_instance(self, output, instance):
        result = self.processor.process_output(output)
        self.assertIsInstance(result, instance)

    def assert_list(self, output, expected):
        result = self.processor.process_output(output)
        self.assertIsInstance(result, ListResult)
        self.assertEqual(result.result, expected)

    def test_process_error_object(self):
        self.assert_is_instance("Error: [eval] Object not found.\nAn error lead to an undefined result.\n", ErrorResult)
        self.assert_is_instance("Error: [eval] Object not found.\nAn error lead to an undefined result.\n", ErrorResult)

    def test_function(self):
        self.assert_is_instance("(closure)\n", FunctionResult)

    def test_not_implemented(self):
        self.assert_is_instance(
            "Not implemented: [do_c]\nAn error lead to an undefined state. Continuing using the old one.\n"
            "An error lead to an undefined result.\n> ", NotImplementedResult)

    def test_parse_error_over_not_implemented(self):
        output = "Error: Parser error at offset 2133.\n> Error: [findFun3] Could not find function \u201cf\u201d.\n" \
                 "An error lead to an undefined result.\n> Error: Parser error at offset 2166.\n" \
                 "> > > (closure)\n> Error: [findFun3] Could not find function \u201cdeparse\u201d.\n" \
                 "An error lead to an undefined result.\n" \
                 "> Not implemented: [do_for]\nAn error lead to an undefined state. Continuing using the old one.\n" \
                 "An error lead to an undefined result."
        self.assert_is_instance(output, ErrorResult)

    def test_process_NULL(self):
        self.assert_is_instance("NULL", NullResult)

    def test_process_ignore_warning(self):
        output = self.processor.process_output("[1] NaN\nWarning message:\nIn sqrt(-16) : NaNs produced")
        self.assertTrue(len(output.result) == 1)
        self.assertTrue(isnan(output.result[0]))

    def test_booleans(self):
        self.assert_vector('[1] TRUE\n', [True])
        self.assert_vector('[1] FALSE\n', [False])
        self.assert_vector('[1] TRUE\n[2] TRUE', [True, True])
        self.assert_vector('[1] TRUE\n[1] FALSE', [True, False])
        self.assert_vector('[1] TRUE    ', [True])

    def test_boolean_with_NA(self):
        self.assert_vector("[1] NA    TRUE  NA    FALSE\n", [None, True, None, False])

    def test_simple_number(self):
        self.assert_vector("[1] 1", [1.0])

    def test_vector_with_spaces(self):
        self.assert_vector('[1] TRUE\n', [True])
        self.assert_vector('[1]     FALSE\n', [False])
        self.assert_vector('[1]     FALSE    TRUE  \n', [False, True])
        self.assert_vector('[1]     "test"    "test2"  \n', ['"test"', '"test2"'])
        self.assert_vector('[1]     1   2 3\n', [1.0, 2.0, 3.0])
        self.assert_vector('    [1] 1      3', [1.0, 3.0])
        self.assert_vector("[1] TRUE  FALSE FALSE FALSE\n", [True, False, False, False])
        self.assert_vector("[1] TRUE  TRUE  TRUE  FALSE\n", [True, True, True, False])

    def test_vector_with_newlines(self):
        self.assert_vector('[1] 1 2 3 4\n[4] 5 6 7 8', [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0])
        self.assert_vector('[1] TRUE\n[2] FALSE\n[3] TRUE\n[4] FALSE', [True, False, True, False])

    def test_process_string(self):
        self.assert_vector("[1] \" + input + \"\n[1] \" + input + \"\n> ", ["\" + input + \"", "\" + input + \""])
        self.assert_vector('[1] "\"hola\"" "como" "estas"', ['"\"hola\""', '"como"', '"estas"'])
        self.assert_vector('[1] "1+1+FALSE-2+2+FALSE-1+3+FALSE"', ['"1+1+FALSE-2+2+FALSE-1+3+FALSE"'])
        self.assert_vector('[1] "/tmp/RtmpagC9oa/Pkgs/exNSS4"', ['"/tmp/RtmpagC9oa/Pkgs/exNSS4"'])
        self.assert_vector('[1] "detaching ‘package:splines’"', ['"detaching ‘package:splines’"'])
        self.assert_vector('[1] "\\226\\128\\152"', ['"\\226\\128\\152"'])

    def test_process_NA(self):
        self.assert_vector("[1] NA", [None])

    def test_process_NaN(self):
        output = self.processor.process_output("[1] NaN")
        self.assertTrue(len(output.result) == 1)
        self.assertTrue(isnan(output.result[0]))

    def test_process_Inf(self):
        self.assert_vector("[1] Inf", [inf])
        self.assert_vector("[1] -Inf", [-inf])

    def test_vector_output(self):
        self.assert_vector("[1] 1 2 3\n[4] 5 6 7\n", [1.0, 2.0, 3.0, 5.0, 6.0, 7.0])

    def test_vector_with_decimals(self):
        self.assert_vector("[1] 2.4259 3.4293 3.9896 5.2832 5.3386 4.9822\n",
                           [2.4259, 3.4293, 3.9896, 5.2832, 5.3386, 4.9822])

    def test_process_multiple_nan(self):
        output = self.processor.process_output("[1] NaN\n [1] NaN\n [4] NaN\n")
        self.assertTrue(len(output.result) == 3)
        for out in output.result:
            self.assertTrue(isnan(out))

        output = self.processor.process_output("[1] NaN NaN NaN\n[1] NaN\n [4] NaN\n")
        self.assertTrue(len(output.result) == 5)
        for out in output.result:
            self.assertTrue(isnan(out))

    def test_numeric_output(self):
        self.assert_vector("[1] NA  1 1.2 0.3 2e-12 -Inf\n[12] NA NA\n",
                           [None, 1.0, 1.2, 0.3, 2e-12, -inf, None, None])

    def test_string_function_not_mistaken_by_real_function(self):
        self.assert_vector('[1] "function"\n', ['"function"'])

    def test_process_error_function(self):
        self.assert_is_instance("Error in e() : could not find function \"e\"", ErrorResult)

    def test_assignment_with_empty_array(self):
        self.assert_is_instance("", InvisibleResult)

    def test_unknown(self):
        self.assert_is_instance("anything", UnknownResult)
        self.assert_is_instance("adfasd", UnknownResult)

    def test_vector_type_to_unknown(self):
        self.assert_is_instance("integer(0)", UnknownResult)
        self.assert_is_instance("numeric(0)", UnknownResult)
        self.assert_is_instance("logical(0)", UnknownResult)
        self.assert_is_instance("character(0)", UnknownResult)

    def test_cbind_output(self):
        self.assert_is_instance("     [,1] [,2]\n[1,]    1    2\n[2,]    2    2\n[3,]    3    2\n", UnknownResult)

    def test_simple_numeric_list(self):
        output = self.processor.process_output("[[1]]\n[1] 1")
        self.assertIsInstance(output, ListResult)
        self.assertIsInstance(output.result, dict)
        self.assertIsInstance(output.result['[[1]]'], NumericVector)
        self.assertEqual(output.result['[[1]]'].result, [1])

        output = self.processor.process_output("[[1]]\n[1] 1\n[[2]]\n[1] 2\n")
        self.assertIsInstance(output, ListResult)
        self.assertIsInstance(output.result, dict)
        self.assertIsInstance(output.result['[[1]]'], NumericVector)
        self.assertIsInstance(output.result['[[2]]'], NumericVector)
        self.assertEqual(output.result['[[1]]'].result, [1])
        self.assertEqual(output.result['[[2]]'].result, [2])

        output = self.processor.process_output("[[1]]\n[1] NA\n[[2]]\n[1] Inf\n")
        self.assertIsInstance(output, ListResult)
        self.assertIsInstance(output.result, dict)
        self.assertIsInstance(output.result['[[1]]'], BooleanVector)
        self.assertIsInstance(output.result['[[2]]'], NumericVector)
        self.assertIsNone(output.result['[[1]]'].result[0])
        self.assertEqual(output.result['[[2]]'].result, [inf])

        output = self.processor.process_output("""[[1]]
 [1]  1  2  3  4  5  6  7  8  9 10

[[2]]
 [1] 10 11 12 13 14 15 16 17 18 19 20""")
        self.assertIsInstance(output, ListResult)
        self.assertIsInstance(output.result, dict)
        self.assertIsInstance(output.result['[[1]]'], NumericVector)
        self.assertIsInstance(output.result['[[2]]'], NumericVector)
        self.assertEqual(output.result['[[1]]'].result, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(output.result['[[2]]'].result, [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

    def test_nested_numeric_lists(self):
        output = self.processor.process_output("[[1]]\n[1] 1\n[[2]]\n[[2]][[1]]\n[1] 2\n")
        self.assertIsInstance(output, ListResult)
        self.assertIsInstance(output.result, dict)
        self.assertIsInstance(output.result['[[1]]'], NumericVector)
        self.assertIsInstance(output.result['[[2]]'], dict)
        self.assertEqual(output.result['[[1]]'].result, [1])
        self.assertEqual(len(output.result['[[2]]']), 1)
        self.assertEqual(output.result['[[2]]']['[[1]]'].result, [2])

        output = self.processor.process_output("[[1]]\n[[1]][[1]]\n[1] 1")
        self.assertIsInstance(output, ListResult)
        self.assertIsInstance(output.result, dict)
        self.assertIsInstance(output.result['[[1]]'], dict)
        self.assertEqual(len(output.result['[[1]]']), 1)
        self.assertIsInstance(output.result['[[1]]']['[[1]]'], NumericVector)
        self.assertEqual(output.result['[[1]]']['[[1]]'].result, [1])

        output = self.processor.process_output("[[1]]\n[[1]][[1]]\n[1] 1\n[[2]]\n[1] 2\n")
        self.assertIsInstance(output, ListResult)
        self.assertIsInstance(output.result, dict)
        self.assertEqual(len(output.result), 2)
        self.assertIsInstance(output.result['[[1]]'], dict)
        self.assertIsInstance(output.result['[[2]]'], NumericVector)
        self.assertEqual(len(output.result['[[1]]']), 1)
        self.assertIsInstance(output.result['[[1]]']['[[1]]'], NumericVector)
        self.assertEqual(output.result['[[1]]']['[[1]]'].result, [1])
        self.assertEqual(output.result['[[2]]'].result, [2])

        output = self.processor.process_output("[[1]]\n[[1]][[1]]\n[1] 1\n[[1]][[2]]\n[1] 2\n")
        self.assertIsInstance(output, ListResult)
        self.assertIsInstance(output.result, dict)
        self.assertEqual(len(output.result), 1)
        self.assertIsInstance(output.result['[[1]]'], dict)
        self.assertEqual(len(output.result['[[1]]']), 2)
        self.assertIsInstance(output.result['[[1]]']['[[1]]'], NumericVector)
        self.assertIsInstance(output.result['[[1]]']['[[2]]'], NumericVector)
        self.assertEqual(output.result['[[1]]']['[[1]]'].result, [1])
        self.assertEqual(output.result['[[1]]']['[[2]]'].result, [2])

        output = self.processor.process_output("""[[1]]
[[1]][[1]]
[[1]][[1]][[1]]
[[1]][[1]][[1]][[1]]
[1] 4

[[1]][[1]][[1]][[2]]
[1] 5




[[2]]
[1] 4""")
        self.assertIsInstance(output, ListResult)
        self.assertIsInstance(output.result, dict)
        self.assertEqual(len(output.result), 2)
        self.assertIsInstance(output.result['[[1]]'], dict)
        self.assertIsInstance(output.result['[[2]]'], NumericVector)
        self.assertEqual(len(output.result['[[1]]']), 1)
        self.assertIsInstance(output.result['[[1]]']['[[1]]'], dict)
        self.assertEqual(len(output.result['[[1]]']['[[1]]']), 1)
        self.assertIsInstance(output.result['[[1]]']['[[1]]']['[[1]]'], dict)
        self.assertEqual(len(output.result['[[1]]']['[[1]]']['[[1]]']), 2)
        self.assertIsInstance(output.result['[[1]]']['[[1]]']['[[1]]']['[[1]]'], NumericVector)
        self.assertIsInstance(output.result['[[1]]']['[[1]]']['[[1]]']['[[2]]'], NumericVector)
        self.assertEqual(output.result['[[1]]']['[[1]]']['[[1]]']['[[1]]'].result, [4])
        self.assertEqual(output.result['[[1]]']['[[1]]']['[[1]]']['[[2]]'].result, [5])
        self.assertEqual(output.result['[[2]]'].result, [4])

    def test_simple_mixed_list(self):
        output = self.processor.process_output("[[1]]\n[1] 1\n[[2]]\n[1] TRUE\n")
        self.assertIsInstance(output, ListResult)
        self.assertIsInstance(output.result, dict)
        self.assertEqual(len(output.result), 2)
        self.assertIsInstance(output.result['[[1]]'], NumericVector)
        self.assertIsInstance(output.result['[[2]]'], BooleanVector)
        self.assertEqual(output.result['[[1]]'].result, [1])
        self.assertEqual(output.result['[[2]]'].result, [True])

        output = self.processor.process_output('[[1]]\n(closure)\n[[2]]\n[1] "hey" "you"\n')
        self.assertIsInstance(output, ListResult)
        self.assertIsInstance(output.result, dict)
        self.assertEqual(len(output.result), 2)
        self.assertIsInstance(output.result['[[1]]'], FunctionResult)
        self.assertIsInstance(output.result['[[2]]'], StringVector)
        self.assertEqual(output.result['[[2]]'].result, ['"hey"', '"you"'])

    def test_fastr_cases(self):
        # argv <- list('‘', 'Matrix', '’');list(argv[[1]],argv[[2]],argv[[3]]);
        output = self.processor.process_output("""[[1]]
[1] "\\226\\128\\152"

[[2]]
[1] "Matrix"

[[3]]
[1] "\\226\\128\\153" """)
        self.assertIsInstance(output, ListResult)
        self.assertIsInstance(output.result, dict)
        self.assertEqual(len(output.result), 3)
        self.assertIsInstance(output.result['[[1]]'], StringVector)
        self.assertIsInstance(output.result['[[2]]'], StringVector)
        self.assertIsInstance(output.result['[[3]]'], StringVector)
        self.assertEqual(output.result['[[1]]'].result, ['"\\226\\128\\152"'])
        self.assertEqual(output.result['[[2]]'].result, ['"Matrix"'])
        self.assertEqual(output.result['[[3]]'].result, ['"\\226\\128\\153"'])

        # argv <- list(.Primitive('c'), list(list(), list(), list()), NULL)
        output = self.processor.process_output("""[[1]]
(builtin: 90)

[[2]]
[[2]][[1]]
list()

[[2]][[2]]
list()

[[2]][[3]]
list()


[[3]]
NULL""")

        self.assertIsInstance(output, ListResult)
        self.assertIsInstance(output.result, dict)
        self.assertEqual(len(output.result), 3)
        self.assertIsInstance(output.result['[[1]]'], FunctionResult)
        self.assertIsInstance(output.result['[[2]]'], dict)
        self.assertEqual(len(output.result['[[2]]']), 3)
        self.assertIsInstance(output.result['[[3]]'], NullResult)
        self.assertIsInstance(output.result['[[2]]']['[[1]]'], UnknownResult)
        self.assertIsInstance(output.result['[[2]]']['[[2]]'], UnknownResult)
        self.assertIsInstance(output.result['[[2]]']['[[3]]'], UnknownResult)

        output = self.processor.process_output("""[[1]]
[1]  1  2  3  4  8 12

[[2]]
[1]  1  2  3  4  8 12

[[3]]
[1] NA

[[4]]
NULL""")

        self.assertIsInstance(output, ListResult)
        self.assertIsInstance(output.result, dict)
        self.assertEqual(len(output.result), 4)
        self.assertIsInstance(output.result['[[1]]'], NumericVector)
        self.assertIsInstance(output.result['[[2]]'], NumericVector)
        self.assertIsInstance(output.result['[[3]]'], BooleanVector)
        self.assertIsInstance(output.result['[[4]]'], NullResult)
        self.assertEqual(output.result['[[1]]'].result, [1, 2, 3, 4, 8, 12])
        self.assertEqual(output.result['[[2]]'].result, [1, 2, 3, 4, 8, 12])

        # argv <- list(structure(function (x, mode = 'any') .Internal(as.vector(x, mode)), target = structure('ANY', class = structure('signature', package = 'methods'), .Names = 'x', package = 'methods'), defined = structure('ANY', class = structure('signature', package = 'methods'), .Names = 'x', package = 'methods'), generic = character(0), class = structure('MethodDefinition', package = 'methods')))
        output = self.processor.process_output("""[[1]]
(closure)""")

        self.assertIsInstance(output, ListResult)
        self.assertIsInstance(output.result, dict)
        self.assertEqual(len(output.result), 1)
        self.assertIsInstance(output.result['[[1]]'], FunctionResult)

    def test_simple_list_with_names(self):
        output = self.processor.process_output("""[[1]]
[1] 1

attr(,"names")
[1] "a" """)
        self.assertIsInstance(output, ListResult)
        self.assertIsInstance(output.result, dict)
        self.assertEqual(len(output.result), 1)
        self.assertIsInstance(output.result['$a'], NumericVector)
        self.assertEqual(output.result['$a'].result, [1])

        output = self.processor.process_output("""[[1]]
[1] 1

[[2]]
[1] 2

attr(,"names")
[1] "a"  "bc" """)
        self.assertIsInstance(output, ListResult)
        self.assertIsInstance(output.result, dict)
        self.assertEqual(output.result.keys(), {'$a', '$bc'})
        self.assertIsInstance(output.result['$a'], NumericVector)
        self.assertIsInstance(output.result['$bc'], NumericVector)
        self.assertEqual(output.result['$a'].result, [1])
        self.assertEqual(output.result['$bc'].result, [2])

        output = self.processor.process_output("""[[1]]
[1] 2

[[2]]
[[2]][[1]]
[1] 3

[[2]][[2]]
[1] 4

attr(,"names")
[1] "c" "d"

attr(,"names")
[1] "a" "b" """)
        self.assertIsInstance(output, ListResult)
        self.assertIsInstance(output.result, dict)
        self.assertEqual(len(output.result), 2)
        self.assertEqual(output.result.keys(), {'$a', '$b'})

        self.assertIsInstance(output.result['$a'], NumericVector)
        self.assertIsInstance(output.result['$b'], dict)
        self.assertEqual(len(output.result['$b']), 2)

        self.assertEqual(output.result['$a'].result, [2])
        self.assertEqual(output.result['$b'].keys(), {'$c', '$d'})

        self.assertIsInstance(output.result['$b']['$c'], NumericVector)
        self.assertIsInstance(output.result['$b']['$d'], NumericVector)
        self.assertEqual(output.result['$b']['$c'].result, [3])
        self.assertEqual(output.result['$b']['$d'].result, [4])

        output = self.processor.process_output("""[[1]]
[1] 1

[[2]]
[1] 1

[[3]]
[[3]][[1]]
[1] 2

attr(,"names")
[1] "b"

[[4]]
[1] 3

attr(,"names")
[1] "a" ""  ""  "c" """)
        self.assertIsInstance(output, ListResult)
        self.assertIsInstance(output.result, dict)
        self.assertEqual(len(output.result), 4)
        self.assertEqual(output.result.keys(), {'$a', '[[2]]', '[[3]]', '$c'})

        self.assertIsInstance(output.result['$a'], NumericVector)
        self.assertIsInstance(output.result['[[2]]'], NumericVector)
        self.assertIsInstance(output.result['[[3]]'], dict)
        self.assertIsInstance(output.result['$c'], NumericVector)
        self.assertEqual(len(output.result['[[3]]']), 1)

        self.assertEqual(output.result['$a'].result, [1])
        self.assertEqual(output.result['[[2]]'].result, [1])
        self.assertEqual(output.result['$c'].result, [3])
        self.assertEqual(output.result['[[3]]'].keys(), {'$b'})

        self.assertIsInstance(output.result['[[3]]']['$b'], NumericVector)
        self.assertEqual(output.result['[[3]]']['$b'].result, [2])

    def test_multilined_list_elements(self):
        output = self.processor.process_output("""[[1]]
  [1]   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18
 [19]  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36
 [37]  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54
 [55]  55  56  57  58  59  60  61  62  63  64  65  66  67  68  69  70  71  72
 [73]  73  74  75  76  77  78  79  80  81  82  83  84  85  86  87  88  89  90
 [91]  91  92  93  94  95  96  97  98  99 100""")
        self.assertIsInstance(output, ListResult)
        self.assertIsInstance(output.result, dict)
        self.assertEqual(output.result['[[1]]'].result, list(range(1, 101)))
