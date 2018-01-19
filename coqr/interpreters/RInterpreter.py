import warnings
from typing import List

import rpy2.rinterface as ri
import rpy2.robjects as robjects

from coqr.interpreters.AbstractInterpreter import AbstractInterpreter

warnings.filterwarnings("ignore", category=ri.RRuntimeWarning)


class RInterpreter(AbstractInterpreter):
    def __init__(self, interp) -> None:
        super().__init__(interp)
        self.name = "R"
        # TODO: Set R_HOME when creating this interpreter, based on param interp

    def interpret(self, expression):
        try:
            output = str(robjects.r(expression))
        except ri.RRuntimeError as err:
            output = err.args[0]
        return output

    def interpret_expressions(self, expressions: list):
        parenthesized_expressions = ["(%s)" % exp for exp in expressions]
        results = []
        robjects.r('rm(list = ls(all.names=TRUE))')
        for expression in parenthesized_expressions:
            output = self.interpret(expression)
            results.append(output)

        return results

