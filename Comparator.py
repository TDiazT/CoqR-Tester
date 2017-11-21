import subprocess
from subprocess import PIPE, STDOUT, Popen
import re

ERROR = "Error:"

NOT = "Not"

IMPOSSIBLE = "Impossible"

SEQ_TOKEN = "SPECIAL_SUPER_TOKEN"

CASE_NOT_IMPLEMENTED = "CASE_NOT_IMPLEMENTED"

CASE_ERROR = "CASE_ERROR"

CASE_IMPOSSIBLE = "CASE_IMPOSSIBLE"

CASE_ASSIGNMENT = "CASE_ASSIGNMENT"

# path_to_proveR = "/Users/Tomas/Documents/Memoria/Coq-R/proveR/low/runR.native"
path_to_proveR = ["make", "run", "-C", "/Users/Tomas/Documents/Memoria/Coq-R/proveR/"]
rscript = "rscript"

vec_res_regex = re.compile('\[\d+\]')


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

    splitlines_ = [line.split() for line in lines]

    return splitlines_


def clean_r_output(r_output):
    return [row.split() for row in r_output.splitlines()]


def resolve_coq_case(output):
    result = []

    for line in output:
        for word in line:
            if word == ERROR:
                result.append(CASE_ERROR)
                break
            elif word == NOT:
                result.append(CASE_NOT_IMPLEMENTED)
                break
            elif word == IMPOSSIBLE:
                result.append(CASE_IMPOSSIBLE)
                break
            elif vec_res_regex.match(word) is not None:
                if vec_res_regex.match(word).group() == '[1]':
                    if line[1] == '"%s"' % SEQ_TOKEN:
                        break
                    else:
                        result.append(line)
                else:
                    result[-1].append(line)
                break
            elif word == '>':
                continue
            else:
                break

    return result


def resolve_r_case(output):
    result = []
    flag = False

    if not output:
        result.append(CASE_ASSIGNMENT)
        return result

    for line in output:
        for word in line:
            if word == ERROR:
                result.append(CASE_ERROR)
                flag = False
                break
            elif vec_res_regex.match(word) is not None:
                if vec_res_regex.match(word).group() == '[1]':
                    if line[1] == '"%s"' % SEQ_TOKEN:
                        if not flag:
                            flag = True
                        else:
                            result.append(CASE_ASSIGNMENT)
                    else:
                        result.append(line)
                        flag = False
                else:
                    result[-1].append(line)
                    flag = False
                break
            elif word == SEQ_TOKEN:
                if not flag:
                    flag = True
                else:
                    result.append(CASE_ASSIGNMENT)
                break
            else:
                break

    return result


def compare_outputs(clean_coq_out, clean_r_out):
    coq_outputs = resolve_coq_case(clean_coq_out)
    r_outputs = resolve_r_case(clean_r_out)

    results = []
    for coq, r in zip(coq_outputs, r_outputs):
        if coq == CASE_NOT_IMPLEMENTED:
            results.append(CASE_NOT_IMPLEMENTED)
        elif coq == CASE_IMPOSSIBLE:
            results.append(CASE_IMPOSSIBLE)
        elif coq == CASE_ERROR:
            if r == CASE_ERROR:
                results.append("OK")
            else:
                results.append(CASE_ERROR)
        else:
            if r == CASE_ASSIGNMENT:
                results.append("OK")
            else:
                results.append("OK") if coq == r else results.append("Not equal")

    return results


def compare_outputs_for(expression):
    coq_output = run_coq_script_for(expression)
    r_output = run_r_script_for(expression)

    clean_coq_out = clean_coq_output(coq_output)
    clean_r_out = clean_r_output(r_output)

    return compare_outputs(clean_coq_out, clean_r_out)
