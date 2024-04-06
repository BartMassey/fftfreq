#!/bin/sh
TMP=/tmp/plotcos.$$
trap "rm -f $TMP" 0 1 2 3 15
PNG=""
case "$1" in
    --png) PNG="set terminal png; set output \"plot.png\";"; shift ;;
esac

python3 cos.py --plot "$@" > $TMP
echo "$PNG plot \"$TMP\" with lines;" | gnuplot -p
