#!/usr/bin/env bash

source settings.sh

echo "R"

RSCRIPT=$RSCRIPT $PYTHON expression-runner.py R "$1"

echo "Coq"

COQ_INTERP=$COQ_INTERP $PYTHON expression-runner.py a "$1"
