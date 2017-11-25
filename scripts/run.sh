#!/bin/bash

SRC=RTests/examples.R
SCRIPTS=scripts
OUT=out

echo "Running R interpreter"
python $SCRIPTS/runner.py R $SRC $OUT/r.json

echo "Running Coq interpreter"
COQ_INTERP=/Users/Tomas/Documents/Memoria/Coq-R/proveR/ python $SCRIPTS/runner.py asdf $SRC $OUT/coq.json

echo "Cleaning outputs"
python $SCRIPTS/cleaner.py $OUT/r.json $OUT/clean-r.json
python $SCRIPTS/cleaner.py $OUT/coq.json $OUT/clean-coq.json

echo "Comparing"
python $SCRIPTS/comparator.py $OUT/clean-coq.json $OUT/clean-r.json $OUT/comparison.json