#!/usr/bin/env python3

import sys
import multiplier
import squarematrix
import time

tstart=time.time()
PATH="Matrizes/"

try:
	size=int(sys.argv[1])
	threadNum=int(sys.argv[2])
	if (size<4 or size>2048 or threadNum<=1 or (size & (size-1))!=0):
		print("It is required an argument of type 2^n, where n is in [2,11] and a number of threads greater than 1:")
		print("./"+sys.argv[0]+" <integer> <number_of_threads>")
		sys.exit(1)

	fileName=sys.argv[1]+"x"+sys.argv[1]+".txt"
	arqA=open(PATH+"A"+fileName,"r")
	arqB=open(PATH+"B"+fileName,"r")

	A=squarematrix.SquareMatrix(file=arqA)
	B=squarematrix.SquareMatrix(file=arqB)

	C=multiplier.matrixmult(A,B,threadNum)
	#print(C)
except FileNotFoundError:
 	print("File not found")
 	sys.exit(2)
except Exception as exc:
	print(exc)
	sys.exit(3)

tend=time.time()

print (tend-tstart)
sys.exit(0)