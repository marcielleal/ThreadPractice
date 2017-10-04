#!/usr/bin/env python3

import sys
import squarematrix

PATH="Matrizes/"

try:
	size=int(sys.argv[1])
	threadNum=int(sys.argv[2])
	if (size%2!=0 or size<4 or size>2048 or threadNum<=1):
		raise ValueError()

	fileName=sys.argv[1]+"x"+sys.argv[1]+".txt"
	arqA=open(PATH+"A"+fileName,"r")
	arqB=open(PATH+"B"+fileName,"r")

	A=squarematrix.SquareMatrix(file=arqA)
	B=squarematrix.SquareMatrix(file=arqB)

	C=squarematrix.matrixmult(A,B,threadNum)

	print(C)

	sys.exit(0)
except (IndexError,ValueError):
	print("It is required an argument of type 2^n, where n is in [2,11] and a number of threads greater than 1:")
	print("./"+sys.argv[1]+" <integer> <number_of_threads>")
	sys.exit(1)
except FileNotFoundError:
	print("File not found")
	sys.exit(2)