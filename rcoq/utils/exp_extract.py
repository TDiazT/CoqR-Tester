import sys


def __extract_quote(quoted_expression):
    if not quoted_expression:
        return '', []
    elif quoted_expression[0] == '\'':
        return '\'', quoted_expression[1:]
    else:
        quote = __extract_quote(quoted_expression[1:])
        return quoted_expression[0] + quote[0], quote[1]


def __extract_double_quote(quoted_expression):
    if not quoted_expression:
        return '', []
    elif quoted_expression[0] == '\"':
        return '"', quoted_expression[1:]
    else:
        quote = __extract_double_quote(quoted_expression[1:])
        return quoted_expression[0] + quote[0], quote[1]


def __extract_curly(curly_exp):
    if not curly_exp:
        return '', []
    elif curly_exp[0] == '}':
        return '}', curly_exp[1:]
    else:
        curly = __extract_curly(curly_exp[1:])
        return curly_exp[0] + curly[0], curly[1]


def __extract_other(param):
    if not param:
        return '', []
    elif param[0] == '\'':
        (quote, rest) = __extract_quote(param[1:])
        other = __extract_other(rest)
        return '\'' + quote + other[0], other[1]
    elif param[0] == '\"':
        (quote, rest) = __extract_double_quote(param[1:])
        other = __extract_other(rest)
        return '\"' + quote + other[0], other[1]

    elif param[0] == '{':
        (quote, rest) = __extract_curly(param[1:])
        other = __extract_other(rest)
        return '{' + quote + other[0], other[1]
    elif param[0] == ';':
        return '', param[1:]
    else:
        (word, rest) = __extract_other(param[1:])
        return param[0] + word, rest


def extract_expressions(expressions):
    if not expressions:
        return []
    elif expressions[0] == '\'':
        (quote, rest) = __extract_quote(expressions[1:])
        return ['\'' + quote] + extract_expressions(rest)
    elif expressions[0] == '\"':
        (quote, rest) = __extract_double_quote(expressions[1:])
        return ['\"' + quote] + extract_expressions(rest)

    elif expressions[0] == '{':
        (quote, rest) = __extract_curly(expressions[1:])
        return ['{' + quote] + extract_expressions(rest)
    elif expressions[0] == ';':
        return extract_expressions(expressions[1:])
    elif expressions[0] == ' ':
        return extract_expressions(expressions[1:])
    else:
        (word, rest) = __extract_other(expressions[1:])
        return [expressions[0] + word] + extract_expressions(rest)


if __name__ == '__main__':
    expressions = extract_expressions(sys.argv[1])
    print(expressions)
