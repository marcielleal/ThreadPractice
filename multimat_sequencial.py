#!/usr/bin/env python3

import sys
import squarematrix

PATH="Matrizes/"

try:
	size=int(sys.argv[1])
	if (size%2!=0 or size<4 or size>2048):
		raise IndexError()
	fileName=sys.argv[1]+"x"+sys.argv[1]+".txt"
	arqA=open(PATH+"A"+fileName,"r")
	arqB=open(PATH+"B"+fileName,"r")

	A=squarematrix.SquareMatrix(file=arqA)
	B=squarematrix.SquareMatrix(file=arqB)

	C=squarematrix.matrixmult(A,B)

	print(C)

	sys.exit(0)
except IndexError:
	print("It is required an argument of type 2^n, where n is in [2,11]. Example:")
	print("./"+sys.argv[1]+" <integer>")
	sys.exit(1)
except FileNotFoundError:
	print("File not found")
	sys.exit(2)