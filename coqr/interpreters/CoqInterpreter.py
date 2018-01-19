import subprocess
from typing import List

import re

from coqr.interpreters.AbstractInterpreter import AbstractInterpreter


class CoqInterpreter(AbstractInterpreter):
    def __init__(self, interp) -> None:
        super().__init__(interp)
        self.name = 'Coq'

    def interpret(self, expression):
        p1 = subprocess.Popen(['echo', expression], stdout=subprocess.PIPE)
        p2 = subprocess.Popen(['make', 'run', '-s', '-C', self.interpreter], stdin=p1.stdout, stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT, universal_newlines=True)
        p1.stdout.close()
        return p2.communicate()[0]

    def interpret_expressions(self, expressions: list):
        parenthesized_expressions = ["(%s)" % exp for exp in expressions]
        tokenized = self.SEQUENCE_TOKEN.join(parenthesized_expressions)
        results = self.interpret(tokenized)

        return re.split(self.token_regex, results)
