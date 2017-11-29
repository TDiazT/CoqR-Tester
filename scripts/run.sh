#!/bin/bash

SRC=$1
OUT=out
ROUT=r.json
COQOUT=coq.json
SCRIPTS=scripts


if [ -z $2 ]
then
    ROUT=r.json
else
    ROUT=$2
fi

if [ -z $3 ]
then
    COQOUT=coq.json
else
    COQOUT=$3
fi

echo "Running R interpreter"
python $SCRIPTS/runner.py R $SRC "$OUT/$ROUT"

echo "Running Coq interpreter"
COQ_INTERP=/Users/Tomas/Documents/Memoria/Coq-R/proveR/ python $SCRIPTS/runner.py asdf $SRC $OUT/$COQOUT

echo "Cleaning outputs"
python $SCRIPTS/cleaner.py $OUT/$ROUT $OUT/clean-$ROUT
python $SCRIPTS/cleaner.py $OUT/$COQOUT $OUT/clean-$COQOUT

echo "Comparing"
python $SCRIPTS/comparator.py $OUT/clean-$COQOUT $OUT/clean-$ROUT $OUT/comparison.json

echo "Done"