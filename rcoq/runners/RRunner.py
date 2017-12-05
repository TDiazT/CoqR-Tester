import subprocess


class RRunner:
    def __init__(self, rscript) -> None:
        self.interpreter = "R"
        self.rscript = rscript

    def run(self, expression):
        return subprocess.run([self.rscript, '-e', expression], universal_newlines=True, stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT).stdout
