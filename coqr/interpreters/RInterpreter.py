import os
import subprocess
from typing import Tuple, List

import time

from coqr.interpreters.AbstractInterpreter import AbstractInterpreter


class RInterpreter(AbstractInterpreter):
    def __init__(self, interp) -> None:
        super().__init__(interp)
        self.name = "R"

    def interpret(self, expression):
        p1 = subprocess.Popen(['echo', expression], stdout=subprocess.PIPE)
        p2 = subprocess.Popen([self.interpreter, '--slave', '--save', '--restore'], stdin=p1.stdout,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT, universal_newlines=True)
        p1.stdout.close()
        return p2.communicate()[0]

    def interpret_expressions(self, expressions: list) -> List[Tuple[str, str, int]]:
        parenthesized_expressions = ["(%s)" % exp for exp in expressions]

        self.__remove_saved_data()
        results = []
        for expression in parenthesized_expressions:
            time_ = time.time()
            output = self.interpret(expression)
            results.append((expression, output, time.time() - time_))

        self.__remove_saved_data()
        return results

    def __remove_saved_data(self):
        try:
            os.remove('.RData')
        except OSError:
            pass
