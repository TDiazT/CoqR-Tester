#!/usr/bin/env bash

echo "R"

python expression-runner.py R "$1"

echo "Coq"

COQ_INTERP=/Users/Tomas/Documents/Memoria/Coq-R/proveR/ python expression-runner.py a "$1"
