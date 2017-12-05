import subprocess


class CoqInterpreter:

    def __init__(self, path_to_interp) -> None:
        self.name = 'Coq'
        self.proveR = path_to_interp

    def interpret(self, expression):
        p1 = subprocess.Popen(['echo', expression], stdout=subprocess.PIPE)
        p2 = subprocess.Popen(['make', 'run', '-s', '-C', self.proveR], stdin=p1.stdout, stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT, universal_newlines=True)
        p1.stdout.close()
        return p2.communicate()[0]
