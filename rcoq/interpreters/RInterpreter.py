import subprocess


class RInterpreter:
    def __init__(self, rscript) -> None:
        self.name = "R"
        self.rscript = rscript

    def interpret(self, expression):
        return subprocess.run([self.rscript, '-e', expression], universal_newlines=True, stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT).stdout
