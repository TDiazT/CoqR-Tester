import subprocess
from subprocess import PIPE, STDOUT


class RRunner:
    rscript = "rscript"

    def run_expression(self, expression):
        return self.__run([self.rscript, "-e", expression])

    def run_file(self, filename):
        return self.__run([self.rscript, filename])

    @staticmethod
    def __run(cmd):
        return subprocess.run(cmd, universal_newlines=True, stdout=PIPE,
                              stderr=STDOUT).stdout
