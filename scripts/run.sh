#!/bin/bash


if [ -n "$1" ]
then

    if [ -f $1 ]
    then
        parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )

        SRC=$1
        OUT=cr_out

        ROUT=r.json
        COQOUT=coq.json
        SCRIPTS=$parent_path

        echo "Creating a directory named $OUT for output"
        mkdir -p $OUT

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
        echo "File not found"
    fi

else
    echo "Missing R source file to run"
fi