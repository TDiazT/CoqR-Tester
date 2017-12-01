#!/bin/bash


if [ -n "$1" ]
then

    parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
    cd "$parent_path"
    cd ..

    SRC=$1
    OUT=out

    ROUT=r.json
    COQOUT=coq.json
    SCRIPTS=scripts


    source "$SCRIPTS/settings.sh"



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
    RSCRIPT=$RSCRIPT python $SCRIPTS/runner.py R $SRC "$OUT/$ROUT"

    echo "Running Coq interpreter"
    COQ_INTERP=$COQ_INTERP python $SCRIPTS/runner.py asdf $SRC $OUT/$COQOUT

    echo "Cleaning outputs"
    python $SCRIPTS/cleaner.py $OUT/$ROUT $OUT/clean-$ROUT
    python $SCRIPTS/cleaner.py $OUT/$COQOUT $OUT/clean-$COQOUT

    echo "Comparing"
    python $SCRIPTS/comparator.py $OUT/clean-$COQOUT $OUT/clean-$ROUT $OUT/comparison.json

    echo "Done"
else
    echo "Missing R source file to run"
fi