import logging
import os
import subprocess
import time
from typing import List, Tuple

from coqr.interpreters.AbstractInterpreter import AbstractInterpreter


class CoqInterpreter(AbstractInterpreter):
    final_state = '.CoqData'

    def __init__(self, interp, initial_state, debug=False) -> None:
        super().__init__(interp)
        self.name = 'Coq'
        self.initial_state = initial_state
        self.logger = logging.getLogger(__name__)
        self.logger.addHandler(logging.StreamHandler())
        if debug:
            self.logger.setLevel(logging.DEBUG)
        else:
            self.logger.setLevel(logging.INFO)

    def interpret(self, expression):
        p1 = subprocess.Popen(['echo', expression], stdout=subprocess.PIPE)

        if os.path.exists(self.final_state):
            initial_state = self.final_state
        else:
            initial_state = self.initial_state

        p2 = subprocess.Popen(
            [self.interpreter, '-initial-state', initial_state, '-final-state', self.final_state, '-hide-prompt'],
            stdin=p1.stdout, stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True)
        p1.stdout.close()

        return p2.communicate()[0]

    def interpret_expressions(self, expressions: list) -> List[Tuple[str, str, int]]:
        self.__remove_saved_data()
        results = []
        for expression in expressions:
            self.logger.debug("Interpreting %s" % expression)
            time_ = time.time()
            output = self.interpret("(" + expression + ")")
            results.append((expression, output, time.time() - time_))

        self.__remove_saved_data()
        return results

    def __remove_saved_data(self):
        try:
            os.remove(self.final_state)
        except OSError:
            pass
