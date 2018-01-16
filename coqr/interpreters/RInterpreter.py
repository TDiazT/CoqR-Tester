import subprocess

from coqr.interpreters.AbstractInterpreter import AbstractInterpreter


class RInterpreter(AbstractInterpreter):
    def __init__(self, interp) -> None:
        super().__init__(interp)
        self.name = "R"

    def interpret(self, expression):
        return subprocess.run([self.interpreter, '-e', expression], universal_newlines=True, stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT).stdout
