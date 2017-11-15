import subprocess
from subprocess import PIPE, STDOUT, Popen

CASE_NOT_IMPLEMENTED = "NOT_IMPLEMENTED"

CASE_NOT_FOUND = "NOT_FOUND"

path_to_proveR = "/Users/Tomas/Documents/Memoria/Coq-R/proveR/low/runR.native"
rscript = "rscript"


def run_coq_script_for(expression):
    p1 = Popen(["echo", expression], stdout=PIPE)
    p2 = Popen(path_to_proveR, stdin=p1.stdout, stdout=PIPE, stderr=STDOUT, universal_newlines=True)
    p1.stdout.close()
    return p2.communicate()[0]


def run_r_script_for(expression):
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

    return splitlines_


def clean_r_output(r_output):
    return [row.split() for row in r_output.splitlines()]


def resolve_coq_case(output):
    if output[0][0] == "Success.":
        return output[1:]
    elif output[0][0] == "Error:":
        if output[0][2:] == ['Object', 'not', 'found.']:
            return CASE_NOT_FOUND
    elif output[0][0:2] == ["Not", "implemented:"]:
        return CASE_NOT_IMPLEMENTED
    else:
        return ""


def resolve_r_case(coq_res, r_out):
    if not r_out:
        if not coq_res == CASE_NOT_FOUND:
            return coq_res
    elif r_out[0][0] == "[1]":
        return r_out
    elif r_out[0][0] == "Error:":
        if r_out[0][1] == 'object':
            return CASE_NOT_FOUND


def compare_outputs(clean_coq_out, clean_r_out):
    coq_res = resolve_coq_case(clean_coq_out)

    if coq_res == CASE_NOT_IMPLEMENTED:
        return CASE_NOT_IMPLEMENTED

    r_res = resolve_r_case(coq_res, clean_r_out)

    return "OK" if coq_res == r_res else "Nop"


def compare_outputs_for(expression):
    coq_output = run_coq_script_for(expression)
    r_output = run_r_script_for(expression)

    clean_coq_out = clean_coq_output(coq_output)
    clean_r_out = clean_r_output(r_output)

    return compare_outputs(clean_coq_out, clean_r_out)
