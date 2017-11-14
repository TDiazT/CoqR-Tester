import subprocess
from subprocess import PIPE, STDOUT, Popen
import glob

path_to_proveR = "/Users/Tomas/Documents/Memoria/Coq-R/proveR/low/runR.native"
rscript = "rscript"


def run_script():
    return subprocess.run(["rscript", filename], universal_newlines=True, stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT).stdout


def clean_output(raw_output):
    return [row.split() for row in raw_output.splitlines()]


def run_coq_script():
    pass


def run_coq_script_for(expression):
    p1 = Popen(["echo", expression], stdout=PIPE)
    p2 = Popen(path_to_proveR, stdin=p1.stdout, stdout=PIPE, stderr=STDOUT, universal_newlines=True)
    p1.stdout.close()
    return p2.communicate()[0]


def run_r_scipt_for(expression):
    return subprocess.run([rscript, "-e", expression], universal_newlines=True, stdout=PIPE,
                          stderr=STDOUT).stdout


def clean_coq_output(coq_output):
    lines = coq_output.splitlines()
    # to remove 'Initialising...'
    lines.pop(0)
    # to remove 'Success.'
    lines.pop(0)
    # removes last '>'
    lines.pop()

    splitlines_ = [line.split() for line in lines]
    splitlines_[0].remove('>')
    if splitlines_[0][0] == "Success.":
        return splitlines_[1:]
    elif splitlines_[0][0] == "Error:":
        if splitlines_[0][2:] == ['Object', 'not', 'found.']:
            return "NOT_FOUND"
        return ""

def clean_r_output(r_output):
    splitlines_ = [row.split() for row in r_output.splitlines()]
    if splitlines_[0][0] == "[1]":
        return splitlines_
    elif splitlines_[0][0] == "Error:":
        if splitlines_[0][1] == 'object':
            return "NOT_FOUND"
        return ""


def compare_outputs(clean_coq_out, clean_r_out):
    return "OK" if clean_coq_out == clean_r_out else "Nop"


def compare_outputs_for(expression):
    coq_output = run_coq_script_for(expression)
    r_output = run_r_scipt_for(expression)

    clean_coq_out = clean_coq_output(coq_output)
    clean_r_out = clean_r_output(r_output)

    return compare_outputs(clean_coq_out, clean_r_out)


for filename in glob.iglob('RTests/**/*.R', recursive=True):
    coq_output = run_coq_script()
    output = run_script()
    cleaned_output = clean_output(output)
    print(cleaned_output)
