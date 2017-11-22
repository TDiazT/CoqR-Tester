from subprocess import Popen, PIPE, STDOUT


class CoqRunner:
    proveR = ["make", "run", "-C", "/Users/Tomas/Documents/Memoria/Coq-R/proveR/"]

    def run_expression(self, expression):
        return self.__run(["echo", expression])

    def run_file(self, filename):
        return self.__run(["cat", filename])

    def __run(self, cmd):
        p1 = Popen(cmd, stdout=PIPE)
        p2 = Popen(self.proveR, stdin=p1.stdout, stdout=PIPE, stderr=STDOUT, universal_newlines=True)
        p1.stdout.close()
        return p2.communicate()[0]