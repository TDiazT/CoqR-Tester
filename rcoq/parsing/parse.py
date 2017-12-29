import sys

from antlr4 import *

from rcoq.parsing.ProgListener import ProgListener
from rcoq.parsing.RFilter import RFilter
from rcoq.parsing.RLexer import RLexer
from rcoq.parsing.RParser import RParser


def parse_file(filename) -> list:
    """
    Parses an R file and returns a list of expressions
    :param filename: file to parse
    :return: list of expressions (str)
    """
    input_ = FileStream(filename)
    lexer = RLexer(input_)
    tokens = CommonTokenStream(lexer)

    tokens.fill()

    filter = RFilter(tokens)
    filter.stream()
    tokens.reset()

    parser = RParser(tokens)
    tree = parser.prog()

    progListener = ProgListener(tokens)
    walker = ParseTreeWalker()
    walker.walk(progListener, tree)

    return progListener.exps

