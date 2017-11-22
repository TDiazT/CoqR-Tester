from subprocess import Popen, PIPE, STDOUT


class CoqRunner:
    proveR = ["make", "run", "-C", "/Users/Tomas/Documents/Memoria/Coq-R/proveR/"]

    def run_expression(self, expression):
        p1 = Popen(["echo", expression], stdout=PIPE)
        p2 = Popen(self.proveR, stdin=p1.stdout, stdout=PIPE, stderr=STDOUT, universal_newlines=True)
        p1.stdout.close()
        return p2.communicate()[0]

    def run_file(self, filename):
        p1 = Popen(["cat", filename], stdout=PIPE)
        p2 = Popen(self.proveR, stdin=p1.stdout, stdout=PIPE, stderr=STDOUT, universal_newlines=True)
        p1.stdout.close()
        return p2.communicate()[0]
