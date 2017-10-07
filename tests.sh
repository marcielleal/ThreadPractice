#!/bin/bash

_PATH1="MeasuresSeq"
_PATH2="MeasuresConc"

chmod +x multimat_sequencial.py
chmod +x multimat_concorrente.py

((size=4))
while ((size<2048)); 
do
	((iter=0))
	while ((iter<20));
	do
		echo "SIZE="$size "ITER="$iter
		./multimat_sequencial.py $size >> $_PATH1/$size"x"$size
		./multimat_concorrente.py $size $size >> $_PATH2/$size"x"$size
		((iter++))
	done
	((size*=2))
done
