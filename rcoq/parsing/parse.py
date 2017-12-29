import sys

import re
from antlr4 import *
from antlr4.Token import CommonToken
from antlr4.tree.Trees import Trees

from rcoq.parsing.ProgListener import ProgListener
from rcoq.parsing.RFilter import RFilter
from rcoq.parsing.RLexer import RLexer
from rcoq.parsing.RListener import RListener
from rcoq.parsing.RParser import RParser


def main(argv):
    input_ = FileStream(argv[1])
    lexer = RLexer(input_)
    tokens = CommonTokenStream(lexer)

    tokens.fill()

    filter = RFilter(tokens)
    filter.stream()
    tokens.reset()

    parser = RParser(tokens)
    # parser.buildParseTrees = False
    tree = parser.prog()

    # output = open("output.R", "w")
    #
    htmlChat = ProgListener(tokens)
    walker = ParseTreeWalker()
    walker.walk(htmlChat, tree)

    # output.close()

    for exp in htmlChat.exps:
        print(exp)


if __name__ == '__main__':
    main(sys.argv)
