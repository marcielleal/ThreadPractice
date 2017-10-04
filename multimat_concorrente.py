#!/usr/bin/env python3

import sys
import squarematrix
import multiplier

try:
	PATH="Matrizes/"

	#try:
	size=int(sys.argv[1])
	threadNum=int(sys.argv[2])
	if (size<4 or size>2048 or threadNum<=1):
		print("It is required an argument of type 2^n, where n is in [2,11] and a number of threads greater than 1:")
		print("./"+sys.argv[0]+" <integer> <number_of_threads>")
		sys.exit(1)

	fileName=sys.argv[1]+"x"+sys.argv[1]+".txt"
	arqA=open(PATH+"A"+fileName,"r")
	arqB=open(PATH+"B"+fileName,"r")

	A=squarematrix.SquareMatrix(file=arqA)
	B=squarematrix.SquareMatrix(file=arqB)

	C=multiplier.matrixmult(A,B,threadNum)

	print(C)

	sys.exit(0)
except FileNotFoundError:
 	print("File not found")
 	sys.exit(2)