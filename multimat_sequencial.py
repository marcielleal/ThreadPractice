#!/usr/bin/env python3

import sys
import multiplier
import squarematrix
import time

tstart=time.timer()
PATH="Matrizes/"

try:
	size=int(sys.argv[1])
	if (size<4 or size>2048 or (size & (size-1))!=0):
		print("It is required an argument of type 2^n, where n is in [2,11]")
		print("./"+sys.argv[0]+" <integer>")
		sys.exit(1)
	fileName=sys.argv[1]+"x"+sys.argv[1]+".txt"
	arqA=open(PATH+"A"+fileName,"r")
	arqB=open(PATH+"B"+fileName,"r")

	A=squarematrix.SquareMatrix(file=arqA)
	B=squarematrix.SquareMatrix(file=arqB)

	C=multiplier.matrixmult(A,B)

	print(C)

	sys.exit(0)
except FileNotFoundError:
	print("File not found")
	sys.exit(2)
tend=time.timer()

