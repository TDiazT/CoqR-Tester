import subprocess


class CoqRunner:

    def __init__(self, path_to_interp) -> None:
        self.interpreter = 'Coq'
        self.proveR = path_to_interp

    def run(self, expression):
        p1 = subprocess.Popen(['echo', expression], stdout=subprocess.PIPE)
        p2 = subprocess.Popen(['make', 'run', '-s', '-C', self.proveR], stdin=p1.stdout, stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT, universal_newlines=True)
        p1.stdout.close()
        return p2.communicate()[0]
