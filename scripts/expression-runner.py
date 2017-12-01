import sys
import subprocess
import os

expression = sys.argv[2]

if sys.argv[1] == 'R':
    r_interp = os.environ['RSCRIPT']
    out = subprocess.run([r_interp, '-e', expression, '--silent'], universal_newlines=True, stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT).stdout
else:
    coq_interp = os.environ['COQ_INTERP']

    p1 = subprocess.Popen(['echo', expression], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(['make', 'run', '-s', '-C', coq_interp], stdin=p1.stdout, stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT, universal_newlines=True)
    p1.stdout.close()
    out = p2.communicate()[0]
    splitlines_ = out.splitlines()[2:]
    splitlines_.pop()
    out = "\n".join(splitlines_)

print(out)
