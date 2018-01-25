from typing import List, Tuple

import io
from antlr4 import *

from coqr.parsing.LineExpListener import LineExpListener
from coqr.parsing.ProgListener import ProgListener
from coqr.parsing.RFilter import RFilter
from coqr.parsing.RParser import RParser

from coqr.parsing.RLexer import RLexer


def parse_expression(expression: str) -> List[str]:
    """
    Parses a string and returns a list of expressions
    :param expression: String to parse
    :return: List of expressions (str)
    """
    stream = InputStream(expression)
    lexer = RLexer(stream)
    tokens = CommonTokenStream(lexer)

    tokens.fill()

    filter_ = RFilter(tokens)
    filter_.stream()
    tokens.reset()

    parser = RParser(tokens)
    tree = parser.prog()

    progListener = ProgListener(tokens)
    walker = ParseTreeWalker()
    walker.walk(progListener, tree)

    return progListener.exps


def parse_file(filename) -> List[Tuple[int, str]]:
    """
    Parses an R file and returns a list of expressions
    :param filename: file to parse
    :return: list of expressions (str)
    """
    input_ = FileStream(filename, encoding='utf-8')
    lexer = RLexer(input_)
    tokens = CommonTokenStream(lexer)

    tokens.fill()

    filter_ = RFilter(tokens)
    filter_.stream()
    tokens.reset()

    parser = RParser(tokens)
    tree = parser.prog()

    progListener = LineExpListener(tokens)
    walker = ParseTreeWalker()
    walker.walk(progListener, tree)

    return progListener.exps
