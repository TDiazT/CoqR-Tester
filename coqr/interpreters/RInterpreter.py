import subprocess

from coqr.interpreters.AbstractInterpreter import AbstractInterpreter


class RInterpreter(AbstractInterpreter):
    def __init__(self, interp) -> None:
        super().__init__(interp)
        self.name = "R"

    def interpret(self, expression):
        p1 = subprocess.Popen(['echo', expression], stdout=subprocess.PIPE)
        p2 = subprocess.Popen([self.interpreter, '--slave'], stdin=p1.stdout, stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT, universal_newlines=True)
        p1.stdout.close()
        return p2.communicate()[0]
