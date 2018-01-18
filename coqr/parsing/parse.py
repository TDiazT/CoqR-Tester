from antlr4 import *
from coqr.parsing.ProgListener import ProgListener
from coqr.parsing.RFilter import RFilter
from coqr.parsing.RParser import RParser

from coqr.parsing.RLexer import RLexer


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

    filter_ = RFilter(tokens)
    filter_.stream()
    tokens.reset()

    parser = RParser(tokens)
    tree = parser.prog()

    progListener = ProgListener(tokens)
    walker = ParseTreeWalker()
    walker.walk(progListener, tree)

    return progListener.exps

