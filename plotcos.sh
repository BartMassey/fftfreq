#!/bin/sh
TMP=/tmp/plotcos.$$
trap "rm -f $TMP" 0 1 2 3 15
python3 cos.py "$@" > $TMP
echo "plot \"$TMP\" with lines;" | gnuplot -p
