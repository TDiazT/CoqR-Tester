import subprocess
from typing import List

import re

import os

from coqr.interpreters.AbstractInterpreter import AbstractInterpreter


class CoqInterpreter(AbstractInterpreter):
    final_state = '.CoqData'

    def __init__(self, interp) -> None:
        super().__init__(interp)
        self.name = 'Coq'
        self.exec_path = os.path.join(self.interpreter, 'low', 'runR.native')

    def interpret(self, expression):
        p1 = subprocess.Popen(['echo', expression], stdout=subprocess.PIPE)

        if os.path.exists(self.final_state):
            initial_state = self.final_state
        else:
            initial_state = os.path.join(self.interpreter, 'low', 'initial.state')

        p2 = subprocess.Popen([self.exec_path, '-initial-state', initial_state, '-final-state', self.final_state],
                              stdin=p1.stdout, stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT,
                              universal_newlines=True)
        p1.stdout.close()

        return p2.communicate()[0]

    def interpret_expressions(self, expressions: list):
        parenthesized_expressions = ["(%s)" % exp for exp in expressions]
        self.__remove_saved_data()
        results = []
        for expression in parenthesized_expressions:
            results.append(self.interpret(expression))
        self.__remove_saved_data()

        return results

    def __remove_saved_data(self):
        try:
            os.remove(self.final_state)
        except OSError:
            pass
