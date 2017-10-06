#!/bin/bash

_PATH="MeasuresSeq"

chmod +x multimat_sequencial.py
chmod +x multimat_concorrente.py

((size=2048))
while ((size<=2048)); 
do
	((iter=0))
	while ((iter<20));
	do
		echo "SIZE="$size "ITER="$iter
		./multimat_sequencial.py $size >> $_PATH/$size"x"$size
		#./multimat_concorrente.py $size $1 >> $_PATH/$size"x"$size
		((iter++))
	done
	((size*=2))
done
