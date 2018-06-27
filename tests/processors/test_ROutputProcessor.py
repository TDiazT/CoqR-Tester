from math import inf, isnan, nan
from unittest import TestCase

from coqr.constants.Status import Status
from coqr.processors.ROutputProcessor import ROutputProcessor
from coqr.reports.results import NullResult, VectorResult, FunctionResult, ErrorResult, \
    InvisibleResult, UnknownResult, ListResult, NumericVector, BooleanVector, StringVector
from tests.processors.test_processor import TestCommonProcessor


class TestROutputProcessor(TestCase, TestCommonProcessor):
    def setUp(self):
        self.processor = ROutputProcessor()

    def assert_vector(self, output, expected: list):
        result = self.processor.process_output(output)
        self.assertIsInstance(result, VectorResult)
        self.assertEqual(result.result, expected)

    def assert_list(self, output, expected):
        result = self.processor.process_output(output)
        self.assertIsInstance(result, ListResult)
        self.assertEqual(result.result, expected)

    def assert_is_instance(self, output, instance):
        result = self.processor.process_output(output)
        self.assertIsInstance(result, instance)

    def assert_results(self, results, expected_case):
        for result in results:
            self.assertEqual(result, expected_case)

    def test_process_NULL(self):
        result = self.processor.process_output("NULL\n")
        self.assertIsInstance(result, NullResult)

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

    def test_null_in_function(self):
        self.assert_is_instance("function(n, trans.mat, init.dist=NULL, states=colnames(trans.mat)) { }",
                                FunctionResult)

    def test_process_error_object(self):
        self.assert_is_instance("Error: object 'e' not found", ErrorResult)

    def test_process_error_function(self):
        self.assert_is_instance("Error in e() : could not find function \"e\"", ErrorResult)

    def test_assignment_with_empty_array(self):
        self.assert_is_instance("", InvisibleResult)

    def test_function(self):
        self.assert_is_instance("function (x) x", FunctionResult)

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

    def test_primitive(self):
        self.assert_is_instance('.Primitive("return")\n', FunctionResult)

    def test_error_zero_length_var(self):
        self.assert_is_instance("Error: attempt to use zero-length variable name\nExecution halted\n", ErrorResult)

    def test_error_no_function_to_return_from(self):
        self.assert_is_instance("Error: no function to return from, jumping to top level\nExecution halted\n",
                                ErrorResult)

    def test_error_in_function(self):
        self.assert_is_instance(
            "Error in (function() break)() : \n  no loop for break/next, jumping to top level\nExecution halted\n",
            ErrorResult)

    def test_error_no_loop(self):
        self.assert_is_instance("Error: no loop for break/next, jumping to top level\nExecution halted\n", ErrorResult)

    def test_function_with_newlines(self):
        self.assert_is_instance("function () \nbreak\n", FunctionResult)

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
        [1] 4\n""")
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

        output = self.processor.process_output('[[1]]\nfunction () x\n[[2]]\n[1] "hey" "you"\n')
        self.assertIsInstance(output, ListResult)
        self.assertIsInstance(output.result, dict)
        self.assertEqual(len(output.result), 2)
        self.assertIsInstance(output.result['[[1]]'], FunctionResult)
        self.assertIsInstance(output.result['[[2]]'], StringVector)
        self.assertEqual(output.result['[[2]]'].result, ['"hey"', '"you"'])

    def test_fastr_cases(self):
        output = self.processor.process_output("""[[1]]
[1] "‘"

[[2]]
[1] "Matrix"

[[3]]
[1] "’" """)
        self.assertIsInstance(output, ListResult)
        self.assertIsInstance(output.result, dict)
        self.assertEqual(len(output.result), 3)
        self.assertIsInstance(output.result['[[1]]'], StringVector)
        self.assertIsInstance(output.result['[[2]]'], StringVector)
        self.assertIsInstance(output.result['[[3]]'], StringVector)
        self.assertEqual(output.result['[[1]]'].result, ['"‘"'])
        self.assertEqual(output.result['[[2]]'].result, ['"Matrix"'])
        self.assertEqual(output.result['[[3]]'].result, ['"’"'])

        output = self.processor.process_output("""[[1]]
function (...)  .Primitive("c")

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
Time Series:
Start = 1 
End = 1 
Frequency = 1 
[1] FALSE

[[2]]
Time Series:
Start = 1 
End = 1 
Frequency = 1 
[1] FALSE""")
        self.assertIsInstance(output, ListResult)
        self.assertIsInstance(output.result, dict)
        self.assertEqual(len(output.result), 2)
        self.assertIsInstance(output.result['[[1]]'], UnknownResult)
        self.assertIsInstance(output.result['[[2]]'], UnknownResult)

        output = self.processor.process_output("[[1]]\nlogical(0)\n")
        self.assertIsInstance(output, ListResult)
        self.assertIsInstance(output.result, dict)
        self.assertEqual(len(output.result), 1)
        self.assertIsInstance(output.result['[[1]]'], UnknownResult)

        output = self.processor.process_output("""[[1]]
       
 p L s  [,1]
  . . . TRUE
  | . . TRUE
  . | . TRUE
  | | . TRUE
  . . | TRUE
  | . | TRUE
  . | | TRUE
  | | | TRUE
  . . ? TRUE
  | . ? TRUE
  . | ? TRUE
  | | ? TRUE

""")
        self.assertIsInstance(output, ListResult)
        self.assertIsInstance(output.result, dict)
        self.assertEqual(len(output.result), 1)
        self.assertIsInstance(output.result['[[1]]'], UnknownResult)

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

        output = self.processor.process_output("""$ANY
function (x, y = NULL) 
.Internal(crossprod(x, y))
attr(,"target")
    x 
"ANY" 
attr(,"class")
[1] "signature"
attr(,"class")attr(,"package")
[1] "methods"
attr(,"package")
[1] "methods"
attr(,"defined")
    x 
"ANY" 
attr(,"class")
[1] "signature"
attr(,"class")attr(,"package")
[1] "methods"
attr(,"package")
[1] "methods"
attr(,"generic")
[1] "crossprod"
attr(,"generic")attr(,"package")
[1] "base"
attr(,"class")
[1] "derivedDefaultMethod"
attr(,"class")attr(,"package")
[1] "methods"
""")

        self.assertIsInstance(output, ListResult)
        self.assertIsInstance(output.result, dict)
        self.assertEqual(len(output.result), 1)
        self.assertIsInstance(output.result['$ANY'], FunctionResult)

    def test_simple_list_with_names(self):
        output = self.processor.process_output("$a\n[1] 1")
        self.assertIsInstance(output, ListResult)
        self.assertIsInstance(output.result, dict)
        self.assertEqual(len(output.result), 1)
        self.assertIsInstance(output.result['$a'], NumericVector)
        self.assertEqual(output.result['$a'].result, [1])

        output = self.processor.process_output("$a\n[1] 1\n$bc\n[1] 2\n")
        self.assertIsInstance(output, ListResult)
        self.assertIsInstance(output.result, dict)
        self.assertIsInstance(output.result['$a'], NumericVector)
        self.assertIsInstance(output.result['$bc'], NumericVector)
        self.assertEqual(output.result['$a'].result, [1])
        self.assertEqual(output.result['$bc'].result, [2])

        output = self.processor.process_output("$a\n[1] 2\n$b\n$b$c\n[1] 3\n$b$d\n[1] 4")
        self.assertIsInstance(output, ListResult)
        self.assertIsInstance(output.result, dict)
        self.assertIsInstance(output.result['$a'], NumericVector)
        self.assertIsInstance(output.result['$b'], dict)
        self.assertEqual(len(output.result['$b']), 2)
        self.assertIsInstance(output.result['$b']['$c'], NumericVector)
        self.assertIsInstance(output.result['$b']['$d'], NumericVector)
        self.assertEqual(output.result['$a'].result, [2])
        self.assertEqual(output.result['$b']['$c'].result, [3])
        self.assertEqual(output.result['$b']['$d'].result, [4])

    def test_mixed_named_numeric_list(self):
        output = self.processor.process_output("$a\n[1] 2\n[[2]]\n[[2]]$b\n[1] 3\n[[2]]$c\n[1] 4\n")
        self.assertIsInstance(output, ListResult)
        self.assertIsInstance(output.result, dict)
        self.assertEqual(len(output.result), 2)
        self.assertIsInstance(output.result['$a'], NumericVector)
        self.assertIsInstance(output.result['[[2]]'], dict)
        self.assertIsInstance(output.result['[[2]]']['$b'], NumericVector)
        self.assertIsInstance(output.result['[[2]]']['$c'], NumericVector)
        self.assertEqual(len(output.result['[[2]]']), 2)
        self.assertEqual(output.result['$a'].result, [2])
        self.assertEqual(output.result['[[2]]']['$b'].result, [3])
        self.assertEqual(output.result['[[2]]']['$c'].result, [4])

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

    def test_weird_names(self):
        output = self.processor.process_output("$`1`\n[1] 1\n")
        self.assertIsInstance(output, UnknownResult)

        output = self.processor.process_output("[[1]]\n[1] 1\n$`'a'`\n[1] 2")
        self.assertIsInstance(output, ListResult)
        # self.assertIsInstance(output.result["[[1]]"], UnknownResult)

        output = self.processor.process_output("""[[1]]
[1] 0

$length.out
[1] 3""")
        self.assertIsInstance(output, ListResult)
        self.assertEqual(set(output.result.keys()), {"[[1]]", "$length.out"})

